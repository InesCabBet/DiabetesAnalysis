import streamlit as st

pg_intro = st.Page("intro.py", title="Introducción")

navigation_env = st.navigation(
    {
        "": [pg_intro]

    }
)

navigation_env.run()