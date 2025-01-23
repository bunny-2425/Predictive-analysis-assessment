from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import pandas as pd
from model import train_model, predict
import os

app = FastAPI()

# Upload Endpoint
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not os.path.exists("data"):
        os.makedirs("data")
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return {"message": "File uploaded successfully", "file_path": file_path}

# Train Endpoint
@app.post("/train")
async def train():
    dataset_path = "data/sample_data.csv"  # Default dataset path
    metrics = train_model(dataset_path)
    return {"message": "Model trained successfully", "metrics": metrics}

# Predict Endpoint
class PredictInput(BaseModel):
    Temperature: float
    Run_Time: float

@app.post("/predict")
def predict_downtime(input_data: PredictInput):
    result = predict(input_data.dict())
    return result
