import pickle
import re 
from pathlib import Path
from fastapi import HTTPException
import os

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent
model = None
model_path = f"{BASE_DIR}/trained_pipeline={__version__}.pkl"

try:
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None

classes = [
    'Arabic', 
    'Danish', 
    'Dutch', 
    'English', 
    'French', 
    'German', 
    'Greek', 
    'Hindi', 
    'Italian', 
    'Kannada', 
    'Malayalam', 
    'Portugeese', 
    'Russian', 
    'Spanish', 
    'Sweedish', 
    'Tamil', 
    'Turkish'
]


def predict_pipeline(text):
    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Model not loaded. Please check if the model file exists and is valid."
        )
    try:
        text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', ' ', text)
        text = re.sub(r'[[]]', ' ', text)
        text = text.lower()
        pred = model.predict([text])
        return classes[pred[0]]
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error during prediction: {str(e)}"
        )