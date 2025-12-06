import streamlit as st
import pandas as pd
import numpy as np
import json
from datetime import datetime
import pytz 
from ui_tabs.footer import render_footer

def render_demo_tab(predictor):
    """
    Renders the 'Demo' tab for single and batch predictions.
    'predictor' is an instance of SentimentPredictor.
    """
    st.header("Try the Product Live")
    st.markdown("You can analyze a single sentence or upload a file for batch analysis.")
    
    if 'single_result' not in st.session_state:
        st.session_state.single_result = None
    
    col1, col2 = st.columns([1, 1])

    # --- Column 1: Single Text Analysis ---
    with col1:
        st.subheader("Single Text Analysis")
        
        if 'user_text' not in st.session_state:
            st.session_state.user_text = "This movie was fantastic, I really loved it!"
        
        user_text = st.text_area(
            "Enter text to analyze:", 
            key='user_text',
            height=150
        )
        
        if st.button("Analyze", type="primary", use_container_width=True):
            if user_text:
                with st.spinner("Analyzing..."):
                    label, confidence = predictor.predict_sentiment(user_text)
                    st.session_state.single_result = (user_text, label, confidence)
            else:
                st.warning("Please enter text to analyze.")
                st.session_state.single_result = None 
        
        # Display result
        if st.session_state.single_result:
            user_text, label, confidence = st.session_state.single_result
            
            st.write("**Result:**")
            
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
            
            # --- Prepare JSON data (FIXED TYPE ERROR) ---
            lviv_tz = pytz.timezone('Europe/Kiev')
            time_now = datetime.now(lviv_tz)

            # Calculate values and ensure they are standard Python floats
            if label == "Neutral":
                score_val = float(confidence) # Convert to python float
                conf_percent_str = "N/A"
            elif label == "Positive":
                score_val = float(confidence / 100) # Convert to python float
                conf_percent_str = f"{confidence:.2f}"
            else: # Negative
                score_val = float(1 - (confidence / 100)) # Convert to python float
                conf_percent_str = f"{confidence:.2f}"

            result_data = {
                "text": user_text,
                "sentiment": label,
                "score_raw": score_val, 
                "confidence_percent": conf_percent_str,
                "analysis_timestamp_local": time_now.isoformat(),
                "timezone": time_now.tzname()
            }
            
            # Now json.dumps will work because score_val is a float, not float32
            result_json = json.dumps(result_data, indent=4)
            
            st.download_button(
                label="Save Result (.json)",
                data=result_json,
                file_name=f"sentiment_result_{time_now.strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                key="download_single_json", 
                use_container_width=True
            )

    # --- Column 2: Batch File Analysis ---
    with col2:
        st.subheader("Batch File Analysis")
        
        uploaded_file = st.file_uploader(
            "Upload a .txt or .csv file", 
            type=['txt', 'csv']
        )
        
        if uploaded_file is not None:
            try:
                # Read file
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                    if 'text' in df.columns:
                        texts = df['text'].astype(str).tolist()
                    elif 'TweetText' in df.columns:
                         texts = df['TweetText'].astype(str).tolist()
                    else:
                        texts = df.iloc[:, 0].astype(str).tolist()
                elif uploaded_file.name.endswith('.txt'):
                    texts = [line.decode('utf-8').strip() for line in uploaded_file.readlines() if line.strip()]
                
                st.success(f"File '{uploaded_file.name}' uploaded. Found {len(texts)} rows.")
                
                # Process texts
                results = []
                with st.spinner(f"Analyzing {len(texts)} rows..."):
                    for text in texts:
                        label, score = predictor.predict_sentiment(text)
                        
                        if label == "Positive":
                            conf = f"{score:.2f} %"
                        elif label == "Negative":
                            conf = f"{score:.2f} %"
                        else:
                            conf = "N/A" # No confidence for neutral
                        
                        results.append([text, label, conf])

                results_df = pd.DataFrame(results, columns=["Original Text", "Sentiment", "Confidence %"])
                st.dataframe(results_df, height=300)

                st.subheader("Sentiment Distribution in File")
                sentiment_counts = results_df["Sentiment"].value_counts()
                st.bar_chart(sentiment_counts, color="#3B82F6") # Apply blue color
                
                @st.cache_data
                def convert_df(df):
                   return df.to_csv(index=False).encode('utf-8')

                csv = convert_df(results_df)
                st.download_button(
                   label="Download Results (.csv)",
                   data=csv,
                   file_name='sentiment_analysis_results.csv',
                   mime='text/csv',
                   use_container_width=True
                )

            except Exception as e:
                st.error(f"Error processing file: {e}")
                
    render_footer()