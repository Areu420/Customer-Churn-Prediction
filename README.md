📌 Customer Churn Prediction

🔍 Overview

This project predicts whether a telecom customer is likely to churn (leave the service) using machine learning.

Instead of relying on a single algorithm, multiple models are trained and compared. The best model is selected based on performance metrics.

The goal is to help businesses identify high-risk customers early and improve retention strategies.

⸻

📊 Dataset

* Source: IBM Telco Customer Churn Dataset
* Records: ~7000 customers
* Target Variable: Churn (Yes / No)

⸻

🧠 Key Insights from EDA

* Month-to-month contracts → highest churn
* Low tenure customers → more likely to churn
* No Tech Support & Online Security → high churn risk
* High Monthly Charges → increased churn probability
* Features like gender and phone service → minimal impact

⸻

⚙️ Feature Engineering

Derived from EDA insights:

* tenure_group → customer lifecycle segmentation
* HighRisk_Contract → identifies month-to-month users
* NoSupport → no tech support + no security
* FiberUser → fiber internet risk indicator

These features improve model understanding of churn behavior.

⸻

🤖 Models Used

The project implements and compares three models:

* Logistic Regression
* Random Forest
* XGBoost

All models are trained using the same preprocessing pipeline for fair comparison.

⸻

🏆 Model Selection

Models are evaluated using:

* ROC-AUC (primary metric)
* Accuracy
* Precision
* Recall
* F1 Score

👉 The best model is selected based on highest ROC-AUC score

🏗️ Pipeline Architecture

* Numerical features → StandardScaler
* Categorical features → OneHotEncoder
* Combined using → ColumnTransformer
* Full workflow managed using → Pipeline

This ensures consistent preprocessing during both training and prediction.

⸻

⚖️ Handling Class Imbalance

* Logistic & Random Forest → class_weight = "balanced"
* XGBoost → scale_pos_weight

This improves detection of churn cases.

⸻

🌐 Web Application

A Flask-based UI allows users to:

* Input customer details
* Predict churn probability
* View:
    * Stay %
    * Churn %
* See risk level:
    * Low
    * Medium
    * High

📁 Project Structure
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

⚠️ Limitations

* Predictions are probabilistic, not guaranteed
* Small differences between models (~0.003 ROC-AUC)
* Performance depends on available features

⸻

🚀 Future Improvements

* Hyperparameter tuning for XGBoost
* Cross-validation for stronger evaluation
* Add model explainability (feature contribution)
* Improve UI with analytics dashboard

⸻

📌 Conclusion

This project demonstrates a complete ML workflow:

* Data cleaning
* Feature engineering
* Multi-model comparison
* Proper evaluation
* Model deployment
