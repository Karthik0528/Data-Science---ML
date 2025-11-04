import streamlit as st
import numpy as np
import joblib

# Load saved models
model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load('supervised_scaler.pkl')

st.set_page_config(page_title="❤️ Heart Disease Risk Predictor", layout="centered")

st.title("❤️ Heart Disease Risk Predictor")
st.markdown("### Predict your heart disease risk based on key health indicators")

# Input fields
age = st.number_input("Age", min_value=20, max_value=100, value=50)
sex = st.selectbox("Sex", ("Male", "Female"))
resting_bp = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, value=120)
chol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
max_hr = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=6.5, value=1.0)
exercise_angina = st.selectbox("Exercise Induced Angina", ("Yes", "No"))

# Encode categorical inputs
sex = 1 if sex == "Male" else 0
exercise_angina = 1 if exercise_angina == "Yes" else 0

# Prepare input array
input_data = np.array([[age, sex, resting_bp, chol, 0, max_hr, exercise_angina, oldpeak, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])  # dummy 20 features

# Scale input data
input_scaled = scaler.transform(input_data)

# Predict
if st.button("🔍 Predict Risk"):
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Risk of Heart Disease! (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Low Risk of Heart Disease (Probability: {probability:.2f})")

st.caption("Made with 💻 by Karthik | BE CSE-AI")
