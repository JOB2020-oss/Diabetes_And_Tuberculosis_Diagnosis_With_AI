import streamlit as st
from PIL import Image
import tensorflow
import numpy as np
import base64
import sqlite3
import pandas as pd
import streamlit.components.v1 as component
import pickle
from xgboost import XGBClassifier
import tensorflow.keras as keras  

model = keras.models.load_model("models/tb_model.h5")
    
def tuberculosis():
    file = st.file_uploader("PLEASE DRAG AND DROP XRAY IMAAGE OF CHEST SAMPLE")
    if file:
        image = Image.open(file)
        #path = r"C:\Users\Job Moshi\Desktop\xyz\TB01\Tuberculosis\Tuberculosis.9.png"
        #image = keras.preprocessing.image.load_img(path,target_size=(250,250))
        st.image(image,use_column_width=False,width=200,caption=None)
        image = keras.preprocessing.image.img_to_array(image)
        image = tensorflow.image.resize(image,(50,50))/255
        image = tensorflow.expand_dims(image,0)
        if st.button("Analyse"):
            pred_ = model.predict(image)
            #if pred =
            #st.success(pred_)
               
def diabetes():
    model0 = pickle.load(open("models/model_xg.pkl","rb"))
    glucose = st.slider("GLUCOSE (mg/dL)",min_value=0,max_value=200)
    sys_bp = st.slider("SYSTOLE PRESSURE INDEX (mmHg)",min_value=80,max_value=200)
    dias_bp = st.slider("DIASTOLIC PRESSURE INDEX (mmHg)",min_value=0,max_value=100)
    height = st.slider("HEIGHT (cm)",min_value=120,max_value=223)
    chol = st.slider("CHOLESTROL LEVEL (mg/dl)",min_value=45,max_value=150)
    sex = st.radio("GENDER",options=["Male","Female"])
    if sex == "Male":
        sex = 1
    elif sex == "Female":
        sex = 0
    age = st.slider("AGE (Years)",min_value=0,max_value=120)
    whp = st.slider("WAIST_HIP_RATIO",min_value=0.1,max_value=0.4)
    var = [[glucose,sys_bp,dias_bp,height,chol,sex,age,whp]]
    button =  st.button("ANALYSE")
    if button:
        pred = model0.predict(var)
        if pred == 0:
            res = """
            <div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
            <h1 style='text-align: center; color: Black;'>NORMAL</h1>
            </div>"""
            component.html(res)
        elif pred == 1:
            res = """
            <div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
            <h1 style='text-align: center; color: Black;'>DIABETIC</h1>
            </div>"""
            component.html(res)
def back_ground(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
back_ground("back/back.jpg")