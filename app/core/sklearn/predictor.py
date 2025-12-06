import pickle
import re
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# Import configuration
from core.config import (
    TFIDF_VECTORIZER_PATH, 
    LR_MODEL_PATH, 
    SVC_MODEL_PATH, 
    NB_MODEL_PATH,
    POSITIVE_THRESHOLD,
    NEGATIVE_THRESHOLD,
    LABEL_ENCODER_PATH
)

class SklearnProcessor:
    """
    Handles text pre-processing (for Sklearn) and prediction post-processing.
    """
    def __init__(self):
        print("Initializing SklearnProcessor...")
        try:
            self.stop_words = set(stopwords.words('english'))
        except LookupError:
            import nltk
            print("Downloading 'stopwords' corpus...")
            nltk.download('stopwords')
            self.stop_words = set(stopwords.words('english'))
        
        self.stemmer = SnowballStemmer('english')
        # This regex is from your notebook
        self.text_cleaning_re = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
        print("✓ SklearnProcessor initialized.")

    def preprocess(self, text, stem=True):
        """
        Cleans and processes a single text string for Sklearn.
        Based on your notebook, this includes stemming (stem=True).
        """
        text = re.sub(self.text_cleaning_re, ' ', str(text).lower()).strip()
        tokens = []
        for token in text.split():
            if token not in self.stop_words:
                # Stemming is enabled
                token = self.stemmer.stem(token)
                
                # Remove short words (from your other notebook)
                if len(token) > 3:
                    tokens.append(token)
                    
        return " ".join(tokens)

    def postprocess(self, model, vectorized_text):
        """
        Converts a model's prediction into a human-readable label and confidence.
        """
        # Check if the model supports probability (LR, NB)
        if hasattr(model, "predict_proba"):
            # Get probability of the "Positive" class (class 1)
            prediction_prob = model.predict_proba(vectorized_text)[0][1]
            
            if prediction_prob > POSITIVE_THRESHOLD:
                label = "Positive"
                confidence = prediction_prob * 100
            elif prediction_prob < NEGATIVE_THRESHOLD:
                label = "Negative"
                confidence = (1.0 - prediction_prob) * 100
            else:
                label = "Neutral"
                confidence = prediction_prob # Raw score
        
        else:
            # For models like LinearSVC that don't have predict_proba
            prediction = model.predict(vectorized_text)[0]
            label = "Positive" if prediction == 1 else "Negative"
            confidence = 100.0 # It's a hard classification, so we show 100%
            
        return label, confidence

class SklearnPredictor:
    """
    Loads all Sklearn models and the TF-IDF vectorizer.
    Orchestrates the entire prediction pipeline for these models.
    """
    def __init__(self):
        print("Initializing SklearnPredictor...")
        try:
            # 1. Load the Processor
            self.processor = SklearnProcessor()
            
            # 2. Load the TF-IDF Vectorizer
            with open(TFIDF_VECTORIZER_PATH, 'rb') as f:
                self.vectorizer = pickle.load(f)
            
            # 3. Load all 3 models
            self.models = {}
            with open(LR_MODEL_PATH, 'rb') as f:
                self.models["Logistic Regression"] = pickle.load(f)
            with open(SVC_MODEL_PATH, 'rb') as f:
                self.models["Linear SVC"] = pickle.load(f)
            with open(NB_MODEL_PATH, 'rb') as f:
                self.models["Multinomial Naive Bayes"] = pickle.load(f)

        except FileNotFoundError as e:
            print(f"ERROR: A Sklearn model or vectorizer file not found.")
            print(f"Please check paths in config.py")
            raise e
        
        print(f"✓ SklearnPredictor initialized with {len(self.models)} models.")

    def get_model_names(self):
        """Returns a list of the loaded model names."""
        return list(self.models.keys())

    def get_processed_text(self, text):
        """Public wrapper for the UI to show preprocessing."""
        return self.processor.preprocess(text)

    def predict_sentiment(self, text, model_name):
        """
        Predicts the sentiment of a single text using the specified model.
        """
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' is not loaded.")
        
        # 1. Get the chosen model
        model = self.models[model_name]
        
        # 2. Pre-process the text (Sklearn-specific)
        processed_text = self.processor.preprocess(text)
        
        # 3. Vectorize the text
        vectorized_text = self.vectorizer.transform([processed_text])
        
        # 4. Post-process the prediction
        label, confidence = self.processor.postprocess(model, vectorized_text)
            
        return label, confidence