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

def add_bg_from_url():    st.markdown(         f"""         <style>         .stApp {{             background-image: url("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/background2.jpg?raw=true");             background-attachment: fixed;             background-size: cover         }}         </style>         """,         unsafe_allow_html=True     )

add_bg_from_url() 

#Sidebar: Ocultar nombres sidebar y login

no_sidebar_style = """    <style>        div[data-testid="stSidebarNav"] {display: none;}    </style>"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')
with st.sidebar:
    st.title('Hints')
    stoggle('Do you need a hint?', "Keep in mind the three bases and use a conditional to limit the flights from one hour since he arrives.")
    stoggle('Do you need an extra hint?', "Ethan visited five cities, counting Codes as a city, so the final code will contain 4 codes separated by '-'.")

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
        switch_page('FT')

with col3:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')


# Contenido


st.text('')

st.markdown("Buddy, I need you to do your thing. Check the flights tracking to find out the hacker whereabouts. Keep in mind three things:")
st.markdown("• The hacker will take all the flights he can to mislead us, starting in Codes City.")
st.markdown("• He will never comeback to a city he has already been during his travelling.")
st.markdown("• The waiting time between two flights has to be a maximum of one hour but never at the same time as the arrival time. He doesn't want to stay too much time in the airport.")

st.text('')

st.info("Try to track the flights in a SQL platform and add the content to your notebook. But you can do it as you want!")

st.text('')

c=st.text_input("Write the codes for each flight and put them down in order and separated by '-'", '')

if c != '':

    if c == '9B6IN-GJG79-MYZ1H-OSYAO':
        time.sleep(2)
        st.markdown('...')
        time.sleep(2)               
        st.markdown('Oh buddy. I think you are right! I will contact immediately with the Tokyo police department to start the searching. We dit it, buddy! Good job!')
        time.sleep(10)
        switch_page('Final')

    else:
        time.sleep(2)
        st.markdown('...')
        time.sleep(2)               
        st.markdown("Did you write the correct code? I don't think so, buddy. Check it and write again!")


