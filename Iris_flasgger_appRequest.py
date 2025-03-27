
import numpy as np
import joblib
import streamlit

model = joblib.load("IrisModel.model")

# user defined Function
def iris_prediction(var_1,var_2,var_3,var_4):
    
    input_data = np.array([[var_1,var_2,var_3,var_4]])
    prediction = model.predict(input_data)
    
    from sklearn.datasets import load_iris
    iris=load_iris()
    return iris.target_names[prediction[0]]


def run():
    streamlit.title('Flower Classification')
    
    html_temp="""
    <div style="background-color:cyan">
    <h1 style="text-align:center">Flower Class Prediction ML Model</h1>    
    </div>    
    """

    streamlit.markdown(html_temp,unsafe_allow_html=True)
    
    v1=float(streamlit.text_input("Sepal Len",value=0.0))
    v2=float(streamlit.text_input("Sepal Width",value=0.0))
    v3=float(streamlit.text_input("Petal Len",value=0.0))
    v4=float(streamlit.text_input("Petal Width",value=0.0))


    prediction=""
    
    if streamlit.button("Predict"):
        prediction = iris_prediction(v1,v2,v3,v4)
        
    streamlit.success("The Predicted Flower Class: {}".format(prediction))


if __name__=="__main__":
    run()
