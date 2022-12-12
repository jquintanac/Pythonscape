import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from streamlit_extras.stoggle import stoggle

#Sidebar: Ocultar nombres sidebar
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')


# Titulo

st.markdown("<h1 style='text-align: center; color: blue;'>CODES CITY POLICE DEPARTMENT", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Simple is better than complex", unsafe_allow_html=True)
st.title('')
st.markdown("<h4 style='text-align: center; color: black;'>Flight tracker", unsafe_allow_html=True)


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