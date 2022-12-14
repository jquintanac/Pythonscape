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

st.markdown("<h5 style='text-align: center; color: white;'>Welcome to the Codes City Police Service. Please, login with the correct ID and your password below.", unsafe_allow_html=True)


#Fondo

def add_bg_from_url():    st.markdown(         f"""         <style>         .stApp {{             background-image: url("https://github.com/jquintanac/Pythonscape/blob/main/imgs/background2.jpg?raw=true");             background-attachment: fixed;             background-size: cover         }}         </style>         """,         unsafe_allow_html=True     )

add_bg_from_url() 


#Sidebar: Ocultar nombres sidebar
no_sidebar_style = """    <style>        div[data-testid="stSidebarNav"] {display: none;}    </style>"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imgs/logo.png?raw=true", use_column_width=True)
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