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

#Sidebar: Ocultar nombres sidebar
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')
with st.sidebar:
    st.title('Hints')
    stoggle('Do you need a hint?', "You work at Codes. Twice 'Codes' without a space in between is...")
    stoggle('Do you need an extra hint?', "You have the departure city and the first letter of the arrival. You have enough information to start tracking the flights")

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
        switch_page('Chat5')

with col3:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')

st.success('Conexion stablished remotely.')

# Contenido

st.markdown("I've been searching through the hacker's computer and I found something really important: his boardpass! We have him, buddy! I am sending you the boardpass. It has some printing issues but I think we can work with this information. I'm going to ask for the house images when he left it. Give me a minute.  ")

time.sleep(5)

st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/boardingpass.jpg?raw=true')

time.sleep(10)

st.markdown("Police service has informed to me that we know more about Ethan. He left his home on 20th November 2022 to take a flight at Codes City airport. We caught him by street cameras. Look!  ")

time.sleep(2)

st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/ethanpics.jpg?raw=true')

time.sleep(2)

st.markdown("We have no time to ask for a permission to track the airports information. Why don't you check your flight program in the desktop? Remember that your password is the name of our city twice with no space!")

st.info('If you want to come back to this page, go to programs in your desktop and enter the correct pass in "Flight investigator". You will find a redirect button there. Be sure what the password is before leaving the page! ')





