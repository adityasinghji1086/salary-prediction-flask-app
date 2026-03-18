import streamlit as st
import pickle
import numpy as np

# load model
model = pickle.load(open("model/model.pkl", "rb"))

st.title("Salary Prediction App")

exp = st.number_input("Enter Years of Experience", min_value=0.0, step=0.1)

if st.button("Predict"):
    prediction = model.predict([[exp]])
    st.success(f"Predicted Salary: ₹ {int(prediction[0])}")
