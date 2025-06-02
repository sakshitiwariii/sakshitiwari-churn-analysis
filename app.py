import pandas as pd
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load your dataset
df_1 = pd.read_csv("first_telc.csv")

@app.route("/")
def loadPage():
    return render_template('home.html', query="")

@app.route("/", methods=['POST'])
def predict():
    try:
        # Collect all inputs
        inputs = {
            'SeniorCitizen': request.form['query1'],
            'MonthlyCharges': request.form['query2'],
            'TotalCharges': request.form['query3'],
            'gender': request.form['query4'],
            'Partner': request.form['query5'],
            'Dependents': request.form['query6'],
            'PhoneService': request.form['query7'],
            'MultipleLines': request.form['query8'],
            'InternetService': request.form['query9'],
            'OnlineSecurity': request.form['query10'],
            'OnlineBackup': request.form['query11'],
            'DeviceProtection': request.form['query12'],
            'TechSupport': request.form['query13'],
            'StreamingTV': request.form['query14'],
            'StreamingMovies': request.form['query15'],
            'Contract': request.form['query16'],
            'PaperlessBilling': request.form['query17'],
            'PaymentMethod': request.form['query18'],
            'tenure': request.form['query19']
        }

        # Convert numerical fields to appropriate types
        inputs['SeniorCitizen'] = int(inputs['SeniorCitizen'])
        inputs['MonthlyCharges'] = float(inputs['MonthlyCharges'])
        inputs['TotalCharges'] = float(inputs['TotalCharges'])
        inputs['tenure'] = int(inputs['tenure'])

        # Create DataFrame
        new_df = pd.DataFrame([inputs])

        # Load the model
        model = pickle.load(open("model.sav", "rb"))

        # Preprocessing - must match exactly what you did during training
        # 1. Create tenure groups (same as during training)
        labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]
        new_df['tenure_group'] = pd.cut(new_df['tenure'], range(1, 80, 12), 
                                right=False, labels=labels)
        
        # 2. Drop original tenure column
        new_df.drop(columns=['tenure'], axis=1, inplace=True)

        # 3. One-hot encoding (must match training exactly)
        categorical_cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService',
                          'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                          'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                          'Contract', 'PaperlessBilling', 'PaymentMethod', 'tenure_group']
        
        # Ensure all categorical columns are strings
        for col in categorical_cols:
            new_df[col] = new_df[col].astype(str)

        new_df_dummies = pd.get_dummies(new_df[categorical_cols])

        # Ensure we have all expected columns (add missing with 0s)
        # First, load the expected columns from your training data
        # You should save these when training the model
        expected_columns = pickle.load(open("expected_columns.sav", "rb"))
        
        # Add missing columns and set to 0
        for col in expected_columns:
            if col not in new_df_dummies.columns:
                new_df_dummies[col] = 0
        
        # Reorder columns to match training
        new_df_dummies = new_df_dummies[expected_columns]

        # Make prediction
        single = model.predict(new_df_dummies)
        probablity = model.predict_proba(new_df_dummies)[:,1][0]

        if single[0] == 1:
            o1 = "This customer is likely to be churned!!"
            o2 = "Confidence: {:.2f}%".format(probablity*100)
        else:
            o1 = "This customer is likely to continue!!"
            o2 = "Confidence: {:.2f}%".format(probablity*100)

        return render_template('home.html', 
                            output1=o1, 
                            output2=o2,
                            **{f'query{i}': request.form[f'query{i}'] for i in range(1, 20)})

    except Exception as e:
        return render_template('home.html', 
                            output1=f"Error: {str(e)}", 
                            output2="Please check your inputs",
                            **{f'query{i}': request.form.get(f'query{i}', '') for i in range(1, 20)})

if __name__ == "__main__":
    app.run(debug=True)
