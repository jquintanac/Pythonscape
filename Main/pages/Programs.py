import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

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
st.markdown("<h4 style='text-align: center; color: white;'>Programs", unsafe_allow_html=True)





# Contenido

st.text('')

st.text('')

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/peoplef.png?raw=true')
    boton=st.button('People finder')
    if boton:
        switch_page('peoplef')

with col2:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/flight.png?raw=true')
    boton=st.button('Flight tracker')
    if boton:
        switch_page('flighttracker')

with col3:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/logocar.png?raw=true')
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