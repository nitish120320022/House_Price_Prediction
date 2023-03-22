# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 12:25:58 2022

@author: Hp
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('House_Price_Prediction.pkl','rb')) 

@app.route('/')
def home():
  
    return render_template("index.html")
  
  
@app.route('/pr',methods=['GET'])
def predict():
  exp1 = float(request.args.get('exp1'))
  exp2 = float(request.args.get('exp2'))
  exp3 = float(request.args.get('exp3'))
  exp4 = float(request.args.get('exp4'))
  exp5 = float(request.args.get('exp5'))
  exp6 = float(request.args.get('exp6'))
  prediction = model.predict([[exp1,exp2,exp3,exp4,exp5,exp6]])
  return render_template('index.html', prediction_text='Regression Model  has predicted Price for the House : {}'.format(prediction))
if __name__ == "__main__":
    app.run(debug = True)