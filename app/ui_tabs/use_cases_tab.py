import streamlit as st
import os

USE_CASES_HTML = """
<div class="use-case-grid">
    <div class="card">
        <h3>Brand Monitoring</h3>
        <p>
        Companies track mentions of their brand on social media 
        to instantly react to negative feedback and measure 
        public perception of their products or ad campaigns.
        </p>
    </div>
    <div class="card">
        <h3>Product Review Analysis</h3>
        <p>
        E-commerce platforms analyze thousands of reviews
        to automatically identify product strengths, weaknesses,
        and detect fraudulent or spam reviews.
        </p>
    </div>
    <div class="card">
        <h3>Customer Support</h3>
        <p>
        Helpdesk systems can automatically analyze incoming support tickets. 
        A highly negative ticket can be immediately escalated 
        to a senior manager for resolution.
        </p>
    </div>
    <div class="card">
        <h3>Market Research</h3>
        <p>
        Instead of running expensive focus groups, companies
        can analyze public discussions to understand
        what customers think about new features, services, or trends.
        </p>
    </div>
    <div class="card">
        <h3>Political Analysis</h3>
        <p>
        Sentiment analysis of Twitter (X) and Facebook
        is used to measure public opinion towards
        politicians, new laws, or social movements.
        </p>
    </div>
    <div class="card">
        <h3>Content Moderation</h3>
        <p>
        Social networks and forums use sentiment analysis
        to automatically detect toxic comments,
        cyberbullying, or hate speech.
        </p>
    </div>
</div>
"""

def render_use_cases_tab():
    """
    Renders the 'Use Cases' tab using custom HTML and CSS.
    Contains both workflow and use cases.
    """

    st.header("Where Can You Use Sentiment Analysis?")
    st.write("This technology has wide applications in business, marketing, and social research.")
    
    st.markdown(USE_CASES_HTML, unsafe_allow_html=True)