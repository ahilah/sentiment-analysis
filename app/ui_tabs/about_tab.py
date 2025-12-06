import streamlit as st
from ui_tabs.footer import render_footer

def render_about_tab():
    """
    Renders the 'About' tab with project and author info
    in a professional, card-based layout.
    """
    st.header("About This Project")

    # --- 2. "Project Motivation" Section ---
    st.subheader("Project Motivation")
    
    with st.container(border=True):
        st.markdown(
        """
        In an era dominated by social media and online reviews, understanding public 
        opinion at scale is crucial for businesses, researchers, and individuals. 
        Manual analysis is impossible due to the sheer volume of text data.
        
        This project's goal was to build and deploy a reliable tool that can:
        * **Analyze sentiment** from raw text instantly.
        * **Handle uncertainty** by identifying 'Neutral' text, not just 'Positive' or 'Negative'.
        * **Process large files** to allow for bulk analysis.
        * **Serve as a prototype** for a real-world sentiment analysis service.
        """
        )

    st.markdown("<br>", unsafe_allow_html=True) # Add space

    # --- 3. "Technology Stack" Section ---
    st.subheader("Technology Stack")
    st.write("This application was built using a modern data science & web stack:")

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        with st.container(border=True):
            st.markdown("### Python & Streamlit")
            st.write(
                "The core application logic is written in Python. "
                "**Streamlit** was used to build and serve this interactive "
                "web application without needing to write complex HTML/CSS/JS."
            )
            
    with col2:
        with st.container(border=True):
            st.markdown("### TensorFlow and Keras")
            st.write(
                "**TensorFlow** is the deep learning framework used to design, "
                "train, and save the core Bidirectional LSTM model "
                "that powers the sentiment predictions."
            )
            
    with col3:
        with st.container(border=True):
            st.markdown("### Pandas & NLTK")
            st.write(
                "**Pandas** was essential for loading and processing the initial 1.6 million tweets. "
                "**NLTK** provided the tools for text preprocessing, such as "
                "removing stopwords."
            )

    with col4:
        with st.container(border=True):
            st.markdown("### Scikit-learn")
            st.write(
                "Used for the classic ML pipeline. **TfidfVectorizer** (with n-grams) "
                "builds the feature matrix, and models like **Logistic Regression** & **LinearSVC** "
                "provide fast, alternative predictions."
            )

    render_footer()