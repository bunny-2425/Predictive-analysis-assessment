# Predictive-analysis-assessment

# Downtime Prediction Model

This project provides a FastAPI-based API to upload data, train a logistic regression model, and predict downtime based on temperature and run time.

## Setup

### 1. Clone the Repository

bash
git clone https://github.com/yourusername/downtime-prediction.git
cd downtime-prediction

2. Install Dependencies
Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

Install required dependencies:

bash
Copy
Edit
pip install -r requirements.txt

3. Run the Application
Start the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload

The app will run at http://127.0.0.1:8000.

API Endpoints
POST /upload: Upload a CSV file for preprocessing.

Request: CSV with Temperature, Run_Time, and Downtime_Flag.
Response: Returns dataset columns.
POST /train: Train the logistic regression model.

Request: None.
Response: Returns accuracy and F1 score of the trained model.
POST /predict: Predict downtime for a given temperature and run time.

Request: JSON with Temperature and Run_Time.
Response: JSON with Downtime (Yes/No) and Confidence score.
Example Usage
Upload Data:
bash
Copy
Edit
curl -X 'POST' 'http://127.0.0.1:8000/upload' -H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'file=@path_to_file.csv'
Train the Model:
bash
Copy
Edit
curl -X 'POST' 'http://127.0.0.1:8000/train' -H 'accept: application/json'
Make Predictions:
bash
Copy
Edit
curl -X 'POST' 'http://127.0.0.1:8000/predict' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"Temperature": 85, "Run_Time": 120}'
License
MIT License

csharp
Copy
Edit

You can copy this block and paste it directly into your `README.md` file.
