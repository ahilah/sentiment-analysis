import streamlit as st
import pandas as pd
import numpy as np
import json
from datetime import datetime
import pytz 
from ui_tabs.footer import render_footer

def render_classic_models_tab(predictor):
    """
    Renders the 'Classic Models' tab.
    'predictor' is an instance of SklearnPredictor.
    """
    st.header("Try the Classic ML Models")
 
    model_names = predictor.get_model_names()
    st.subheader("Choose a Model")
    st.markdown("Select one of the top-performing classic ML models to test.")

    model_choice = st.selectbox(
        "Select Model:",
        options=model_names,
        index=0 # Default to the first model (Logistic Regression)
    )
    st.info(f"You are currently using the **{model_choice}** model.")
    
    st.markdown("---")
    
    if 'classic_single_result' not in st.session_state:
        st.session_state.classic_single_result = None
    
    col1, col2 = st.columns([1, 1])

    # --- Column 1: Single Text Analysis ---
    with col1:
        st.subheader("Single Text Analysis")
        
        if 'classic_user_text' not in st.session_state:
            st.session_state.classic_user_text = "This is a wonderful product, I am very happy!"
        
        user_text = st.text_area(
            "Enter text to analyze:", 
            key='classic_user_text',
            height=150
        )
        
        if st.button("Analyze (Classic Model)", type="primary", use_container_width=True):
            if user_text:
                with st.spinner(f"Analyzing with {model_choice}..."):
                    label, confidence = predictor.predict_sentiment(user_text, model_choice)
                    st.session_state.classic_single_result = (user_text, label, confidence, model_choice)
            else:
                st.warning("Please enter text to analyze.")
                st.session_state.classic_single_result = None 
        
        # Display result
        if st.session_state.classic_single_result:
            user_text, label, confidence, used_model = st.session_state.classic_single_result
            
            st.write(f"**Result (from {used_model}):**")
            
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
            
            # Prepare JSON data
            lviv_tz = pytz.timezone('Europe/Kiev')
            time_now = datetime.now(lviv_tz)
            result_data = {
                "model_used": used_model,
                "text": user_text,
                "sentiment": label,
                "confidence_percent": f"{confidence:.2f}" if label != "Neutral" else "N/A",
                "analysis_timestamp_local": time_now.isoformat(),
                "timezone": time_now.tzname()
            }
            result_json = json.dumps(result_data, indent=4)
            
            st.download_button(
                label="Save Result",
                data=result_json,
                file_name=f"sentiment_result_{used_model.replace(' ', '_')}.json",
                mime="application/json",
                key="download_classic_json", 
                use_container_width=True
            )

    # --- Column 2: Batch File Analysis ---
    with col2:
        st.subheader("Batch File Analysis")
        
        uploaded_file = st.file_uploader(
            "Upload a .txt or .csv file", 
            type=['txt', 'csv'],
            key="classic_uploader" # Different key
        )
        
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                    if 'text' in df.columns: texts = df['text'].astype(str).tolist()
                    else: texts = df.iloc[:, 0].astype(str).tolist()
                elif uploaded_file.name.endswith('.txt'):
                    texts = [line.decode('utf-8').strip() for line in uploaded_file.readlines() if line.strip()]
                
                st.success(f"File '{uploaded_file.name}' uploaded. Found {len(texts)} rows.")
                
                results = []
                with st.spinner(f"Analyzing {len(texts)} rows with {model_choice}..."):
                    for text in texts:
                        label, score = predictor.predict_sentiment(text, model_choice)
                        
                        if label == "Positive": conf = f"{score:.2f} %"
                        elif label == "Negative": conf = f"{score:.2f} %"
                        else: conf = "N/A"
                        
                        results.append([text, label, conf])

                results_df = pd.DataFrame(results, columns=["Original Text", "Sentiment", "Confidence %"])
                st.dataframe(results_df, height=300)

                st.subheader(f"Distribution (Model: {model_choice})")
                sentiment_counts = results_df["Sentiment"].value_counts()
                st.bar_chart(sentiment_counts, color="#3B82F6")
                
                @st.cache_data
                def convert_df_classic(df):
                   return df.to_csv(index=False).encode('utf-8')

                csv = convert_df_classic(results_df)
                st.download_button(
                   label="Download Results",
                   data=csv,
                   file_name=f"batch_results_{model_choice.replace(' ', '_')}.csv",
                   mime='text/csv',
                   use_container_width=True
                )
            except Exception as e:
                st.error(f"Error processing file: {e}")
                
    render_footer()