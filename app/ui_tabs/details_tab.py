import streamlit as st
import os
from core.config import (
    TRAINING_PLOT_PATH, 
    CONFUSION_MATRIX_PATH,
    CM_LR_PATH,
    CM_SVC_PATH,
    CM_NB_PATH
)
from ui_tabs.footer import render_footer
from core.processor import TextProcessor

def render_details_tab(predictor):
    """
    Renders the 'How it Works' tab with model details,
    using a styled, card-based layout.
    """
    st.header("How it Works (The Details)")
    
    # --- Section 1: Preprocessing & NN Architecture ---
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("Interactive Preprocessing")
            st.write("The model doesn't see 'raw' text. It sees this:")
            example_text = st.text_input(
                "Enter text to see the processed version:", 
                "I LOVE @Health4UandPets u guys r the best!!",
                key="preprocess_example"
            )
            #processed_example = predictor.get_processed_text(example_text, stem=False)
            processor = TextProcessor()  # створюємо об’єкт
            processed_example = processor.preprocess(example_text, stem=False)
            st.code(f"Original: {example_text}\nCleaned:  {processed_example}", language="text")

    with col2:
        with st.container(border=True):
            st.subheader("Model Architecture (LSTM)")
            st.write("A hybrid Conv1D + LSTM model:")
            model_summary = """
Layer (type)       Output Shape     Param #   
================================================
input_1 (InputLayer)  [(None, 30)]     0         
embedding (Embedding) (None, 30, 300)  18842100  
(trainable=False)                               
... (layers) ...                                                      
dense_2 (Dense)       (None, 1)        513       
================================================
Total params: 19,333,429
Trainable params: 491,329
Non-trainable params: 18,842,100 (GloVe)
            """
            st.code(model_summary, language="text")
    
    st.markdown("<br>", unsafe_allow_html=True) # Add space
    
    # --- Section 2: NN Training History ---
    with st.container(border=True):
        st.subheader("Deep Learning (LSTM) Model Performance")
        st.write("The following charts show the LSTM model's performance during training.")
        
        img_col1, img_col2 = st.columns(2)
        
        with img_col1:
            if os.path.exists(CONFUSION_MATRIX_PATH):
                c1, c2, c3 = st.columns([1, 5, 1]) # 1 part margin, 5 parts image, 1 part margin
                with c2:
                    st.image(CONFUSION_MATRIX_PATH, caption="LSTM Model Confusion Matrix", use_container_width=True)
            else:
                st.warning(f"Image not found: 'confusion_matrix.png'")

        with img_col2:
            if os.path.exists(TRAINING_PLOT_PATH):
                c1, c2, c3 = st.columns([1, 5, 1])
                with c2:
                    st.image(TRAINING_PLOT_PATH, caption="Model Accuracy and Loss", use_container_width=True)
            else:
                st.warning(f"Image not found: 'image_8ccd42.png'")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- Section 3: Classic Model Comparison ---
    with st.container(border=True):
        st.subheader("Classic Model Comparison (TF-IDF)")
        st.write("This application also supports classic, non-neural network models. Here is a performance comparison of the top 3.")

        tab_lr, tab_svc, tab_nb = st.tabs([
            "1. Logistic Regression", 
            "2. Linear SVC", 
            "3. Multinomial Naive Bayes"
        ])

        # --- Logistic Regression Tab ---
        with tab_lr:
            st.markdown("#### Logistic Regression (Accuracy: ~79-80%)")
            st.write(
                "This model is the **best all-rounder**. It's very fast, balanced, and provides "
                "reliable probabilities. It's the recommended choice for general-purpose analysis."
            )
            if os.path.exists(CM_LR_PATH):
                c1, c2, c3 = st.columns([1, 3, 1]) # 1:3:1 ratio
                with c2:
                    st.image(CM_LR_PATH, caption="Logistic Regression Confusion Matrix", use_container_width=True)
            else:
                st.warning("Please add 'cm_logistic_regression.png' to your project's root folder.")

        # --- Linear SVC Tab ---
        with tab_svc:
            st.markdown("#### Linear SVC (Accuracy: ~77-79%)")
            st.write(
                "A powerful model that works by finding the 'best line' to separate the classes. "
                "It's very effective but doesn't provide probability scores, only a hard classification."
            )
            if os.path.exists(CM_SVC_PATH):
                c1, c2, c3 = st.columns([1, 3, 1])
                with c2:
                    st.image(CM_SVC_PATH, caption="Linear SVC Confusion Matrix", use_container_width=True)
            else:
                st.warning("Please add 'cm_linear_svc.png' to your project's root folder.")
        
        # --- Multinomial Naive Bayes Tab ---
        with tab_nb:
            st.markdown("#### Multinomial Naive Bayes (Accuracy: ~77%)")
            st.write(
                "A classic algorithm designed specifically for text classification. "
                "It's extremely fast and works surprisingly well, though it's often slightly "
                "less accurate than Logistic Regression."
            )
            if os.path.exists(CM_NB_PATH):
                c1, c2, c3 = st.columns([1, 3, 1])
                with c2:
                    st.image(CM_NB_PATH, caption="Multinomial Naive Bayes Confusion Matrix", use_container_width=True)
            else:
                st.warning("Please add 'cm_multinomial_nb.png' to your project's root folder.")
    
    render_footer()