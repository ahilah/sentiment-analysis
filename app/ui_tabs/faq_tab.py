import streamlit as st
from ui_tabs.footer import render_footer

def render_faq_tab():
    """
    Renders the 'FAQ' tab with relevant questions for the project.
    """
    st.header("Frequently Asked Questions (FAQ)")

    with st.expander("What model is powering this application?"):
        st.markdown("""
        This app uses two types of models, which you can select from the tabs:
        
        1.  **NN Model (Default):** A custom-built hybrid Deep Learning model (LSTM + Conv1D) that understands text context and sequence.
        2.  **Classic Models:** A selection of traditional machine learning models (like Logistic Regression) that are extremely fast and analyze word statistics (TF-IDF).
        
        You can see the full architecture for the NN Model in the **"How it Works"** tab.
        """)

    with st.expander("Why did my text get a 'Neutral' sentiment?"):
        st.markdown("""
        The core models were trained only on "Positive" and "Negative" data. However, forcing every text into one of these two boxes is inaccurate for ambiguous text (like "The service was okay").
        
        We introduced a "neutrality zone" as a post-processing step.
        * If the model's confidence is **high** (e.g., > 75% Positive or > 75% Negative), we show that label.
        * If the model is **uncertain** (the score is between 0.25 and 0.75), we label it **"Neutral"** to avoid a wrong classification.
        """)

    with st.expander("How accurate are these models?"):
        st.markdown("""
        * The **NN Model (LSTM)** achieved approximately **79.1% accuracy** on the validation test set.
        * The **Classic Models (TF-IDF)** achieved similar results, with the best model (Logistic Regression) reaching ~79-80% accuracy after tuning and adding n-grams.
        
        While 100% is impossible (even humans disagree on sentiment), this accuracy is strong because the model was trained on **social media data (tweets)**, which is very "noisy" (slang, typos, sarcasm).
        
        You can see the Confusion Matrices for all models in the **"How it Works"** tab.
        """)
        
    with st.expander("What's the difference between the NN and Classic models?"):
        st.markdown("""
        They use fundamentally different approaches to "understand" text:

        * **NN Model (LSTM):**
            * **How it works:** Reads text like a human, word-by-word, and understands the *sequence* and *context*. It learns that "not good" is negative, even though "good" is positive.
            * **Input:** Word Embeddings (GloVe) - vectors that understand word meanings.
            * **Pros:** Higher potential for accuracy, understands context.
            * **Cons:** Much slower, requires more computational power (GPU).

        * **Classic Models (Logistic Regression, etc.):**
            * **How it works:** Uses a "Bag of Words" approach. It doesn't know the order of words, only *which* words (and word pairs) appear and how *important* they are (using TF-IDF).
            * **Input:** TF-IDF Matrix (a giant spreadsheet of word importance scores).
            * **Pros:** Extremely fast to train and predict (milliseconds).
            * **Cons:** "Dumber" — it has no deep understanding of context or sarcasm.
        """)

    with st.expander("Which model should I use?"):
        st.markdown("""
        **It depends on your goal:**

        * **Use the NN Model (LSTM)** for the **highest possible accuracy**. If you need the best guess at what a user *really* meant, the NN's ability to understand context is superior.
        
        * **Use the Classic Models (Logistic Regression)** for **speed and high throughput**. If you needed to analyze 1 million comments *right now*, Logistic Regression would finish the job in a fraction of the time of the NN model, while still providing a very high-quality result (~79-80% accurate).
        """)
        
    with st.expander("Can I analyze text in other languages (e.g., Ukrainian)?"):
        st.markdown("""
        **No, not at this time.** All models were trained *exclusively* on English text and use English "stopwords" (like 'the', 'is', 'a'). 
        
        They will provide highly inaccurate results for any other language. To analyze Ukrainian text, new models would need to be trained from scratch on a large, labeled Ukrainian dataset.
        """)

    with st.expander("How do I analyze a file?"):
        st.markdown("""
        1.  Navigate to either **"Try the NN Model"** or **"Try Classic Models"**.
        2.  Go to the **"Batch File Analysis"** column on the right.
        3.  Click the "Browse files" button or drag-and-drop your file.
        4.  The app accepts **.txt** (one sentence per line) or **.csv** (must have a column named 'text').
        5.  The results will appear in a table, along with a bar chart showing the sentiment distribution.
        """)

    with st.expander("What's the difference between 'Workflow', 'Use Cases', and 'How it Works'?"):
        st.markdown("""
        * **"Workflow"** shows the *high-level business process* (the 6 steps from input to output).
        * **"Use Cases"** shows *where* this technology can be applied in the real world.
        * **"How it Works"** shows the *technical details* (model architecture, preprocessing, and performance metrics) for a developer or examiner.
        """)

    render_footer()