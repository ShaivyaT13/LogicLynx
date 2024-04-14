from flask import Flask, render_template, request
import pickle
import numpy as np
from array import array

app1= Flask(__name__)

model=pickle.load(open('Fertilizer Prediction.pkl', 'rb'))

@app1.route('/')
def home():
    return render_template('fert.html')

@app1.route('/predict', methods=['POST'])
def predict():
    feature1 = float(request.form['Nitrogen'])
    feature2 = float(request.form['Potassium'])
    feature3 = float(request.form['Phosphorous'])
    print(feature1, feature2, feature3)
    features = np.array([[feature1, feature2, feature3]])
    print(features)
    prediction = model.predict(features)
    predicted_fert= prediction[0]
    return render_template('fert.html', prediction_text=f'you should use: {predicted_fert}' )

if __name__ == '__main__':
    app1.run(debug=True)