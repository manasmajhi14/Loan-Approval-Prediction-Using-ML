# 🏦 Loan Approval Prediction Using Machine Learning

## 📌 Project Overview
This project focuses on building a machine learning–based classification system to predict whether a loan application should be **approved or rejected** based on applicant financial and employment details.  
The project simulates a real-world banking decision-making process using proper data preprocessing, exploratory analysis, model training, and evaluation.

---

## 🎯 Problem Statement
Banks need to evaluate loan applications efficiently while minimizing financial risk.  
Manual evaluation is time-consuming and may lead to inconsistent decisions.

**Objective:**  
To develop a machine learning model that predicts loan approval status using historical applicant data.

---

## 📊 Dataset Description
The dataset contains financial and employment-related information of loan applicants.

### Features:
- **ApplicantIncome** – Income of the primary applicant  
- **CoapplicantIncome** – Income of the co-applicant  
- **LoanAmount** – Loan amount requested  
- **Credit_History** – Credit history (1 = good, 0 = bad)  
- **Employment_Status** – Employment type of the applicant  

### Target Variable:
- **Loan_Status**
  - `Y` → Loan Approved  
  - `N` → Loan Rejected  

---

## 🔄 Project Workflow
The project follows an end-to-end machine learning pipeline:

1. Data Loading  
2. Data Cleaning & Preprocessing  
3. Exploratory Data Analysis (EDA)  
4. Feature Engineering  
5. Model Training  
6. Model Evaluation  
7. Model Comparison  
8. Model Saving  
9. Streamlit Demo 

---

## 🧹 Data Cleaning & Preprocessing
The following preprocessing steps were applied to prepare the data:

- Missing value handling  
  - Numerical features filled using **median**  
  - Categorical features filled using **mode**  
- Outlier removal using the **IQR method**  
- Categorical feature encoding using **One-Hot Encoding**  
- Feature scaling using **StandardScaler**  
- Train-test split (80% training, 20% testing) with stratification  

These steps ensure clean, unbiased, and model-ready data.

---

## 📈 Exploratory Data Analysis (EDA)
EDA was performed to understand data distribution and feature impact.

### Key Insights:
- Credit history has a strong influence on loan approval  
- Applicants with higher income have higher approval chances  
- Loan amount shows moderate impact on approval decisions  

### Visualizations:
- Loan status distribution  
- Applicant income vs loan status  
- Credit history vs loan status  
- Correlation heatmap  

---

## 🤖 Models Used
The following machine learning models were implemented:

1. **Logistic Regression**  
   - Baseline model  
   - Easy to interpret  

2. **Decision Tree Classifier**  
   - Captures non-linear relationships  
   - Prone to overfitting  

3. **Random Forest Classifier**  
   - Ensemble of multiple decision trees  
   - Provides better generalization and stability  

---

## 📏 Model Evaluation
Models were evaluated using:

- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Confusion Matrix  

### Why Recall is Important
In loan approval systems, approving loans for risky applicants can lead to financial loss.  
Therefore, **minimizing false negatives and improving recall** is critical.

---

## 🏆 Results & Model Comparison
- Logistic Regression showed stable but lower recall  
- Decision Tree improved recall but showed signs of overfitting  
- **Random Forest achieved the best performance**, with fewer false negatives and higher recall  

👉 **Random Forest was selected as the final model**

---

## 💾 Model Saving
All trained models were saved for future use:

- `logistic_regression_model.pkl`  
- `decision_tree_model.pkl`  
- `random_forest_model.pkl`  

These models can be reused for deployment or further experimentation.

---

## 🌐 Streamlit Demo 
A lightweight Streamlit web application was developed to demonstrate real-time loan approval prediction.  
Users can input applicant details and instantly receive loan approval predictions using the trained Random Forest model.

---

## 🧾 Conclusion
This project demonstrates a complete machine learning solution for loan approval prediction.  
By applying proper preprocessing, analysis, and evaluation techniques, the Random Forest model proved to be the most reliable for financial risk assessment.

---

## ▶️ How to Run the Project
1. Clone the repository or download the files  
2. Open `Loan_Approval_Prediction.ipynb` in Jupyter Notebook  
3. Run all notebook cells sequentially  
4. (Optional) Run Streamlit app using:
   ```bash
   streamlit run app.py
