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
with st.sidebar:
    st.title('Hints')
    stoggle('Do you need a hint?', "The date you are looking for is in the boarding pass.")
    stoggle('Do you need an extra hint?', "The city you are looking for is which the hacker is from.")


# Titulo

st.markdown("<h1 style='text-align: center; color: blue;'>CODES CITY POLICE DEPARTMENT", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Simple is better than complex", unsafe_allow_html=True)
st.title('')
st.markdown("<h4 style='text-align: center; color: black;'>Flight tracker application", unsafe_allow_html=True)


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





