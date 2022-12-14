import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
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

def add_bg_from_url():    st.markdown(         f"""         <style>         .stApp {{             background-image: url("https://github.com/jquintanac/Pythonscape/blob/main/imgs/background2.jpg?raw=true");             background-attachment: fixed;             background-size: cover         }}         </style>         """,         unsafe_allow_html=True     )

add_bg_from_url() 

#Sidebar: Ocultar nombres sidebar y login

no_sidebar_style = """    <style>        div[data-testid="stSidebarNav"] {display: none;}    </style>"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imgs/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')


# Titulo


st.title('')
st.markdown("<h4 style='text-align: center; color: white;'>Chat", unsafe_allow_html=True)
with st.sidebar:
    st.title('Hints')
    stoggle('Do you need a hint?', "Do you have multiplied both matrixes? If not, then do it!")
    stoggle('Do you need an extra hint?', "What numbers are not matching with the pattern?")


# Botones para volver


col1, col2, col3 = st.columns([1,1,1])

with col1:
    boton=st.button('Back to James desktop')
    if boton:
        switch_page('desktopJ')

with col2:
    boton=st.button('Previous chat')
    if boton:
        switch_page('Chat1')

with col3:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')



#Codigo

st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/keyboard.jpg?raw=true',use_column_width=True) 

c=st.text_input('Write the numbers separated by a comma. The code for the door lock is:', '')

if c != '':
    if re.search('\d{1},\d{1},\d{1},\d{1}', c):

        if c == '5,6,8,9':
            time.sleep(2)
            st.text('...')
            time.sleep(2)               
            st.markdown('It has worked! I go inside.')
            time.sleep(4)
            switch_page('Chat3')

        else:
            time.sleep(2)
            st.text('...')
            time.sleep(2)               
            st.markdown('Mec mec, door is closed yet. Try again, buddy.')

    else:
        time.sleep(2)
        st.markdown("I can't enter that as a code, buddy! Be serious!")    