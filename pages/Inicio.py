import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page


# Cabecera

st.markdown("<h1 style='text-align: center; color: blue;'>CODES CITY POLICE DEPARTMENT", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Simple is better than complex", unsafe_allow_html=True)
st.title('')

st.markdown('Welcome to the Codes City Police Service. Please, login with the correct ID and your password below.')

#Sidebar: Ocultar nombres sidebar
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')

# Inicio de sesión

a=st.text_input('ID', '')

if a != '':
    if a=='381455':
        st.markdown('Correct ID. Welcome back James!')
        b=st.text_input('Password', '')
        if b != '':
            if b== '2400':
                st.markdown('Correct password. Access allowed.')
                boton=st.button('Continue to desktop')
                if boton:
                    switch_page("desktopJ")                
            else:
                st.text('Wrong password. Try again!')           
    elif a=='641228':
        st.markdown('Correct ID. Welcome back Scarlett!')
        b=st.text_input('Password', '')
        if b != '':
            if b== '768':
                st.markdown('Correct password. Access allowed.')
                boton=st.button('Continue to desktop')
                if boton:
                    switch_page("desktopS")
            else:
                st.markdown('Wrong password. Try again!')           
    else:
        st.markdown('Wrong ID. Try again!')