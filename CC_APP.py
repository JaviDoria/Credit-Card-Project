import streamlit as st
import pickle
import numpy as np

# Load the trained model and scaler
with open('logistic_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Streamlit app
st.title("Customer Prediction App")

st.write("""
Welcome to the prediction tool!  
This app uses a trained model to predict outcomes based on the data you provide.  
Please fill out the form below to see the results.
""")

# Define input fields for the app
st.header("Enter the required details:")

# Replace these with actual feature descriptions
age = st.number_input("Age (e.g., 25):", min_value=0, max_value=120, step=1)
salary = st.number_input("Monthly Income in USD (e.g., 3000):", min_value=0, max_value=100000, step=100)
gender = st.selectbox("Gender:", options=["Male", "Female"])
experience = st.number_input("Years of Work Experience (e.g., 5):", min_value=0, max_value=50, step=1)

# Convert gender input to numeric value
gender_numeric = 0 if gender == "Male" else 1

# Prepare input data
input_data = np.array([[age, salary, gender_numeric, experience]])

# Scale the input data
input_data_scaled = scaler.transform(input_data)

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data_scaled)
    prediction_proba = model.predict_proba(input_data_scaled)

    # Display the result in user-friendly terms
    st.subheader("Prediction Results:")
    result = "Yes" if prediction[0] == 1 else "No"
    st.write(f"Prediction: **{result}**")
    st.write(f"Probability of Positive Outcome: **{prediction_proba[0][1] * 100:.2f}%**")
    st.write(f"Probability of Negative Outcome: **{prediction_proba[0][0] * 100:.2f}%**")

    st.info("This prediction is based on the data you entered. Please consult a professional for detailed insights.")

