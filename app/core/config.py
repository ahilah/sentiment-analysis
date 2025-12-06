import os

# --- Path Configuration ---

# 1. Визначаємо, де ми зараз (всередині app/core/)
CORE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Піднімаємось на рівень вище -> папка 'app'
APP_DIR = os.path.dirname(CORE_DIR)

# 3. Піднімаємось ще вище -> Корінь проєкту (де лежить app.py)
BASE_DIR = os.path.dirname(APP_DIR)

ASSETS_DIR = os.path.join(BASE_DIR, 'app', 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'image')

#all paths relative to the main project directory
MODEL_DIR = os.path.join(BASE_DIR, 'model')
NN_MODEL_PATH = os.path.join(MODEL_DIR, 'nn', 'best_model_initial.keras')
TOKENIZER_PATH = os.path.join(MODEL_DIR, 'component', 'keras_tokenizer.pkl')

# Path for the training graph image
#TRAINING_PLOT_PATH = 'C:\\Users\\rurik\\Downloads\\нулп\\programming\\innovative-information-technologies\\app\\assets\\image\\accuracy_loss_nn.png'
#CONFUSION_MATRIX_PATH = 'C:\\Users\\rurik\\Downloads\\нулп\\programming\\innovative-information-technologies\\app\\assets\\image\\confusion_matrix_nn.png'

TRAINING_PLOT_PATH = os.path.join(IMAGES_DIR, 'accuracy_loss_nn.png')
CONFUSION_MATRIX_PATH = os.path.join(IMAGES_DIR, 'confusion_matrix_nn.png')

# --- Model & Prediction Configuration ---
MAX_SEQUENCE_LENGTH = 30
POSITIVE_THRESHOLD = 0.75  # Score > 0.75 = Positive
NEGATIVE_THRESHOLD = 0.25  # Score < 0.25 = Negative

# --- Sklearn Model & Vectorizer Paths ---
SKLEARN_MODEL_DIR = os.path.join(MODEL_DIR, 'sklearn')
COMPONENT_DIR = os.path.join(MODEL_DIR, 'component')
LABEL_ENCODER_PATH = os.path.join(COMPONENT_DIR, 'label_encoder.pkl')

# Vectorizer trained with (1, 2) n-grams
TFIDF_VECTORIZER_PATH = os.path.join(COMPONENT_DIR, 'tfidf_vectorizer_ngrams.pkl') 

LR_MODEL_PATH = os.path.join(SKLEARN_MODEL_DIR, 'LR_ngrams.pkl')
SVC_MODEL_PATH = os.path.join(SKLEARN_MODEL_DIR, 'SVC_ngrams.pkl')
NB_MODEL_PATH = os.path.join(SKLEARN_MODEL_DIR, 'MNB_ngrams.pkl')

# --- Paths for Sklearn Confusion Matrices ---
#CM_LR_PATH = 'C:\\Users\\rurik\\Downloads\\нулп\\programming\\innovative-information-technologies\\app\\assets\\image\\confusion_matrix_lr.png'
#CM_SVC_PATH = 'C:\\Users\\rurik\\Downloads\\нулп\\programming\\innovative-information-technologies\\app\\assets\\image\\confusion_matrix_svc.png'
#CM_NB_PATH = 'C:\\Users\\rurik\\Downloads\\нулп\\programming\\innovative-information-technologies\\app\\assets\\image\\confusion_matrix_mnb.png'

CM_LR_PATH = os.path.join(IMAGES_DIR, 'confusion_matrix_lr.png')
CM_SVC_PATH = os.path.join(IMAGES_DIR, 'confusion_matrix_svc.png')
CM_NB_PATH = os.path.join(IMAGES_DIR, 'confusion_matrix_mnb.png')