from flask import Flask, render_template, request
import pandas as pd
import pickle
app = Flask(__name__)
model = pickle.load(open("model.sav", "rb"))
def engineer_features(df):
    bins = [0,12,24,36,48,60,72]
    labels = ["0-1yr","1-2yr","2-3yr","3-4yr","4-5yr","5+yr"]
    df["tenure_group"] = pd.cut(df["tenure"], bins=bins, labels=labels)
    df["AvgMonthlySpend"] = df["TotalCharges"] / (df["tenure"] + 1)
    df["HighRisk_Contract"] = (df["Contract"] == "Month-to-month").astype(int)
    df["NoSupport"] = (
        (df["TechSupport"] == "No") &
        (df["OnlineSecurity"] == "No")
    ).astype(int)
    df["FiberUser"] = (df["InternetService"] == "Fiber optic").astype(int)
    return df
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            data = {
                "gender": request.form.get("gender"),
                "SeniorCitizen": int(request.form.get("SeniorCitizen")),
                "Partner": request.form.get("Partner"),
                "Dependents": request.form.get("Dependents"),
                "PhoneService": request.form.get("PhoneService"),
                "MultipleLines": request.form.get("MultipleLines"),
                "InternetService": request.form.get("InternetService"),
                "OnlineSecurity": request.form.get("OnlineSecurity"),
                "OnlineBackup": request.form.get("OnlineBackup"),
                "DeviceProtection": request.form.get("DeviceProtection"),
                "TechSupport": request.form.get("TechSupport"),
                "StreamingTV": request.form.get("StreamingTV"),
                "StreamingMovies": request.form.get("StreamingMovies"),
                "Contract": request.form.get("Contract"),
                "PaperlessBilling": request.form.get("PaperlessBilling"),
                "PaymentMethod": request.form.get("PaymentMethod"),
                "tenure": int(request.form.get("tenure")),
                "MonthlyCharges": float(request.form.get("MonthlyCharges")),
                "TotalCharges": float(request.form.get("TotalCharges")),
            }
            df = pd.DataFrame([data])
            df = engineer_features(df)
            pred = model.predict(df)[0]
            probs = model.predict_proba(df)[0]
            stay_prob = round(probs[0] * 100, 2)
            churn_prob = round(probs[1] * 100, 2)
            if pred == 1:
                result = "Likely to Churn"
            else:
                result = "Will Stay"
            if churn_prob > 70:
                risk = "High Risk"
                color = "danger"
            elif churn_prob > 40:
                risk = "Medium Risk"
                color = "warning"
            else:
                risk = "Low Risk"
                color = "success"
            return render_template(
                "home.html",
                result=result,
                stay_prob=stay_prob,
                churn_prob=churn_prob,
                risk=risk,
                color=color
            )
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)