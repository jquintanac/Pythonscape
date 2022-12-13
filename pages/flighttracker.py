import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from streamlit_extras.stoggle import stoggle

# Cabecera
st.title('')
st.markdown('')
st.title('')
st.markdown('')
st.title('')
st.markdown('')
st.markdown('')
st.markdown('')

st.markdown("<h3 style='text-align: center; color: white;'>Welcome to the Codes City Police Service.", unsafe_allow_html=True)

#Fondo

def add_bg_from_url():    st.markdown(         f"""         <style>         .stApp {{             background-image: url("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/background2.jpg?raw=true");             background-attachment: fixed;             background-size: cover         }}         </style>         """,         unsafe_allow_html=True     )

add_bg_from_url() 

#Sidebar: Ocultar nombres sidebar y login

no_sidebar_style = """    <style>        div[data-testid="stSidebarNav"] {display: none;}    </style>"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')


# Titulo


st.title('')
st.markdown("<h4 style='text-align: center; color: white;'>Flight tracker", unsafe_allow_html=True)


# Contenido


c=st.text_input('Enter your ID and password for the aplication to get access to.', '')


if c != '':
    c=c.lower()
    if c == 'codescodes':
        st.markdown('...')
        time.sleep(3)
        st.success('The conection has been stablished. Redirecting...')
        time.sleep(3)
        switch_page('FT')
    else:
        st.markdown('...')
        time.sleep(3)
        st.error('The conection has not been stablished. Wrong password. Try again.')        




st.text('')
st.text('')
st.text('')
st.text('')
st.text('')
st.text('')