# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:06:29 2024
Host the Model with UI- Iris_flasgger_04.py
@author: adminuser
"""


from flask import Flask,request
from flasgger import Swagger
import joblib
import numpy as np
import pandas as pd

model = joblib.load(r"IrisModel.model")

app = Flask(__name__)    # creating Flask instance
                         #  http://127.0.0.1:8005
                         
swagObj = Swagger(app)    #  http://127.0.0.1:8005/apidocs 

@app.route('/modelpredict',methods=['POST'])    
def app_predict():
    """Example endpoint returning prediction for Iris
    ---
    parameters:
        - name: s_length
          in: query
          type: number
          required: true
        - name: s_width
          in: query
          type: number
          required: true
        - name: p_length
          in: query
          type: number
          required: true
        - name: p_width
          in: query
          type: number
          required: true    
    """
   
    var1 = request.args.get('s_length')
    var2 = request.args.get('s_width')
    var3 = request.args.get('p_length')
    var4 = request.args.get('p_width')
   
    
    userInput_array = np.array([[var1,var2,var3,var4]])
    
    prediction = model.predict(userInput_array)
    
    return   "The prediction from server {}".format(prediction[0])   # prediction value to return

@app.route('/filepredict',methods=['POST'])    
def app_filepredict():
    """Example endpoint returning prediction for Iris
    ---
    parameters:
        - name: input_file
          in: formData
          type: file
          required: true
    """
    
    dataset = pd.read_csv(request.files.get("input_file"), header=None)

    prediction = model.predict(dataset)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8005, debug=True)       
                             
    
    
    
    
    
    
    
    
              