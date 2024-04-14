from flask import Flask, render_template, request
import pickle
import numpy as np
from array import array

app= Flask(__name__)

model=pickle.load(open('RandomForest.pkl','rb'))

@app.route('/')
def home():
    return render_template('croprec.html')

@app.route('/predict',methods=['POST'])
def predict():
    feature1 = float(request.form['Temperature'])
    feature2 = float(request.form['Humidity'])
    feature3 = float(request.form['pH'])
    feature4 = float(request.form['Rainfall'])
    print(feature1, feature2, feature3, feature4)
    features = np.array([[feature1, feature2, feature3, feature4]])
    print(features)
    prediction = model.predict(features)
    predicted_crop= prediction[0]
    return render_template('croprec.html', prediction_text=f'you should grow: {predicted_crop}' )

if __name__ == '__main__':
    app.run(debug=True)