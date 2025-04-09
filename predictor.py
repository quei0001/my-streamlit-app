# predictor.py - Prediction logic and input validation

import numpy as np
from sklearn.datasets import load_iris

def predict_species(input_data, model):
    """Predict the Iris species based on user input."""
    try:
        # Validate input data (must be a list of length 4)
        if len(input_data) != 4:
            raise ValueError("Input data must have 4 features.")
        
        input_data = np.array([input_data])
        
        # Make the prediction
        prediction = model.predict(input_data)
        
        # Load Iris species names
        iris = load_iris()
        species = iris.target_names[prediction[0]]
        return species

    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")
    except Exception as e:
        raise Exception(f"Prediction failed: {e}")
