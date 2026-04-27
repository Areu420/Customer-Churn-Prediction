# Customer Churn Prediction

# Overview
This project predicts whether a telecom customer is likely to churn (leave the service) based on their demographic, service usage, and billing information.

The goal is to identify high-risk customers early so that businesses can take preventive actions.

---

# Dataset
- Source: IBM Telco Customer Churn Dataset  
- Records: ~7000 customers  
- Target Variable: Churn (Yes / No)

---

# Key Insights from EDA
- Customers with month-to-month contracts have the highest churn rate  
- Low tenure (new customers) are more likely to churn  
- Lack of TechSupport and OnlineSecurity increases churn  
- High monthly charges correlate with higher churn  
- Features like gender and phone service have minimal impact  

---

# Feature Engineering
Based on EDA, the following features were created:

- tenure_group → customer lifecycle segmentation  
- AvgMonthlySpend → spending behavior  
- HighRisk_Contract → month-to-month indicator  
- NoSupport → lack of security + tech support  
- FiberUser → high-risk internet category  

These features help the model capture real churn patterns.

---

# Model
- Algorithm: Random Forest Classifier  
- Pipeline:
  - Numerical features → StandardScaler  
  - Categorical features → OneHotEncoder  
- Class imbalance handled using:
  - class_weight = "balanced"

---

# Evaluation Metrics
- Accuracy  
- ROC-AUC Score  
- Precision / Recall (for churn detection)

Note: The model focuses on detecting churn patterns rather than memorizing exact dataset labels.

---

# Project Structure
Customer-Churn-Prediction/
│
├── templates/
│   └── home.html
├── EDA.ipynb
├── ModelBuild.ipynb
├── app.py
├── model.sav
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
└── README.md

---

# Web Application
A Flask-based web app allows users to:
- Input customer details  
- Get churn prediction  
- View probability of:
  - Staying  
  - Churning  
- See risk level (Low / Medium / High)

---

# How to Run

1. Clone the repository:
git clone <your-repo-link> cd Customer-Churn-Prediction

2. Install dependencies:
pip install -r requirements.txt

3. Run the app:
python app.py

4. Open in browser:
http://127.0.0.1:5000/

---

# Limitations
- Model predictions are probabilistic, not exact  
- Some non-churn customers may be predicted as churn (false positives)  
- Performance depends on available features in dataset  

---

# Future Improvements
- Try advanced models (XGBoost, LightGBM)  
- Hyperparameter tuning  
- Add explainability (feature contributions per prediction)  
- Improve UI with analytics dashboard  

---

# Conclusion
The model successfully captures key churn patterns such as:
- early-stage customers  
- high charges  
- lack of support services  

This makes it useful for real-world customer retention strategies.
