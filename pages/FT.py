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
with st.sidebar:
    st.title('Hints')
    stoggle('Do you need a hint?', "The date you are looking for is in the boarding pass.")
    stoggle('Do you need an extra hint?', "The city you are looking for is which the hacker is from.")


# Titulo


st.title('')
st.markdown("<h4 style='text-align: center; color: white;'>Flight tracker application", unsafe_allow_html=True)


# Botones para volver


col1, col2, col3 = st.columns([1,1,1])

with col1:
    boton=st.button('Back to James desktop')
    if boton:
        switch_page('desktopJ')

with col2:
    boton=st.button('Previous chat')
    if boton:
        switch_page('Chat6')

with col3:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')

st.success('Conexion stablished remotely.')


# Contenido

c=st.text_input('Enter the date you want to check as YYYY-MM-DD.', '')


if c != '':

    if c == '2022-11-20':
        st.markdown('...')
        time.sleep(3)
        d=st.text_input('Enter the name of the city to check the flights and scales availables.', '')
        if d != '':
            d=d.lower()
            if d == 'codes':
                time.sleep(2)
                with open("../codesflightsandscales.rar", "rb") as file:
                    btn = st.download_button(
                            label='Codes flights and scales',
                            data=file,
                            file_name="codesflightsandscales.rar",
                            )
                st.markdown("Let's go back to the chat with Sarah to work together.")
                boton=st.button('Chat with Sarah')
                if boton:
                    switch_page('Chat7')
            else:
                st.error('Flights not available to track or wrong input. Please, check your query.')

    else:
        st.markdown('...')
        time.sleep(3)
        st.error('Date not available to track or wrong input. Please, check your query.')        





