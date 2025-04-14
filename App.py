import streamlit as st
from streamlit_extras.buy_me_a_coffee import button


st.set_page_config(layout="wide")

Main = st.Page(
    page="pages/Main.py",
    icon="📝",
    title="Write Resume",
    default=True,
)
ReqPage = st.Page(
    page="pages/Req.py",
    icon="🚀",
    title="Requirements",
)

About = st.Page(
    page="pages/About.py",
    icon="👤",    
    title = "About"
)


with st.sidebar:
    st.header("Section Counts")
    st.number_input(
        "Number of Experiences",
        min_value=1,
        max_value=5, # Adjust max as needed
        key='num_experiences' # Link to session state
    )
    st.number_input(
        "Number of Projects",
        min_value=1,
        max_value=5,
        key='num_projects' # Link to session state
    )
    st.number_input(
        "Number of Extracurricular Activities",
        min_value=1,
        max_value=3,
        key='num_extras' # Link to session state
    )
    st.logo('assets/logo.png', size="large")
    st.markdown(4*'''<br>''', unsafe_allow_html=True)
    st.caption("Support me by clicking on this button 👇")
    button(username="astrayn", floating=False, width=221)
    st.caption('0.0.1')
pg = st.navigation([Main, ReqPage, About])
pg.run()