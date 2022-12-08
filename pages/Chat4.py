import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain

#Sidebar: Ocultar nombres sidebar
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')
with st.sidebar:
    st.title('Hints')
    stoggle('Do you need a hint?', "")
    stoggle('Do you need an extra hint?', "")

# Titulo

st.markdown("<h1 style='text-align: center; color: blue;'>CODES CITY POLICE DEPARTMENT", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Simple is better than complex", unsafe_allow_html=True)
st.title('')
st.markdown("<h4 style='text-align: center; color: black;'>Chat", unsafe_allow_html=True)


# Botones para volver


col1, col2, col3 = st.columns([1,1,1])

with col1:
    boton=st.button('Back to James desktop')
    if boton:
        switch_page('desktopJ')

with col2:
    boton=st.button('Previous chat')
    if boton:
        switch_page('Chat3')

with col3:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')

st.success('Conexion stablished remotely.')


# Contenido


st.markdown('I share the screen for you but I do not understand anything. Why are there graphics in the main page? Maybe it is an access control?')

