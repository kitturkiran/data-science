# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:01:17 2020

"""



import pandas as pd
import streamlit as st 
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load

st.title('Model Deployment: Logistic Regression')

st.sidebar.header('User Input Parameters')

def user_input_features():
    bookname= st.text_input('Book-Title',"Type Here")
    
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)


# load the model from disk
loaded_model = load(open('filename', 'rb'))


st.subheader('Predicted book')
st.write(matrix.index[indices.flatten()[i]])




