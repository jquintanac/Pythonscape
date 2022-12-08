import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stoggle import stoggle

#Sidebar: Ocultar nombres sidebar
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')


# Titulo

st.markdown("<h1 style='text-align: center; color: blue;'>CODES CITY POLICE DEPARTMENT", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Simple is better than complex", unsafe_allow_html=True)
st.title('')
st.markdown("<h4 style='text-align: center; color: black;'>Chat", unsafe_allow_html=True)
with st.sidebar:
    st.title('Hints')
    stoggle('Do you need a hint?', "Do you have multiplied bot matrixes? If not, then do it!")
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

st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/keyboard.jpg?raw=true',use_column_width=True) 

c=st.text_input('Write the numbers separated by a comma. The code for the door lock is:', '')

if c != '':
    if re.search('\d{1},\d{1},\d{1},\d{1}', c):

        if c == '5,6,8,9':
            time.sleep(2)
            st.text('...')
            time.sleep(2)               
            st.text('It worked! I go inside')
            time.sleep(4)
            switch_page('Chat3')

        else:
            time.sleep(2)
            st.text('...')
            time.sleep(2)               
            st.text('Mec mec, door is closed yet. Try again, buddy.')

    else:
        time.sleep(2)
        st.text("I can't enter that as a code, buddy! Be serious!")    