import pickle
import json
## Flask is a lightweight Python web framework used to build web applications or APIs, letting you turn your Python code (like an ML model) into a web service so others can access it via a browser or HTTP requests.
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd
app = Flask(__name__)
# Load the model
regmodel = pickle.load(open('regmodel.pkl','rb'))
scaler = pickle.load(open('scaling.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    df = pd.DataFrame([data])
    new_data = scaler.transform(df)
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify({'prediction': float(output[0])})

if __name__ =="__main__":
    app.run(debug = True)
    