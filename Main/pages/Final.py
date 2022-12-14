import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain
import matplotlib.pyplot as plt
import pandas as pd
import os.path
import pathlib

# Cabecera
st.title('')
st.markdown('')
st.title('')
st.markdown('')
st.title('')
st.markdown('')
st.markdown('')
st.markdown('')



#Fondo

def add_bg_from_url():    st.markdown(         f"""         <style>         .stApp {{             background-image: url("https://github.com/jquintanac/Pythonscape/blob/main/imgs/background2.jpg?raw=true");             background-attachment: fixed;             background-size: cover         }}         </style>         """,         unsafe_allow_html=True     )

add_bg_from_url() 

#Sidebar: Ocultar nombres sidebar y login

no_sidebar_style = """    <style>        div[data-testid="stSidebarNav"] {display: none;}    </style>"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imgs/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')





# Botones para volver


col1, col2, col3 = st.columns([1,1,1])

with col1:
    boton=st.button('Back to James desktop')
    if boton:
        switch_page('desktopJ')

with col2:
    boton=st.button('Previous chat')
    if boton:
        switch_page('Chat7')

with col3:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')


# Contenido

st.markdown("<h1 style='text-align: center; color: white;'>Congratulations! You have caught the hacker in Tokyo!", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>The case is solved!", unsafe_allow_html=True)
st.markdown('')
st.markdown("<h3 style='text-align: center; color: white;'>Apparently, he was plotting about dropping Twitter and taking the control. This way, he could sell it on the stock market to earn a huge amount of cryptocurrency. Well done, we stopped the crime! ", unsafe_allow_html=True)



col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/arrested1.png?raw=true',use_column_width=True)
with col2:
    st.image("https://github.com/jquintanac/Pythonscape/blob/main/imgs/logo.png?raw=true", use_column_width=True)   
with col3:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/arrested5.png?raw=true',use_column_width=True)

col4, col5, col6 = st.columns([1,1,1])

with col4:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/arrested2.png?raw=true',use_column_width=True)
with col5:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/arrested3.png?raw=true',use_column_width=True)
with col6:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/arrested4.png?raw=true',use_column_width=True)


st.markdown('')
st.markdown("<h4 style='text-align: center; color: white;'> You can upload your jupyter notebook to get into the ranking. Thank you for participating and I hope you like it! ", unsafe_allow_html=True)

image_file= st.file_uploader("Upload your notebook", type=["ipynb"], key="uploaded_file")
if image_file is not None:
    file_details = {"FileName":image_file.name, "FileType":image_file.type}
    st.write(file_details)
    with open(os.path.join("https://drive.google.com/drive/folders/1_Ien05-EZIvcbPFefVD0V66LYZuAEtXf?usp=sharing",image_file.name),"wb") as f:
        f.write(image_file.getbuffer())
    st.success("File saved")

