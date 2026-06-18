import streamlit as st
import pandas as pd
import joblib

# Load Model and Scaler
model = joblib.load("heart.pkl")
scaler = joblib.load("heart_scaler.pkl")
st.title("Heart Disease Prediction System")

# Inputs
age = st.number_input("Age", 1, 120, 25)
sex = st.selectbox("Sex", [0, 1])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", 50, 250, 120)
chol = st.number_input("Cholesterol", 50, 700, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", 50, 250, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)
slope = st.selectbox("Slope", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3, 4])
thal = st.selectbox("Thal", [0, 1, 2, 3])

# Create DataFrame
input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'cp': [cp],
    'trestbps': [trestbps],
    'chol': [chol],
    'fbs': [fbs],
    'restecg': [restecg],
    'thalach': [thalach],
    'exang': [exang],
    'oldpeak': [oldpeak],
    'slope': [slope],
    'ca': [ca],
    'thal': [thal]
})

if st.button("Predict"):

    # Scale Input Data
    scaled_data = scaler.transform(input_data)

    # Predict
    prediction = model.predict(scaled_data)
    prob = model.predict_proba(scaled_data)

    st.write("Probability:", prob)

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")