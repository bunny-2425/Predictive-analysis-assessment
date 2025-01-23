import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import pickle

MODEL_PATH = "model.pkl"

def train_model(dataset_path):
    # Load dataset
    df = pd.read_csv(dataset_path)

    # Preprocess data
    X = df[["Temperature", "Run_Time"]]
    y = df["Downtime_Flag"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Save model
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    return {"accuracy": accuracy, "f1_score": f1}

def predict(input_data):
    # Load model
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    # Predict
    data_df = pd.DataFrame([input_data])
    prediction = model.predict(data_df)[0]
    confidence = max(model.predict_proba(data_df)[0])
    
    result = {
        "Downtime": "Yes" if prediction == 1 else "No",
        "Confidence": round(confidence, 2)
    }
    return result
