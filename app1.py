import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🧠 Burnout Predictor App")

# Collect user input
gender = st.selectbox("Gender", ["Male", "Female"])
company_type = st.selectbox("Company Type", ["Product", "Service"])
wfh = st.selectbox("WFH Setup Available", ["Yes", "No"])
designation = st.slider("Designation Level (0–5)", 0, 5, 2)
resource_allocation = st.slider("Daily Resource Allocation (0–10)", 0, 10, 5)
mental_fatigue = st.slider("Mental Fatigue Score (0–10)", 0.0, 10.0, 5.0)
tenure = st.slider("Tenure (Days at Company)", 0, 5000, 1000)

# Encode inputs
input_df = pd.DataFrame({
    'Designation': [designation],
    'Resource Allocation': [resource_allocation],
    'Mental Fatigue Score': [mental_fatigue],
    'Tenure': [tenure],
    'Gender_Male': [1 if gender == "Male" else 0],
    'Company Type_Product': [1 if company_type == "Product" else 0],
    'WFH Setup Available_Yes': [1 if wfh == "Yes" else 0]
})

# Align input with model columns
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[model.feature_names_in_]

# Predict
if st.button("Predict Burnout Rate"):
    prediction = model.predict(input_df)[0]
    st.success(f"🔮 Predicted Burnout Rate: {prediction:.2f}")
