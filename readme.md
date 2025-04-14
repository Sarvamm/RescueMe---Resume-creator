# 🚀 RescueMé! – LaTeX Resume Generator using Streamlit

Create beautiful, professional resumes using LaTeX – no LaTeX knowledge required!

RescueMé! is a web app built with [Streamlit](https://streamlit.io/) that lets you fill out a form and instantly generate a polished PDF resume using a LaTeX template. It’s fast, open-source, and easy to use.

![RescueMé Banner](https://raw.githubusercontent.com/Sarvamm/rescueme/refs/heads/main/assets/logo.png)



## 📦 Features

- Fill in your resume content using simple forms  
- Auto-generate `.tex` source file from inputs  
- Compiles LaTeX to high-quality PDF resume  
- Download the final PDF instantly  

---

## 🛠 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sarvamm/rescueme.git
cd rescueme
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit
```

> Other libraries used (`os`, `base64`, `subprocess`, `tempfile`) are part of the Python standard library.

---

### 3. Install a LaTeX Compiler

The app uses `pdflatex` to compile LaTeX into PDF.

#### Windows

- Install [MiKTeX](https://miktex.org/download)
- Ensure `pdflatex` is added to your system `PATH`
- Test it:

```bash
pdflatex --version
```

#### Linux

```bash
sudo apt update
sudo apt install texlive-latex-base
```

#### macOS

```bash
brew install --cask mactex
```

Or get MacTeX from [https://tug.org/mactex/](https://tug.org/mactex/)

---

##  Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

---

## 📁 Project Structure
```
RESCUEME/
│
├── .streamlit/
│   └── config.toml               # Streamlit app config (title, icon, etc.)
│
├── assets/
│   └── logo.png                  # App logo
│
├── pages/                        # Multi-page structure for Streamlit
│   ├── About.py                  # About page of RescueMé!
│   ├── GetStarted.py             # Setup & installation instructions
│   └── Main.py                   # Main functionality (resume generation)
│
├── App.py                        # Entry point of the Streamlit app
├── LICENSE                       # MIT License for open-source usage
├── readme.md                     # Project overview and usage guide
└── Requirement.txt               # Python dependencies
```

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo, make improvements, and submit a PR.  
For major changes, please open an issue first to discuss what you’d like to change.

---

## 📬 Contact
 
🔗 [LinkedIn](https://www.linkedin.com/in/sarvamm) • [GitHub](https://github.com/sarvamm)

---

## 📃 License

This project is licensed under the MIT License.
```

---
