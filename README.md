

# Insight AI - Sentiment Analysis

**Insight AI** is a Streamlit web application for analyzing text sentiment (**Positive**, **Negative**, or **Neutral**) using a deep learning model (Bidirectional LSTM) trained on the 1.6 million tweet [Sentiment140 dataset](https://www.tensorflow.org/datasets/catalog/sentiment140).

This repository contains the application source code. *The model files and datasets are hosted externally due to their large size.*

Key Features
- Real-time Analysis: Instant sentiment classification with confidence scores.
- Batch Processing: Support for uploading .csv or .txt files for bulk analysis.
- Smart Thresholding: Custom logic to identify "Neutral" sentiment based on model confidence.
- Model Comparison: Switch between Deep Learning and Classic ML models on the fly.
- Interactive Visualizations: Training history, confusion matrices, and data distribution charts.

---

## How to Run this Project

To run this application on your local machine, please follow these steps.

### 1. Initial Setup

First, clone this repository to your computer:

```bash
git clone https://github.com/ahilah/sentiment-analysis.git
cd sentiment-analysis
```

Next, create a virtual environment and install the required Python packages:

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
source venv/bin/activate 

# On Windows use
venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

### 2\. Download Required Files 

This project requires large model and component files that are not included in this Git repository. **You must download them manually.**

| File                        | Target Folder      | Purpose                                  | Download Link |
|-----------------------------|---------------------|-------------------------------------------|---------------|
| best_model_initial.keras    | model/nn/           | The trained Keras (LSTM) model            | [Download](https://drive.google.com/file/d/1L6IYhbWj48c0itEHVZPlIEF1s9xeU82F/view?usp=sharing)|
| keras_tokenizer.pkl         | model/component/    | Tokenizer for NN model                    | [Download](https://drive.google.com/file/d/1L1H0jRGRjFlaQXu8lZxhcqZ43D9eIrfY/view?usp=sharing)|
| label_encoder.pkl           | model/component/    | Label Encoder for target variable         | [Download](https://drive.google.com/file/d/1yy4Haf7rmZ8vz6Hkl7Q6UIne7PqI4grr/view?usp=sharing)|
| tfidf_vectorizer_ngrams.pkl | model/component/    | TF-IDF Vectorizer for Sklearn models      | [Download](https://drive.google.com/file/d/17K50xR6W3H7K0DSW4pUmGBSKZOHvf7iY/view?usp=sharing)|
| LR_ngrams.pkl               | model/sklearn/      | Logistic Regression model                 | [Download](https://drive.google.com/file/d/1l6rcDASgYWdYHtJhGPk74F75UrwwacWN/view?usp=sharing)|
| SVC_ngrams.pkl              | model/sklearn/      | Linear SVC model                          | [Download](https://drive.google.com/file/d/1hcRVilHiiNstqBoQk8c7ceiGBQbUoj6b/view?usp=sharing)|
| MNB_ngrams.pkl              | model/sklearn/      | Multinomial Naive Bayes model             | [Download](https://drive.google.com/file/d/1Q3iqERSFIOs3z3pOgVLAfLtT8KCQlbEu/view?usp=sharing)|


### 3\. Run the App

Once all files are in place, run the Streamlit application from your terminal (from the project's root folder):

```bash
streamlit run app.py
```

The application should automatically open in your web browser.

-----

## Project Structure

```text
├── .streamlit/
│   └── config.toml         # App theme configuration
├── app/
│   ├── assets/             # CSS, fonts, and icons (favicon.png)
│   ├── core/               # Backend logic (predictor.py, config.py)
│   └── ui_tabs/            # Python files for each Streamlit tab (Home, Demo, etc.)
├── model/
│   ├── component/          # (Place .pkl tokenizers/encoders here)
│   ├── nn/                 # (Place .keras model here)
│   └── sklearn/            # (Place .pkl ML models here)
├── .gitignore
├── app.py                  # Main Streamlit entry point
├── README.md               # This file
└── requirements.txt        # List of dependencies
```


## Model Performance

Comparison of the Deep Learning model and the best-performing classic ML models on the test dataset.

| Model | Accuracy | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| **Bi-LSTM (Neural Network)** | **79.1%** | 0.79 | 0.79 | 0.79 |
| **Logistic Regression** | **79.0%** | 0.79 | 0.79 | 0.79 |
| **Linear SVC** | **78.0%** | 0.78 | 0.78 | 0.78 |
| **Multinomial Naive Bayes** | **77.0%** | 0.77 | 0.77 | 0.77 |

> **Note:** While Logistic Regression shows similar accuracy, the **Bi-LSTM** model demonstrates superior performance on complex sentences involving sarcasm and negation due to its context-aware architecture.

---

## Tech Stack & Environment

This project was developed using the following technologies:

| Category | Technology | Version Used |
| :--- | :--- | :--- |
| **Language** | Python | `3.10.x` |
| **Web Framework** | Streamlit | `1.32.0` |
| **Deep Learning** | TensorFlow / Keras | `2.15.0` |
| **Machine Learning** | Scikit-learn | `1.4.0` |
| **NLP Library** | NLTK | `3.8.1` |
| **Data Manipulation** | Pandas | `2.2.0` |
| **Visualization** | Matplotlib / Seaborn | `3.8.0` |
