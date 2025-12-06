import streamlit as st

FOOTER_HTML = """
<div class_name="footer-container">
    <hr class_name="footer-divider">
    <p class_name="footer-text">
        © 2025 | Developed by Anastasiia Hileta<br>
        Institution of Computer Science and Informational Technologies, Lviv Polytechnic National University
    </p>
    <div class_name="social-icons">
        <a href="https://facebook.com" target="_blank" class_name="social-icon"><i class_name="fab fa-facebook-f"></i></a>
        <a href="https://instagram.com" target="_blank" class_name="social-icon"><i class_name="fab fa-instagram"></i></a>
        <a href="https://twitter.com" target="_blank" class_name="social-icon"><i class_name="fab fa-twitter"></i></a>
        <a href="https://linkedin.com" target="_blank" class_name="social-icon"><i class_name="fab fa-linkedin-in"></i></a>
        <a href="https://github.com" target="_blank" class_name="social-icon"><i class_name="fab fa-github"></i></a>
    </div>
</div>
"""

def render_footer():
    """
    Renders the custom HTML footer.
    We are using class_name instead of class to avoid Python syntax issues,
    and we will fix it in app.py before rendering.
    """
    st.markdown(FOOTER_HTML.replace('class_name=', 'class='), unsafe_allow_html=True)