import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu
import predictor
from predictor import tuberculosis,back_ground,diabetes
from PIL import Image
import numpy as np
import streamlit.components.v1 as component
import matplotlib.pyplot as plt

back_ground("back/md4.jpg")
with st.sidebar:
    back_ground("back/md4.jpg")
st.markdown(
"""
<style>
.sidebar .sidebar-content {
background-image: linear-gradient(#2e7bcf,#2e7bcf);
color: white;
 }
</style>
 """,
unsafe_allow_html=True,
 )

def main():
    #st.title("Login App")
    h1 = """
    <div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
    <h1 style='text-align: center; color: Black;'>SELF DIAGNOSIS SYSTEM</h1>
    </div>
    """
    h2d = """
    <div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
    <h2 style='text-align: center; color: Black;'>Tuberculosis Diagnosis</h2>
    </div>
    """
    h2v = """
    <div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
    <h2 style='text-align: center; color: Black;'>Diabetes Diagnosis</h2>
    </div>
    """
    h2a = """
    <div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
    <h2 style='text-align: center; color: Black;'>BloodPressure Diagnosis</h2>
    </div>
    """
    #menu = ["Home","Login","SignUp"]
    #choice = st.sidebar.selectbox("Main",menu)
    with st.sidebar:
        choice = option_menu(None, ["Home", "Diagnosis",  "Info"], 
            icons=['house', 'thermometer', "info"], 
            menu_icon="cast", default_index=0, orientation="vertical",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "green"},
            }
        )
    if choice == "Home":
        component.html(h1)
        st.subheader("Home")
    elif choice == "Diagnosis":
            component.html(h1)
            task = st.selectbox("Tasks",["Diabetes","Tuberculosis","BloodPressure"])
            if task == "Tuberculosis":
                tb= """
                <div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
                <h2 style='text-align: center; color: Black;'>Work in Progress..............</h2>
                </div>
                """
                #tuberculosis()
                component.html(tb)
            elif task == "Diabetes":
                component.html(h2v)
                diabetes()
            elif task == "BloodPressure":
                tb= """
                <div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
                <h2 style='text-align: center; color: Black;'>Work in Progress..............</h2>
                </div>
                """
                component.html(tb)
            
    elif choice == "Info":
        tb= """
        <div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
        <h2 style='text-align: center; color: Black;'>Work in Progress..............</h2>
        </div>
        """
        component.html(tb)
        #st.balloons()
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
footer = """
<style>
footer {
	
	visibility: hidden;
	
	}
footer:after {
	content:'Made With Love For AI'; 
	visibility: visible;
	display: block;
	position: relative;
	#background-color: red;
	padding: 5px;
	top: 2px;}
    </style>
"""
component.html(footer)
if __name__=='__main__':
    main()

