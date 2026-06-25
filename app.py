from flask import Flask, render_template, request
import joblib
import pandas as pd


app = Flask(__name__)


# ==========================
# Load Model and Scaler
# ==========================

model = joblib.load("Decision Tree.pkl")

scaler = joblib.load("X_Scaled.pkl")


print("Model loaded successfully")


# ==========================
# Transaction Type Encoding
# ==========================

type_mapping = {

    "PAYMENT": 0,
    "TRANSFER": 1,
    "CASH_OUT": 2,
    "DEBIT": 3,
    "CASH_IN": 4

}



# ==========================
# Home Page
# ==========================

@app.route("/")
def home():

    return render_template("index.html")



# ==========================
# Prediction
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    try:


        # Print received data
        print(request.form)



        # ======================
        # Get User Inputs
        # ======================


        step = float(
            request.form.get("step")
        )


        transaction_type = request.form.get(
            "type"
        )


        amount = float(
            request.form.get("amount")
        )


        oldbalanceOrg = float(
            request.form.get("oldbalanceOrg")
        )


        newbalanceOrig = float(
            request.form.get("newbalanceOrig")
        )


        oldbalanceDest = float(
            request.form.get("oldbalanceDest")
        )


        newbalanceDest = float(
            request.form.get("newbalanceDest")
        )



        acct_type = int(
            request.form.get("Acct_type")
        )


        date_transaction = int(
            request.form.get("Date_of_transaction")
        )


        time_day = int(
            request.form.get("Time_of_day")
        )


        branch = int(
            request.form.get("branch")
        )


        unusual_login = int(
            request.form.get("unusuallogin")
        )



        # ======================
        # Encode Type
        # ======================


        type_encoded = type_mapping.get(
            transaction_type,
            0
        )



        # ======================
        # Create DataFrame
        # SAME ORDER AS TRAINING
        # ======================


        input_data = pd.DataFrame(

            [[

                step,

                type_encoded,

                amount,

                oldbalanceOrg,

                newbalanceOrig,

                oldbalanceDest,

                newbalanceDest,

                acct_type,

                date_transaction,

                time_day,

                branch,

                unusual_login


            ]],


            columns=scaler.feature_names_in_

        )



        print("Input Data:")
        print(input_data)



        # ======================
        # Scaling
        # ======================


        input_scaled = scaler.transform(
            input_data
        )



        # ======================
        # Prediction
        # ======================


        prediction = model.predict(
            input_scaled
        )



        if prediction[0] == 1:


            result = "⚠ Fraudulent Transaction Detected"



        else:


            result = "✅ Legitimate Transaction"




        return render_template(

            "index.html",

            prediction_text=result

        )




    except Exception as e:


        print(e)


        return render_template(

            "index.html",

            prediction_text=f"Error: {str(e)}"

        )





# ==========================
# Run Flask
# ==========================


if __name__ == "__main__":


    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )