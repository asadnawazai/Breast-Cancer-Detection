from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
# loading model
model = pickle.load(open('model.pkl', 'rb'))
# flask app
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = request.form['feature']
    if features =="":
        return render_template('index.html',mess="please fill the input.....")
    features = features.split(',')
    np_features = np.asarray(features, dtype=np.float32)

    # prediction
    pred = model.predict(np_features.reshape(1, -1))


    return render_template('index.html', message=pred, allowed="allowed")

if __name__ == '__main__':
    app.run(debug=True)
