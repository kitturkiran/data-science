#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install streamlit')


# In[2]:


import streamlit as st
import pickle
import pandas as pd
import requests

st.title('books Recommender System')



matrix= pickle.load(open("books.pk1","rb"))
model= pickle.load(open("model.pk1",'rb'))
result= pickle.load(open("result.pk1",'rb'))
def recommend(books):



  distances, indices = model.kneighbors(matrix.loc[books].values.reshape(1, -1), n_neighbors =10)
  print("\nRecommended books:\n")
  for i in range(0, len(distances.flatten())):
    if i > 0:
        print(matrix.index[indices.flatten()[i]]) 



books_list = result['Book-Title'].values
selected_book= st.selectbox('Select a books from drop down',books_list)

st.write('You selected:', selected_book)


if st.button('Show Recommend book'):
    recommended_book_names = recommend(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_book_names[0])
        

    with col2:
        st.text(recommended_book_names[1])
      

    with col3:
        st.text(recommended_book_names[2])
      

    with col4:
        st.text(recommended_book_names[3])
       

    with col5:
        st.text(recommended_book_names[4])


# In[ ]:




