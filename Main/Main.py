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

def add_bg_from_url():    st.markdown(         f"""         <style>         .stApp {{             background-image: url("https://github.com/jquintanac/Pythonscape/blob/main/imgs/background2.jpg?raw=true);             background-attachment: fixed;             background-size: cover         }}         </style>         """,         unsafe_allow_html=True     )

add_bg_from_url() 


#Sidebar: Ocultar nombres sidebar
no_sidebar_style = """    <style>        div[data-testid="stSidebarNav"] {display: none;}    </style>"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
placa= Image.open('/app/pythonscape/imgs/logo.png') 
st.sidebar.image(placa, use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')



# Video

st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

st.video('https://youtu.be/aZwbSuNrPPM')


# Contenido

st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown("<h2 style='text-align: center; color: white;'>Welcome to the Codes City Police Academy!", unsafe_allow_html=True)
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

portada = Image.open('/app/pythonscape/imgs/fronpage.jpg')  
st.image(portada, use_column_width=True)      
st.markdown('')
gil = Image.open('/app/pythonscape/imgs/gilb.png') 
st.image(gil)
st.markdown('<div style="text-align: justify;">Welcome buddy! My name is Gil Push and I am the Chief of Police at Codes City Police Academy. So I will be your instructor until you pass your first case</div>', unsafe_allow_html=True)
st.markdown('')
st.markdown("<div style='text-align: justify;'>You are a lucky buddy because we have a new case and we need your help! It has taken us too much time but finally we made it: we found out the Hacker's den! I need you to work as the computer expert you are and help our team that is arriving to hacker's den. We will need all your knowledge in Data analysis and your wit to solve the case. Are you ready, buddy?</div>", unsafe_allow_html=True)
st.markdown('')
st.markdown('<div style="text-align: justify;">Right here you will find all you need to start solving the case: a jupyter notebook that you have to download to write all you need to solve the case and a identification for the police service. We are sorry but we have not received your ID yet!. In case you need some help to solve the case because you do not know too much about Data analysis, just download the Junior jupyter notebook and follow the instructions. This experience would be nicer to you if a senior buddy join to you. If you feel prepared to work without guideline because you have enough knowledge about Data analysis, download the Senior jupyter notebook. Do not forget to count the time when you had finished since you started to get possitions in the ranking! You will have to give us back the completed jupyter notebook when finished! If you are ready, just click the button Start the game!</div>', unsafe_allow_html=True)

st.markdown('')

col1, col2, col3= st.columns([1,1,1])

with col1:

    with open('/app/pythonscape/docs/Jr_Buddy_notebook.ipynb', "rb") as file:
        btn = st.download_button(
                label='Your junior buddy notebook',
                data=file,
                file_name="Jr_Buddy_notebook.ipynb",
                )
            
with col3:

    with open("/app/pythonscape/imgs/ids.jpg", "rb") as file:
        btn = st.download_button(
                label='Your buddy identification',
                data=file,
                file_name="ids.jpg",
                mime="image/jpg")

with col2:

    with open('/app/pythonscape/docs/Sn_Buddy_notebook.ipynb', "rb") as file:
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
