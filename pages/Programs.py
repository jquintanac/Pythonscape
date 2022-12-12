import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

#Sidebar: Ocultar nombres sidebar
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')


# Titulo

st.markdown("<h1 style='text-align: center; color: blue;'>CODES CITY POLICE DEPARTMENT", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Simple is better than complex", unsafe_allow_html=True)
st.title('')
st.markdown("<h4 style='text-align: center; color: black;'>Programs", unsafe_allow_html=True)





# Contenido

st.text('')

st.text('')

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/peoplefinder.png?raw=true')
    boton=st.button('People finder')
    if boton:
        switch_page('peoplef')

with col2:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/714942.png?raw=true')
    boton=st.button('Flight tracker')
    if boton:
        switch_page('flighttracker')

with col3:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/findercar.png?raw=true')
    boton=st.button('Car finder')
    if boton:
        switch_page('carfinder')



# Botones para volver

st.text('')

st.text('')

st.text('')

st.text('')

st.text('')

st.text('')

st.text('')

st.text('')
col1, col3, col2 = st.columns([1,1,1])

with col1:
    boton=st.button('Back to James desktop')
    if boton:
        switch_page('desktopJ')

with col2:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')