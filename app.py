import streamlit as st
import sys
import os

# Отримуємо шлях до папки, де лежить цей скрипт (app.py)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Додаємо шлях до папки 'app', бо саме в ній лежить 'core'
sys.path.append(os.path.join(base_dir, 'app'))

# Add the 'app' directory to the system path
APP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(APP_DIR)

# Import core components
from core.config import BASE_DIR
from core.nn.predictor import SentimentPredictor as KerasPredictor # Renamed for clarity
from core.utils import load_css

# --- Import Sklearn Predictor ---
from core.sklearn.predictor import SklearnPredictor

# Import render functions for each tab
from ui_tabs.home_tab import render_home_tab
from ui_tabs.demo_tab import render_demo_tab

# --- Import Classic Models Tab ---
from ui_tabs.classic_models_tab import render_classic_models_tab
from ui_tabs.workflow_tab import render_workflow_tab
from ui_tabs.use_cases_tab import render_use_cases_tab
from ui_tabs.details_tab import render_details_tab
from ui_tabs.about_tab import render_about_tab
from ui_tabs.faq_tab import render_faq_tab

# --- Define paths for assets ---
ASSETS_DIR = os.path.join(BASE_DIR, 'app', 'assets') 

CSS_PATH = os.path.join(ASSETS_DIR, 'styles.css')
ICON_PATH = os.path.join(ASSETS_DIR, 'image', 'favicon.png')

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Insight AI Sentiment Analysis", 
    page_icon=ICON_PATH,                         
    layout="wide"
)

# --- 2. Load CSS ---
load_css(CSS_PATH)
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">', unsafe_allow_html=True)


# --- 3. Load Models ---
@st.cache_resource
def load_keras_predictor():
    """Loads the Keras LSTM model"""
    try:
        predictor = KerasPredictor()
        return predictor
    except Exception as e:
        st.error(f"Error loading Keras model: {e}")
        return None

@st.cache_resource
def load_sklearn_predictor():
    """Loads all Sklearn models"""
    try:
        predictor = SklearnPredictor()
        return predictor
    except Exception as e:
        st.error(f"Error loading Sklearn models: {e}")
        return None

keras_predictor = load_keras_predictor()
sklearn_predictor = load_sklearn_predictor()

if keras_predictor is None or sklearn_predictor is None:
    st.error("Fatal Error: A predictor failed to load. App cannot start.")
    st.stop()

# --- 4. Save max_len to session state ---
st.session_state.max_len = keras_predictor.get_max_len() # From Keras predictor

# --- 5. Create Tabs (UPDATED) ---
tab_home, tab_demo_nn, tab_demo_classic, tab_workflow, tab_use_cases, tab_details, tab_faq, tab_about = st.tabs([
    "Welcome",
    "Try the NN Model",  # <-- Renamed
    "Try Classic Models", # <-- (NEW TAB)
    "Workflow",
    "Use Cases",
    "How it Works",
    "FAQ",
    "About"
])

# --- 6. Render Tabs ---
with tab_home:
    render_home_tab(keras_predictor) # Home tab uses the main NN model

with tab_demo_nn:
    render_demo_tab(keras_predictor)

# --- (NEW) Render the classic models tab ---
with tab_demo_classic:
    render_classic_models_tab(sklearn_predictor) # Pass the sklearn predictor

with tab_workflow:
    render_workflow_tab()
    
with tab_use_cases:
    render_use_cases_tab()

with tab_details:
    render_details_tab(keras_predictor)

with tab_faq:
    render_faq_tab()

with tab_about:
    render_about_tab()