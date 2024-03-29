# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:43:40 2021

@author: rincy
"""
import numpy as np
import pickle
from flask import Flask,request, render_template
app=Flask(__name__,template_folder="templates")
model = pickle.load(open('abalone.pkl', 'rb'))
@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')
@app.route('/home', methods=['GET'])
def about():
    return render_template('home.html')
@app.route('/pred',methods=['GET'])
def page():
    return render_template('upload.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    print(features_value)
    
    features_name = ['Sex','Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight']
    prediction = model.predict(features_value)
    output=prediction[0]    
    print(output)
    return render_template('upload.html', prediction_text='The predicted age of abalone is {} years.'.format((output+1.5)))

    
if __name__ == '__main__':
      app.run(debug=False)