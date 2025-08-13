from fastapi import FastAPI
from pydantic import BaseModel
import os
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version 
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Add CORS middleware - ADD THESE LINES
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predictmodel", response_model=PredictionOut)
async def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Get PORT from environment, default 8000
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)