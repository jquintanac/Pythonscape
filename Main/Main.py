#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page




#Fondo

def add_bg_from_url():    st.markdown(         f"""         <style>         .stApp {{             background-image: url("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/background2.jpg?raw=true");             background-attachment: fixed;             background-size: cover         }}         </style>         """,         unsafe_allow_html=True     )

add_bg_from_url() 


#Sidebar: Ocultar nombres sidebar
no_sidebar_style = """    <style>        div[data-testid="stSidebarNav"] {display: none;}    </style>"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')




# Contenido

st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/fronpage.jpg?raw=true')

st.markdown('<div style="text-align: justify;">Welcome to this adventure in which you have to catch a dangerous hacker using your data analysis knowledge! You have to work as a computer expert for the police and help your partner in crime. Are you ready for this challenge?</div>', unsafe_allow_html=True)

st.markdown('')

st.markdown('<div style="text-align: justify;">Right here you will find all you need to start playing: a jupyter notebook that you have to download to write all you need to solve the case and your identification for police department. In case you need some help to solve the case because you do not know too much about Data analysis, just download the Junior jupyter notebook. If you feel prepared to work without guideline because you can have enough knowledge about Data analysis, download de Senior jupyter notebook. Do not forget to count the time where you had finished since you started to get possitions in the ranking! You will have to give us back the jupyter completed when finished! If you are ready, just click the button Start the game!</div>', unsafe_allow_html=True)

st.markdown('')

col1, col2, col3= st.columns([1,1,1])

with col1:

    with open("../Jr_Buddy_notebook.ipynb", "rb") as file:
        btn = st.download_button(
                label='Your junior buddy notebook',
                data=file,
                file_name="Jr_Buddy_notebook.ipynb",
                )
            
with col3:

    with open("../imgs/ids.jpg", "rb") as file:
        btn = st.download_button(
                label='Your buddy identification',
                data=file,
                file_name="ids.jpg",
                mime="image/jpg")

with col2:

    with open("../Sn_Buddy_notebook.ipynb", "rb") as file:
        btn = st.download_button(
                label='Your senior buddy notebook',
                data=file,
                file_name="Sn_Buddy_notebook.ipynb",
                )

st.text('')
st.text('')
st.text('')
col4, col5, col6= st.columns([1,1,1])

with col4:
    st.empty()

with col5:
    empezar=st.button('Start the game!')    
    if empezar:
        switch_page('Inicio')

with col6:
    st.empty()

st.markdown('')
























# %%
