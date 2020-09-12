import streamlit as st
import pandas as pd
import numpy as np
import pickle
import util
import pickle
import json


st.write("""
# Home Price Prediction App
This app predicts the **Home Price** of City!
""")

st.sidebar.header('User Input Features')

util.load_saved_artifacts()

total_sqft = st.sidebar.text_input('Area (Square Feet):',1200)
total_sqft=int(total_sqft)
bhk = st.sidebar.selectbox('BHK',(1,2,3,4,5,6),1)
bath = st.sidebar.selectbox('Bathroom',(1,2,3,4,5,6),1)
location = st.sidebar.selectbox('Location',(util.__locations))
  
response = util.get_estimated_price(location,total_sqft,bhk,bath)

st.subheader('Please select the required details at Sidebar to check ***Home Price ***')
st.write('')
st.write("You selected Location : **",location,"**")
st.write("You selected Area : **", total_sqft,"**")
st.write("You selected BHK : **", bhk,"**")
st.write("You selected Bathroom : **",bath,"**")
st.write("**Price = ",response," Lacs( INR )**")
st.write('')
st.write('')
st.write('')
st.write("*By-   Shalendra Kumar*")

