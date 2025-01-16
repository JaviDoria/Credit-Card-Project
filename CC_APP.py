{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88dd670e-f576-4ac1-b0d5-8da911b48131",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load the trained model and scaler\n",
    "with open('logistic_model.pkl', 'rb') as model_file:\n",
    "    model = pickle.load(model_file)\n",
    "\n",
    "with open('scaler.pkl', 'rb') as scaler_file:\n",
    "    scaler = pickle.load(scaler_file)\n",
    "\n",
    "# Streamlit app\n",
    "st.title(\"Customer Prediction App\")\n",
    "\n",
    "st.write(\"\"\"\n",
    "Welcome to the prediction tool!  \n",
    "This app uses a trained model to predict outcomes based on the data you provide.  \n",
    "Please fill out the form below to see the results.\n",
    "\"\"\")\n",
    "\n",
    "# Define input fields for the app\n",
    "st.header(\"Enter the required details:\")\n",
    "\n",
    "# Replace these with actual feature descriptions\n",
    "age = st.number_input(\"Age (e.g., 25):\", min_value=0, max_value=120, step=1)\n",
    "salary = st.number_input(\"Monthly Income in USD (e.g., 3000):\", min_value=0, max_value=100000, step=100)\n",
    "gender = st.selectbox(\"Gender:\", options=[\"Male\", \"Female\"])\n",
    "experience = st.number_input(\"Years of Work Experience (e.g., 5):\", min_value=0, max_value=50, step=1)\n",
    "\n",
    "# Convert gender input to numeric value\n",
    "gender_numeric = 0 if gender == \"Male\" else 1\n",
    "\n",
    "# Prepare input data\n",
    "input_data = np.array([[age, salary, gender_numeric, experience]])\n",
    "\n",
    "# Scale the input data\n",
    "input_data_scaled = scaler.transform(input_data)\n",
    "\n",
    "# Predict button\n",
    "if st.button(\"Predict\"):\n",
    "    prediction = model.predict(input_data_scaled)\n",
    "    prediction_proba = model.predict_proba(input_data_scaled)\n",
    "\n",
    "    # Display the result in user-friendly terms\n",
    "    st.subheader(\"Prediction Results:\")\n",
    "    result = \"Yes\" if prediction[0] == 1 else \"No\"\n",
    "    st.write(f\"Prediction: **{result}**\")\n",
    "    st.write(f\"Probability of Positive Outcome: **{prediction_proba[0][1] * 100:.2f}%**\")\n",
    "    st.write(f\"Probability of Negative Outcome: **{prediction_proba[0][0] * 100:.2f}%**\")\n",
    "\n",
    "    st.info(\"This prediction is based on the data you entered. Please consult a professional for detailed insights.\")\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
