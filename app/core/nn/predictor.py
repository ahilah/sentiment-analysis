import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from core.config import NN_MODEL_PATH, TOKENIZER_PATH, MAX_SEQUENCE_LENGTH
from core.processor import TextProcessor

class SentimentPredictor:
    """
    A class to load the ML model and orchestrate the prediction.
    It USES TextProcessor for text handling.
    """
    def __init__(self):
        print("Initializing SentimentPredictor...")
        try:
            self.model = load_model(NN_MODEL_PATH)
            with open(TOKENIZER_PATH, 'rb') as f:
                self.tokenizer = pickle.load(f)
        except FileNotFoundError as e:
            print(f"ERROR: Model or tokenizer file not found.")
            print(f"Please check paths:\nModel: {NN_MODEL_PATH}\nTokenizer: {TOKENIZER_PATH}")
            raise e
            
        self.processor = TextProcessor()
        print("✓ SentimentPredictor initialized successfully.")

    def get_processed_text(self, text, stem=False):
        return self.processor.preprocess(text, stem=stem)

    def predict_sentiment(self, text):
        processed_text = self.processor.preprocess(text, stem=False)
        sequence = self.tokenizer.texts_to_sequences([processed_text])
        padded_sequence = pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH)
        prediction_prob = self.model.predict(padded_sequence, verbose=0)[0][0]
        label, confidence = self.processor.postprocess(prediction_prob)
        return label, confidence
    
    def get_max_len(self):
        return MAX_SEQUENCE_LENGTH