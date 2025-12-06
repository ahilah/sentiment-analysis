import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from core.config import POSITIVE_THRESHOLD, NEGATIVE_THRESHOLD, LABEL_ENCODER_PATH

class TextProcessor:
    """
    Handles all text pre-processing and prediction post-processing.
    """
    def __init__(self):
        print("Initializing TextProcessor...")
        try:
            self.stop_words = set(stopwords.words('english'))
            with open(LABEL_ENCODER_PATH, 'rb') as f:
                self.encoder = pickle.load(f)
            print("✓ Label Encoder loaded.")
        except LookupError:
            print("Downloading 'stopwords' corpus...")
            nltk.download('stopwords')
            self.stop_words = set(stopwords.words('english'))
        
        self.stemmer = SnowballStemmer('english')
        self.text_cleaning_re = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
        self.positive_threshold = POSITIVE_THRESHOLD
        self.negative_threshold = NEGATIVE_THRESHOLD
        print("✓ TextProcessor initialized.")

    def preprocess(self, text, stem=False):
        text = re.sub(self.text_cleaning_re, ' ', str(text).lower()).strip()
        tokens = []
        for token in text.split():
            if token not in self.stop_words:
                if stem:
                    tokens.append(self.stemmer.stem(token))
                else:
                    tokens.append(token)
        return " ".join(tokens)

    def postprocess(self, prediction_prob):
        if prediction_prob > self.positive_threshold:
            label = "Positive"
            confidence = prediction_prob * 100
        elif prediction_prob < self.negative_threshold:
            label = "Negative"
            confidence = (1.0 - prediction_prob) * 100
        else:
            label = "Neutral"
            confidence = prediction_prob
        return label, confidence