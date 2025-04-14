import streamlit as st
import base64
import tempfile
import os
import subprocess

# --- LaTeX Generation Functions (Keep As Is) ---
def generate_resume(data):
    # (Your existing generate_resume function - no changes needed here)
    latex_template = r'''%-------------------------
% Resume in Latex
% Author : Jake Gutierrez
% Based off of: https://github.com/sb2nov/resume
% License : MIT
%------------------------

\documentclass[letterpaper,11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{fontawesome5}
\usepackage{multicol}
\setlength{\multicolsep}{-3.0pt}
\setlength{\columnsep}{-1pt}
\input{glyphtounicode}


%----------FONT OPTIONS----------
% sans-serif
% \usepackage[sfdefault]{FiraSans}
% \usepackage[sfdefault]{roboto}
% \usepackage[sfdefault]{noto-sans}
% \usepackage[default]{sourcesanspro}

% serif
% \usepackage{CormorantGaramond}
% \usepackage{charter}


\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.6in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1.19in}
\addtolength{\topmargin}{-.7in}
\addtolength{\textheight}{1.4in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large\bfseries
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\classesList}[4]{
    \item\small{
        {#1 #2 #3 #4 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & \textbf{\small #2} \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{1.001\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & \textbf{\small #2}\\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemi{$\vcenter{\hbox{\tiny$\bullet$}}$}
\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%


\begin{document}

%----------HEADING----------
\begin{center}
    {\Huge \scshape ''' + data.get("full_name", "") + r'''} \\ \vspace{1pt}
    ''' + data.get("university", "") + r''', ''' + data.get("university_location", "") + r''' \\ \vspace{1pt}
    \small \raisebox{-0.1\height}\faPhone\ ''' + data.get("phone", "") + r''' ~ \href{mailto:''' + data.get("email", "") + r'''}{\raisebox{-0.2\height}\faEnvelope\  \underline{''' + data.get("email", "") + r'''}} ~
    \href{''' + data.get("linkedin", "") + r'''}{\raisebox{-0.2\height}\faLinkedin\ \underline{''' + data.get("linkedin", "").replace("https://", "") + r'''}}  ~
    \href{''' + data.get("github", "") + r'''}{\raisebox{-0.2\height}\faGithub\ \underline{''' + data.get("github", "").replace("https://", "") + r'''}}
    \vspace{-8pt}
\end{center}


%-----------EDUCATION-----------
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {''' + data.get("university", "") + r'''}{''' + data.get("education_period", "") + r'''}
      {''' + data.get("degree", "") + r'''}{''' + data.get("university_location", "") + r'''}
  \resumeSubHeadingListEnd

%------RELEVANT COURSEWORK-------
\section{Relevant Coursework}
    \begin{multicols}{4}
        \begin{itemize}[itemsep=-5pt, parsep=3pt]
'''

    # Add coursework items
    for course in data.get("coursework", []):
        if course and course.strip():
            latex_template += r'            \item\small ' + course + '\n'

    latex_template += r'''        \end{itemize}
    \end{multicols}
    \vspace*{2.0\multicolsep}

%-----------EXPERIENCE-----------
\section{Experience}
  \resumeSubHeadingListStart
'''

    # Add experience entries
    for exp in data.get("experiences", []):
        if exp.get("company", "").strip():
            latex_template += r'''
    \resumeSubheading
      {''' + exp.get("company", "") + r'''}{''' + exp.get("exp_period", "") + r'''}
      {''' + exp.get("position", "") + r'''}{''' + exp.get("location", "") + r'''}
      \resumeItemListStart
'''
            for resp in exp.get("responsibilities", []):
                if resp and resp.strip():
                    latex_template += r'        \resumeItem{' + resp + r'}' + '\n'

            latex_template += r'''      \resumeItemListEnd
'''

    latex_template += r'''  \resumeSubHeadingListEnd

%-----------PROJECTS-----------
\section{Projects}
    \vspace{-5pt}
    \resumeSubHeadingListStart
'''

    # Add project entries
    for proj in data.get("projects", []):
        if proj.get("name", "").strip():
            latex_template += r'''      \resumeProjectHeading
          {\textbf{''' + proj.get("name", "") + r'''} $|$ \emph{''' + proj.get("technologies", "") + r'''}}''' + '{' + proj.get("date", "") + r'''}
          \resumeItemListStart
'''
            for desc in proj.get("descriptions", []):
                if desc and desc.strip():
                    latex_template += r'            \resumeItem{' + desc + r'}' + '\n'

            latex_template += r'''          \resumeItemListEnd
          \vspace{-13pt}
'''

    latex_template += r'''    \resumeSubHeadingListEnd
\vspace{10pt}

%-----------Certifications------------
\section{Certifications and Licenses}
    \vspace{-5pt}
    \resumeSubHeadingListStart
      \resumeProjectHeading
          {\textbf{Professional Certifications}}{''' + data.get("cert_period", "") + r'''}
          \resumeItemListStart
'''

    # Add certification entries
    for cert in data.get("certifications", []):
        if cert and cert.strip():
            latex_template += r'            \resumeItem{' + cert + r'}' + '\n'

    latex_template += r'''          \resumeItemListEnd
          \vspace{-13pt}
    \resumeSubHeadingListEnd
\vspace{10pt}

%-----------PROGRAMMING SKILLS-----------
\section{Technical Skills}
\begin{itemize}[leftmargin=0.15in, label={}]
    \small{\item{
        \textbf{Languages:} ''' + data.get("languages", "") + r''' \\
        \textbf{Tools:} ''' + data.get("tools", "") + r''' \\
        \textbf{Technologies/Frameworks:} ''' + data.get("technologies", "") + r''' \\
    }}
\end{itemize}
\vspace{-16pt}

\vspace{10pt}
%-----------INVOLVEMENT---------------
\section{Extracurricular}
    \resumeSubHeadingListStart
'''

    # Add extracurricular entries
    for extra in data.get("extracurriculars", []):
        if extra.get("activity", "").strip():
            latex_template += r'''        \resumeSubheading{''' + extra.get("activity", "") + r'''}{''' + extra.get("period", "") + r'''}
        {''' + extra.get("position", "") + r'''}{''' + extra.get("date", "") + r'''}
            \resumeItemListStart
                \resumeItem{''' + extra.get("description", "") + r'''}
            \resumeItemListEnd
'''

    latex_template += r'''    \resumeSubHeadingListEnd

\end{document}'''

    # Add .get() with defaults for robustness in the template filling
    # This prevents errors if a key is missing when generating LaTeX
    # (e.g., if a user sets 0 projects and the code tries to access data["projects"])

    return latex_template


def compile_latex_to_pdf(latex_content):
    with tempfile.TemporaryDirectory() as temp_dir:
        tex_file_path = os.path.join(temp_dir, "resume.tex")
        pdf_file_path = os.path.join(temp_dir, "resume.pdf") # Define path early

        try:
            with open(tex_file_path, "w", encoding="utf-8") as tex_file:
                tex_file.write(latex_content)
        except Exception as e:
            st.error(f"Error writing temporary LaTeX file: {e}")
            return None

        # --- First Run ---
        try:
            process1 = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-output-directory", temp_dir, tex_file_path],
                capture_output=True, text=True, encoding="utf-8", errors='ignore', timeout=30 # Added timeout
            )
        except FileNotFoundError:
             st.error("Error: 'pdflatex' command not found. Ensure LaTeX (like MiKTeX) is installed and in PATH.")
             return None
        except subprocess.TimeoutExpired:
            st.error("Error: pdflatex (first run) timed out. The LaTeX document might be too complex or stuck.")
            return None
        except Exception as e:
            st.error(f"Error during first pdflatex run: {e}")
            return None

        # --- Second Run (often needed) ---
        process2 = None # Initialize
        try:
            if os.path.exists(tex_file_path): # Only run if first step didn't fail badly
                process2 = subprocess.run(
                   ["pdflatex", "-interaction=nonstopmode", "-output-directory", temp_dir, tex_file_path],
                   capture_output=True, text=True, encoding="utf-8", errors='ignore', timeout=30 # Added timeout
                )
            else:
                 st.error("Cannot perform second pdflatex run, .tex file missing.")
                 # Optionally show process1 logs here if needed
                 return None

        except subprocess.TimeoutExpired:
            st.error("Error: pdflatex (second run) timed out.")
            # Optionally show process1/process2 logs
            return None
        except Exception as e:
             st.error(f"Error during second pdflatex run: {e}")
             # Optionally show process1/process2 logs
             return None


        # --- !!! DEBUGGING BLOCK !!! ---
        st.divider()
        st.subheader("Debugging Info (Python Check)")
        if process2:
             st.write(f"Second run command args: `{process2.args}`")
             st.write(f"Second run return code: `{process2.returncode}`")
        else:
             st.write("Second run did not execute (process2 is None).")

        st.write(f"Checking for PDF at path: `{pdf_file_path}`")
        pdf_exists = os.path.exists(pdf_file_path)
        st.write(f"Does PDF file exist according to Python? `{pdf_exists}`")

        if not pdf_exists and process2 and process2.returncode == 0:
            # If Python thinks the file doesn't exist, but LaTeX seemed okay, list dir
            try:
                st.warning(f"Listing files in temp directory ({temp_dir}):")
                st.json(os.listdir(temp_dir)) # Use json for better list display
            except Exception as e:
                st.error(f"Could not list files in temp dir: {e}")
        st.divider()
        # --- !!! END DEBUGGING BLOCK !!! ---


        # --- The Original Check (Now Informed by Debug Output) ---
        final_return_code = process2.returncode if process2 is not None else -1 # Use -1 if second run failed to start

        if final_return_code != 0 or not pdf_exists:
            st.error("LaTeX Compilation Failed (as determined by Python check). Check inputs or logs.") # Modified message

            # Display logs from the process that likely failed (process2 if it ran, else process1)
            log_content = "Log file not found or process did not run."
            log_path = os.path.join(temp_dir, "resume.log")
            if os.path.exists(log_path):
                 try:
                     with open(log_path, "r", encoding="utf-8", errors='ignore') as log_file:
                         log_content = log_file.read()
                 except Exception as e:
                     log_content = f"Error reading log file: {e}"

            st.error("pdflatex Log:")
            st.code(log_content[-3000:], language="log") # Show more log

            return None
        else:
            # Success path
            st.success("Python check passed: PDF exists and return code is 0.")
            try:
                with open(pdf_file_path, "rb") as pdf_file:
                    pdf_content = pdf_file.read()
                    st.write(f"Successfully read {len(pdf_content)} bytes from PDF.")
                    return pdf_content
            except Exception as e:
                st.error(f"Error reading PDF file even though it exists: {e}")
                # Display log here too, maybe reading failed due to lock?
                # ... (code to display log again) ...
                return None

def download_pdf_link(pdf_content, filename="resume.pdf"):
    """Generates a link to download the PDF."""
    b64_pdf = base64.b64encode(pdf_content).decode()
    return f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="{filename}">Download PDF</a>'

def download_latex_link(latex_content, filename="resume.tex"):
    """Generates a link to download the LaTeX source."""
    b64_latex = base64.b64encode(latex_content.encode('utf-8')).decode() # Ensure utf-8 encoding
    return f'<a href="data:text/latex;base64,{b64_latex}" download="{filename}">Download LaTeX Source (.tex)</a>'

# --- Streamlit App ---
st.markdown('''Fill in the details below. Do not leave any field blank. Learn how to write a resume [here](https://www.indeed.com/career-advice/resumes/how-to-write-a-resume).''')

# --- Initialize Session State ---
# This ensures the values persist across reruns
if 'num_experiences' not in st.session_state:
    st.session_state.num_experiences = 1
if 'num_projects' not in st.session_state:
    st.session_state.num_projects = 1
if 'num_extras' not in st.session_state:
    st.session_state.num_extras = 1


# --- The Form ---
# All inputs that need to be submitted together go inside the form
with st.form("resume_form"):
    # Use columns for better layout
    col1, col2 = st.columns(2)

    with col1:
        st.header("Personal Information")
        # Add keys to all form elements to preserve state during reruns
        st.text_input("Full Name", "John Doe", key="full_name")
        st.text_input("Phone", "123-456-7890", key="phone")
        st.text_input("Email", "john.doe@example.com", key="email")
        st.text_input("LinkedIn URL", "https://linkedin.com/in/johndoe", key="linkedin")
        st.text_input("GitHub URL", "https://github.com/johndoe", key="github")

        st.header("Education")
        st.text_input("University Name", "Example University", key="university")
        st.text_input("University Location", "City, State", key="university_location")
        st.text_input("Degree", "Bachelor of Science in Computer Science", key="degree")
        st.text_input("Education Period (e.g., Aug. 2020 -- May 2024)", "Aug. 2020 -- May 2024", key="education_period")

    with col2:
        st.header("Technical Skills")
        st.text_input("Programming Languages", "Python, Java, C++", key="languages")
        st.text_input("Tools", "VS Code, Git, Docker, Jupyter", key="tools")
        st.text_input("Technologies/Frameworks", "React, Node.js, Django, Pandas, Scikit-learn", key="technologies")

        st.header("Relevant Coursework")
        st.text_area("Coursework (one per line)",
                     "Data Structures\nAlgorithms\nSoftware Engineering\nDatabase Management\nOperating Systems\nMachine Learning",
                     key="coursework_text", height=150)

        st.header("Certifications")
        st.text_input("Certification Period (Optional)", "Issued 2023", key="cert_period")
        st.text_area("Certifications & Licenses (one per line)",
                     "AWS Certified Cloud Practitioner\nGoogle Data Analytics Professional Certificate",
                     key="certifications_text", height=100)

    st.markdown("---") # Separator

    # --- Dynamic Sections Inside Form ---

    # Experience
    st.header("Experience")
    # Use the number from session state to control the loop
    for i in range(st.session_state.num_experiences):
        st.subheader(f"Experience {i+1}")
        exp_cols = st.columns([2, 2, 1, 2]) # Adjust column widths as needed
        with exp_cols[0]:
            # Use unique keys for each input inside the loop
            st.text_input(f"Company","Company Name",  key=f"exp_company_{i}")
        with exp_cols[1]:
            st.text_input(f"Position","Your Role",  key=f"exp_position_{i}")
        with exp_cols[2]:
            st.text_input(f"Location", "City, ST", key=f"exp_location_{i}")
        with exp_cols[3]:
            st.text_input(f"Period", "Mon YYYY - Mon YYYY", key=f"exp_period_{i}")
        st.text_area(f"Responsibilities (one per line)", 
                     f"- Achieved X by doing Y using Z\n- Led team initiative...",
                      key=f"exp_responsibilities_{i}",
                      height=100)
        st.markdown("---")

    # Projects
    st.header("Projects")
    for i in range(st.session_state.num_projects):
        st.subheader(f"Project {i+1}")
        proj_cols = st.columns([2, 2, 1])
        with proj_cols[0]:
            st.text_input(f"Project Name","Awesome Project", key=f"proj_name_{i}")
        with proj_cols[1]:
            st.text_input(f"Technologies Used","Python, Streamlit, Pandas", key=f"proj_technologies_{i}")
        with proj_cols[2]:
            st.text_input(f"Date", "Fall 2023", key=f"proj_date_{i}")
        st.text_area(f"Description (one bullet point per line)",
                     f"- Developed feature A solving problem B\n- Implemented algorithm C for efficiency",
                     key=f"proj_descriptions_{i}",
                     height=100
                )
        st.markdown("---")

    # Extracurricular
    st.header("Extracurricular Activities")
    for i in range(st.session_state.num_extras):
        st.subheader(f"Activity {i+1}")
        extra_cols = st.columns([2, 2, 1, 1])
        with extra_cols[0]:
            st.text_input(f"Activity/Organization Name","Coding Club", key=f"extra_activity_{i}")
        with extra_cols[1]:
            st.text_input(f"Position/Role", "President",key=f"extra_position_{i}")
        with extra_cols[2]:
            st.text_input(f"Period", "YYYY - YYYY", key=f"extra_period_{i}")
        with extra_cols[3]:
            st.text_input(f"Location/Date","University / May 2023", key=f"extra_date_{i}") # Combined date/location for simplicity
        st.text_area(f"Description/Achievements (one per line)","- Organized weekly workshops...", key=f"extra_description_{i}", height=75)
        st.markdown("---")

    # Submit Button
    st.markdown("---")
    submitted = st.form_submit_button("Generate Resume PDF & LaTeX")

# --- Post-Submission Logic ---
if submitted:
    # Collect data from st.session_state using the assigned keys
    data = {
        "full_name": st.session_state.get("full_name", ""),
        "phone": st.session_state.get("phone", ""),
        "email": st.session_state.get("email", ""),
        "linkedin": st.session_state.get("linkedin", ""),
        "github": st.session_state.get("github", ""),
        "university": st.session_state.get("university", ""),
        "university_location": st.session_state.get("university_location", ""),
        "degree": st.session_state.get("degree", ""),
        "education_period": st.session_state.get("education_period", ""),
        "coursework": st.session_state.get("coursework_text", "").split("\n"),
        "cert_period": st.session_state.get("cert_period", ""),
        "certifications": st.session_state.get("certifications_text", "").split("\n"),
        "languages": st.session_state.get("languages", ""),
        "tools": st.session_state.get("tools", ""),
        "technologies": st.session_state.get("technologies", ""),
    }

    # Collect experience data
    experiences_data = []
    for i in range(st.session_state.num_experiences):
        exp = {
            "company": st.session_state.get(f"exp_company_{i}", ""),
            "position": st.session_state.get(f"exp_position_{i}", ""),
            "location": st.session_state.get(f"exp_location_{i}", ""),
            "exp_period": st.session_state.get(f"exp_period_{i}", ""),
            "responsibilities": st.session_state.get(f"exp_responsibilities_{i}", "").split("\n")
        }
        # Only add if company name is provided
        if exp["company"].strip():
            experiences_data.append(exp)
    data["experiences"] = experiences_data

    # Collect project data
    projects_data = []
    for i in range(st.session_state.num_projects):
        proj = {
            "name": st.session_state.get(f"proj_name_{i}", ""),
            "technologies": st.session_state.get(f"proj_technologies_{i}", ""),
            "date": st.session_state.get(f"proj_date_{i}", ""),
            "descriptions": st.session_state.get(f"proj_descriptions_{i}", "").split("\n")
        }
        if proj["name"].strip():
             projects_data.append(proj)
    data["projects"] = projects_data

    # Collect extracurricular data
    extras_data = []
    for i in range(st.session_state.num_extras):
        extra = {
            "activity": st.session_state.get(f"extra_activity_{i}", ""),
            "position": st.session_state.get(f"extra_position_{i}", ""),
            "period": st.session_state.get(f"extra_period_{i}", ""),
            "date": st.session_state.get(f"extra_date_{i}", ""), # Corresponds to 'Achievement Date' in old code? Renamed field
            "description": st.session_state.get(f"extra_description_{i}", "") # Only one description field now based on text_area
        }
        # Split description into list if needed by LaTeX template, or adjust template
        # For simplicity here, assume template takes a single string description.
        # If template needs a list:
        # extra["description_list"] = st.session_state.get(f"extra_description_{i}", "").split("\n")

        if extra["activity"].strip():
            extras_data.append(extra)
    data["extracurriculars"] = extras_data

    # Generate LaTeX content
    latex_content = generate_resume(data)

    with st.spinner("Compiling LaTeX to PDF..."):
        pdf_content = compile_latex_to_pdf(latex_content)

    if pdf_content:
        st.success("PDF compiled successfully!")
        # Create download buttons
        st.markdown(download_pdf_link(pdf_content), unsafe_allow_html=True)
        st.markdown(download_latex_link(latex_content), unsafe_allow_html=True)
        # Optional: Display preview (might require extra libraries like PyMuPDF)
        # st.pdf_viewer(pdf_content) # Streamlit's built-in PDF display if available/desired
    else:
        st.error("Failed to generate PDF. See error messages above.")
        # Offer LaTeX download even if PDF fails
        st.markdown(download_latex_link(latex_content), unsafe_allow_html=True)
        st.warning("You can download the LaTeX (.tex) file and try compiling it manually.")