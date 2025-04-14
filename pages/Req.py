import streamlit as st

def get_started_page():

    st.markdown("## Getting Started")

    # 1. Clone the repository
    st.markdown("### 1. Clone the Repository")
    st.code("git clone https://github.com/your-username/resume-generator.git\ncd resume-generator", language="bash")

    # 2. Install Python Dependencies
    st.markdown("### 2. Install Python Dependencies")
    st.write("Make sure you have Python 3.7+ installed. Then install dependencies:")
    st.code("pip install -r requirements.txt", language="bash")

    st.write("Or install manually:")
    st.code("pip install streamlit", language="bash")


    # 3. Install a LaTeX Compiler
    st.markdown("### 3. Install a LaTeX Compiler")
    st.write("The app uses `pdflatex` to convert `.tex` files into `.pdf`. Choose your OS below:")

    # Windows
    st.markdown("#### Windows")
    st.markdown("- Download and install [MiKTeX](https://miktex.org/download)")
    st.markdown("- Ensure `pdflatex` is added to your system `PATH`")
    st.write("Verify installation:")
    st.code("pdflatex --version", language="bash")

    # Linux
    st.markdown("#### Linux")
    st.code("sudo apt update\nsudo apt install texlive-latex-base", language="bash")

    # macOS
    st.markdown("#### macOS")
    st.code("brew install --cask mactex", language="bash")
    st.markdown("Or download from: [https://tug.org/mactex/](https://tug.org/mactex/)")

    # Run App
    st.markdown("---")
    st.markdown("##  Run the App")
    st.code("streamlit run app.py", language="bash")
    st.write("The app will open in your browser at `http://localhost:8501`.")

    # Requirements
    st.markdown("## Required Libraries")
    st.code("streamlit\npdflatex", language="bash")

get_started_page()