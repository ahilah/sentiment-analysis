import streamlit as st
import time
from ui_tabs.footer import render_footer 

HERO_HTML = """
<div class="hero-section">
    <h1 class="hero-title">Welcome to Insight AI</h1>
    <p class="hero-subtitle">
        Understand your text in seconds.
        Powered by a Deep Learning model trained on 1.6 million tweets.
    </p>
</div>
"""

FEATURES_HTML = """
<div class="use-case-grid">
    <div class="card">
        <h3>Instant Analysis</h3>
        <p>
        Get immediate sentiment classification (Positive, Negative, or Neutral) 
        for any text you provide.
        </p>
    </div>
    <div class="card">
        <h3>Batch Processing</h3>
        <p>
        Need to analyze a large volume of feedback? Upload a .csv or .txt file 
        and get a full report in seconds.
        </p>
    </div>
    <div class="card">
        <h3>Nuanced Understanding</h3>
        <p>
        The model isn't just binary. It uses a "neutrality threshold" to 
        identify ambiguous text, avoiding false classifications.
        </p>
    </div>
</div>
"""

def display_result_metric(label, confidence):
    """
    Displays the custom HTML metric box for the result.
    """
    if label == "Positive":
        value_class = "metric-value-positive"
        confidence_text = f"{confidence:.2f} %"
    elif label == "Negative":
        value_class = "metric-value-negative"
        confidence_text = f"{confidence:.2f} %"
    else:
        value_class = "metric-value-neutral"
        confidence_text = f"Raw Score: {confidence:.3f}"

    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Sentiment</div>
        <div class="{value_class}">{label}</div>
        <div class="metric-confidence">{confidence_text}</div>
    </div>
    """, unsafe_allow_html=True)

def render_home_tab(predictor):
    """
    Renders the new, aesthetic 'Welcome' tab.
    'predictor' is passed in for the interactive demo.
    """
    
    # 1. Inject Hero Section HTML
    st.markdown(HERO_HTML, unsafe_allow_html=True)
    
    # 2. Inject Features Section HTML
    st.header("What Can Insight AI Do?")
    st.markdown(FEATURES_HTML, unsafe_allow_html=True)
    
    st.markdown("<br><br><hr><br>", unsafe_allow_html=True)
    
    # 3. Interactive Demo Section
    st.header("Try it Instantly")
    st.write("Click any example to see the live analysis:")

    if 'home_result' not in st.session_state:
        st.session_state.home_result = (None, None)

    examples = [
        "This movie was fantastic, I really loved it!",
        "The service was okay, not bad but not great either.",
        "I hated this product. It was a total waste of money."
    ]

    cols = st.columns(len(examples))
    
    for i, (col, example) in enumerate(zip(cols, examples)):
        with col:
            st.markdown("<div class='example-button-container'>", unsafe_allow_html=True)
            
            if st.button(example, key=f"ex{i}", use_container_width=True):
                with st.spinner("Analyzing..."):
                    label, confidence = predictor.predict_sentiment(example)
                    # Save the result to session state
                    st.session_state.home_result = (label, confidence)

            st.markdown("</div>", unsafe_allow_html=True)

    label, confidence = st.session_state.home_result

    # Add a check to ensure 'label' is not None before trying to display
    if label is not None: 
        st.markdown("<br>", unsafe_allow_html=True)
        display_result_metric(label, confidence)

    render_footer()