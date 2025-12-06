import streamlit as st
import os
from ui_tabs.footer import render_footer

WORKFLOW_HTML = """
<div class="workflow-container">
    <div class="workflow-step">
        <div class="workflow-icon">📥</div>
        <h3>1. Input Text</h3>
        <p>User provides text or uploads a file.</p>
    </div>
    <div class="workflow-arrow">→</div>
    <div class="workflow-step">
        <div class="workflow-icon">🧹</div>
        <h3>2. Preprocess</h3>
        <p>Remove links, punctuation, @users, and stopwords.</p>
    </div>
    <div class="workflow-arrow">→</div>
    <div class="workflow-step">
        <div class="workflow-icon">🔡</div>
        <h3>3. Tokenize</h3>
        <p>Convert cleaned text into a sequence of numeric IDs.</p>
    </div>
    <div class="workflow-arrow">→</div>
    <div class="workflow-step">
        <div class="workflow-icon">📏</div>
        <h3>4. Padding</h3>
        <p>Pad or truncate all sequences to a length of {max_len}.</p>
    </div>
    <div class="workflow-arrow">→</div>
    <div class="workflow-step">
        <div class="workflow-icon">🧠</div>
        <h3>5. Predict</h3>
        <p>LSTM model analyzes the sequence and outputs a probability (0.0-1.0).</p>
    </div>
    <div class="workflow-arrow">→</div>
    <div class="workflow-step">
        <div class="workflow-icon">📊</div>
        <h3>6. Interpret</h3>
        <p>Convert the probability into 'Positive', 'Negative', or 'Neutral'.</p>
    </div>
</div>
"""

def render_workflow_tab():
    """
    Renders the 'Workflow' tab using custom HTML and CSS.
    Contains both workflow and use cases.
    """
    
    st.header("How Our Pipeline Works")
    st.write("From raw text to a final result, the process involves 6 key stages:")
    
    max_len = st.session_state.get('max_len', 30)
    
    st.markdown(WORKFLOW_HTML.format(max_len=max_len), unsafe_allow_html=True)
    
    render_footer()