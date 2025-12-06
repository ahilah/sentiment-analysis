import os
import streamlit as st

def load_css(file_path):
    """
    Loads a CSS file and injects it into the Streamlit app.
    """
    try:
        with open(file_path) as f:
            css = f.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found at {file_path}")