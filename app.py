# app.py - Streamlit app

import streamlit as st
from model import load_model
from predictor import predict_species
from utils import handle_error

# Load the trained model (this can be a pre-trained model in practice)
model = load_model()

def main():
    st.title("🌸 Iris Flower Species Predictor")
    st.write("Enter flower measurements to predict the species.")

    try:
        # Collect user input for prediction
        sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
        sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
        petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
        petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

        input_data = [sepal_length, sepal_width, petal_length, petal_width]

        if st.button("Predict"):
            species = predict_species(input_data, model)
            st.success(f"The predicted Iris species is: **{species}**")

    except Exception as e:
        handle_error(e)

if __name__ == '__main__':
    main()
