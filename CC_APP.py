import streamlit as st
import pickle
import numpy as np

# Custom CSS for background color
st.markdown(
    """
    <style>
    body {
        background-color: #e8f5e9; /* Verde suave */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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

# Input fields for the updated features
number_of_children = st.number_input(
    "Number of Children (e.g., 2):", min_value=0, max_value=20, step=1
)
current_salary = st.number_input(
    "Current Monthly Salary in € (e.g., 3000):", min_value=0, max_value=200000, step=100
)
savings = st.number_input(
    "Total Savings in € (e.g., 10000):", min_value=0, max_value=1000000, step=500
)
housing = st.selectbox(
    "Do you have any housing loan? (Yes/No):", options=["Yes", "No"]
)
current_loans = st.selectbox(
    "Do you have any current loans? (Yes/No):", options=["Yes", "No"]
)
monthly_expenses = st.number_input(
    "Monthly Expenses in € (e.g., 1500):", min_value=0, max_value=50000, step=100
)

# Convert categorical variables to numeric
housing_numeric = 1 if housing == "Yes" else 0
current_loans_numeric = 1 if current_loans == "Yes" else 0

# Prepare input data
input_data = np.array(
    [[number_of_children, current_salary, savings, housing_numeric, current_loans_numeric, monthly_expenses]]
)

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
