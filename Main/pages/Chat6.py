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

def add_bg_from_url():    st.markdown(         f"""         <style>         .stApp {{             background-image: url("https://github.com/jquintanac/Pythonscape/blob/main/imgs/background2.jpg?raw=true");             background-attachment: fixed;             background-size: cover         }}         </style>         """,         unsafe_allow_html=True     )

add_bg_from_url() 

#Sidebar: Ocultar nombres sidebar y login

no_sidebar_style = """    <style>        div[data-testid="stSidebarNav"] {display: none;}    </style>"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imgs/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')
with st.sidebar:
    st.title('Hints')
    stoggle('Do you need a hint?', "You work at Codes. Twice 'Codes' without a space in between is...")
    stoggle('Do you need an extra hint?', "You have the departure city and the first letter of the arrival. You have enough information to start tracking the flights")

# Titulo


st.title('')
st.markdown("<h4 style='text-align: center; color: white;'>Chat", unsafe_allow_html=True)


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

st.markdown("  ")
st.markdown('<div style="text-align: justify;"> I have been searching through the hacker"s computer and I found something really important: his boarding pass! We have him, buddy! I am sending to you the boarding pass. It has some printing issues but I think we can work with this information. I am going to ask for the house images when he left it. Give me a minute.</div>', unsafe_allow_html=True)

time.sleep(5)

st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/boardingpass.jpg?raw=true')

time.sleep(10)

st.markdown("  ")
st.markdown('<div style="text-align: justify;"> Police service has informed to me that we know more about Ethan. He left his home on 20th November 2022 to take a flight at Codes City airport. We caught him by street cameras. Look!</div>', unsafe_allow_html=True)

time.sleep(2)

st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/camera.jpg?raw=true')

time.sleep(2)

st.markdown("  ")
st.markdown("We have no time to ask for a permission to track the airports information. Why don't you check your flight program in the desktop? Remember that your password is the name of our city twice with no space!")

st.info('If you want to come back to this page, go to programs in your desktop and enter the correct pass in "Flight investigator". You will find a redirect button there. Be sure what the password is before leaving the page! ')





