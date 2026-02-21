import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/random_forest_model.pkl")

st.set_page_config(page_title="Loan Approval Prediction", layout="centered")

st.title("🏦 Loan Approval Prediction App")
st.write("Enter applicant details to predict loan approval status.")

# -------- User Inputs --------

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0,
    help="Monthly income of the applicant"
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0,
    help="Monthly income of the co-applicant"
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    help="Loan amount requested"
)

credit_history = st.selectbox(
    "Credit History",
    [1, 0],
    help="1 = Good credit history, 0 = Poor credit history"
)

employment_status = st.selectbox(
    "Employment Status",
    ["Employed", "Self-Employed", "Unemployed"]
)

# -------- Input DataFrame --------

input_data = pd.DataFrame({
    "ApplicantIncome": [applicant_income],
    "CoapplicantIncome": [coapplicant_income],
    "LoanAmount": [loan_amount],
    "Credit_History": [credit_history],
    "Employment_Status": [employment_status]
})

# -------- Prediction --------

if st.button("Predict Loan Status"):
    prediction = model.predict(input_data)[0]

    if prediction == "Y":
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")