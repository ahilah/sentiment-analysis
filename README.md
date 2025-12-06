

# Insight AI - Sentiment Analysis

**Insight AI** is a Streamlit web application for analyzing text sentiment (**Positive**, **Negative**, or **Neutral**) using a deep learning model (Bidirectional LSTM) trained on the 1.6 million tweet Sentiment140 dataset.

This repository contains the application source code. *The model files and datasets are hosted externally due to their large size.*

---

## How to Run this Project

To run this application on your local machine, please follow these steps.

### 1. Initial Setup

First, clone this repository to your computer:

```bash
git clone [your-github-repo-link]
cd [your-project-folder-name]
```

Next, create a virtual environment and install the required Python packages:

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
source venv/bin/activate 

# On Windows use:
venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

### 2\. (IMPORTANT) Download Required Files 

This project requires large model and component files that are not included in this Git repository. **You must download them manually.**

| File | Purpose | Download Link |
| :--- | :--- | :--- |
| `best_model_fine_tuned.keras` | The trained Keras (LSTM) model | [] |
| `keras_tokenizer.pkl` | The Keras Tokenizer | [] |
| `label_encoder.pkl` | The SKlearn Label Encoder | [] |

#### Where to place the files:

Once downloaded, you must place the files in the **correct folders** before running the app:

  * Move **`best_model_fine_tuned.keras`** into: `model/nn/`
  * Move **`keras_tokenizer.pkl`** and **`label_encoder.pkl`** into: `model/component/`

### 3\. Run the App

Once all files are in place, run the Streamlit application from your terminal (from the project's root folder):

```bash
streamlit run app/app.py
```

The application should automatically open in your web browser.

-----

## Project Structure

```text
├── .streamlit/
│   └── config.toml     # App theme configuration
├── app/
│   ├── assets/         # CSS, fonts, and icons (favicon.png)
│   ├── core/           # Backend logic (predictor.py, processor.py)
│   ├── ui_tabs/        # Python files for each Streamlit tab
│   └── app.py          # Main Streamlit application file
├── model/
│   ├── component/      # (Place .pkl files here)
│   └── nn/             # (Place .keras model here)
├── .gitignore
├── README.md           # This file
└── requirements.txt
```

```
```