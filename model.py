# model.py - Model training and loading

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def load_model():
    """Load a pre-trained model or train a new one if it doesn't exist."""
    try:
        # Try loading an existing model if saved
        model = joblib.load("data/iris_model.pkl")
        print("✅ Model loaded from file.")
    except FileNotFoundError:
        print("🔄 No pre-trained model found. Training a new model...")
        model = train_model()
        joblib.dump(model, "data/iris_model.pkl")
    return model

def train_model():
    """Train the model and return it."""
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Model accuracy (optional)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"✅ Model trained. Accuracy: {accuracy:.2f}")

    return model
