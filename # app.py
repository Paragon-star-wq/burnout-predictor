# app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import datetime

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🔮 Employee Burnout Predictor")
st.write("Enter employee details to predict burnout risk")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
company_type = st.selectbox("Company Type", ["Product", "Service"])
wfh = st.selectbox("WFH Setup Available?", ["Yes", "No"])
designation = st.slider("Designation (1 = Junior, 5 = Executive)", 0, 5, 2)
resource_alloc = st.slider("Resource Allocation (hrs/day)", 0.0, 10.0, 5.0)
mental_fatigue = st.slider("Mental Fatigue Score (0-10)", 0.0, 10.0, 5.0)
doj = st.date_input("Date of Joining")

# Calculate tenure
today = datetime.date.today()
tenure = (today - doj).days

# Prepare input features
input_df = pd.DataFrame({
    'Designation': [designation],
    'Resource Allocation': [resource_alloc],
    'Mental Fatigue Score': [mental_fatigue],
    'Tenure': [tenure],
    'Gender_Male': [1 if gender == "Male" else 0],
    'Company Type_Product': [1 if company_type == "Product" else 0],
    'WFH Setup Available_Yes': [1 if wfh == "Yes" else 0],
})

# Predict burnout rate
if st.button("Predict Burnout Rate"):
    result = model.predict(input_df)[0]
    st.success(f"🔻 Predicted Burnout Rate: {round(result, 3)}")
