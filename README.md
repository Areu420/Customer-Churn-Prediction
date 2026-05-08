Customer Churn Prediction System

🔍 Overview

This project is a complete end-to-end Machine Learning application that predicts whether a telecom customer is likely to churn.

The system performs:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature engineering
* Model training and evaluation
* Model serialization
* Flask-based deployment

The trained machine learning model is integrated into a Flask web application where users can enter customer details and instantly receive churn predictions with probability scores.

The main objective of this project is to help telecom companies identify customers at high risk of leaving so retention strategies can be applied proactively.

⸻

📊 Dataset

* Dataset Used: IBM Telco Customer Churn Dataset
* Total Records: ~7000 customer records
* Target Variable: Churn
* Prediction Type: Binary Classification

The dataset contains:

* Customer demographics
* Account information
* Subscription details
* Billing information
* Service usage patterns

⸻

📈 Exploratory Data Analysis (EDA)

EDA was performed to identify patterns affecting customer churn.

Key Findings

* Customers with month-to-month contracts showed significantly higher churn.
* Customers with low tenure were more likely to leave.
* Users without:
    * Tech Support
    * Online Security
        had increased churn probability.
* Higher monthly charges were associated with greater churn risk.
* Features like:
    * Gender
    * Phone Service
        showed relatively low influence on churn.

Visual analysis and correlation checks were used to better understand customer behavior before model building.

⸻

⚙️ Data Preprocessing

The preprocessing pipeline includes:

* Handling missing values
* Label encoding target values
* One-hot encoding categorical variables
* Feature scaling for numerical columns
* Splitting dataset into training and testing sets

Pipeline Components

* StandardScaler → numerical feature scaling
* OneHotEncoder → categorical encoding
* ColumnTransformer → combines preprocessing steps
* Pipeline → creates a consistent ML workflow

This ensures identical preprocessing during both training and real-time prediction.

⸻

🧠 Feature Engineering

Additional features were created based on EDA insights to improve prediction performance.

Engineered Features

* tenure_group
    * Segments customers based on customer lifecycle.
* HighRisk_Contract
    * Flags month-to-month contract customers.
* NoSupport
    * Identifies customers lacking tech support and online security.
* FiberUser
    * Indicates customers using fiber internet services.

These engineered features help the model better capture churn behavior patterns.

⸻

🤖 Machine Learning Models Used

The project trains and compares multiple classification algorithms.

Models Implemented

1. Logistic Regression
2. Random Forest Classifier
3. XGBoost Classifier

All models use the same preprocessing pipeline to ensure fair evaluation.

⸻

🏆 Model Evaluation

Models were evaluated using multiple performance metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

Primary Metric

ROC-AUC was used as the primary metric because churn prediction is an imbalanced classification problem.

The best-performing model was selected based on the highest ROC-AUC score.

⸻

⚖️ Handling Class Imbalance

Customer churn datasets are naturally imbalanced because non-churn customers are usually higher in number.

To improve churn detection:

* Logistic Regression and Random Forest used:
    * class_weight = "balanced"
* XGBoost used:
    * scale_pos_weight

This helps the model better identify actual churn cases.

⸻

🌐 Flask Web Application

A Flask-based frontend interface is integrated with the trained model.

Features

Users can:

* Enter customer information
* Predict churn probability instantly
* View:
    * Churn Percentage
    * Retention Percentage
* Receive risk categorization:
    * Low Risk
    * Medium Risk
    * High Risk

The Flask app loads the trained serialized model and performs real-time predictions.

⸻

🏗️ Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Serialization
8. Flask Deployment
9. Real-Time Prediction

⸻

📁 Project Structure

Customer-Churn-Prediction/
│
├── templates/
│   └── home.html
│
├── static/
│
├── app.py
├── model.sav
├── EDA.ipynb
├── ModelBuild.ipynb
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── requirements.txt
└── README.md

⸻

🛠️ Technologies Used

Programming Language

* Python

Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Flask
* Joblib / Pickle

⸻

▶️ Running the Project

1. Clone the Repository

git clone <repository-url>
cd Customer-Churn-Prediction

2. Install Dependencies

pip install -r requirements.txt

3. Run the Flask Application

python app.py

4. Open in Browser

http://127.0.0.1:5000

⸻

⚠️ Limitations

* Predictions are probabilistic and not guaranteed.
* Small performance differences exist between models.
* Model performance depends heavily on dataset quality and available features.
* External business factors affecting churn are not included.

⸻

🚀 Future Improvements

Possible improvements for the project:

* Hyperparameter tuning
* Cross-validation optimization
* Feature importance visualization
* SHAP-based explainability
* Advanced ensemble techniques
* Cloud deployment
* Improved UI dashboard with analytics
* Real-time database integration

⸻

📌 Conclusion

This project demonstrates a complete machine learning lifecycle from raw data to deployment.

It includes:

* Data preprocessing
* Feature engineering
* Model comparison
* Performance evaluation
* Handling class imbalance
* Flask deployment
* Real-time churn prediction

The project provides practical exposure to building production-oriented ML systems and deploying predictive models into usable web applications.
