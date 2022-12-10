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
with st.sidebar:
    st.title('Hints')
    stoggle('Do you need a hint?', "It seems that the doormat contains some numbers and they are perfectly placed, don't they?")
    stoggle('Do you need an extra hint?', "Numbers are placed as matrixes so you have to operate with both. Is the result familiar?")



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
        switch_page('Chat')

with col3:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')




# Chat



st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/doorhacker.png?raw=true',use_column_width=True)



b=st.text_input('Sarah should check the mailbox, doormat or door lock?', '')
if b != '':

    if b == 'mailbox':
        time.sleep(2)
        st.text('...')
        time.sleep(2)
        st.text('Just magazines, advertisement... No letters to check the hacker data. Sh*t!')

    elif b == 'doormat':
        time.sleep(2)
        st.text('...')
        time.sleep(2)
        st.text('Nothing on the floor, under de doormat. Either over it. But...')
        time.sleep(2)
        st.text('...')
        time.sleep(2) 
        st.text('Oh wait! There is something written in the doormat back. Maybe letters, numbers? What do you think?. Let me send you a picture of it') 
        time.sleep(2)
        st.text('...')
        time.sleep(4)
        st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/doormat.jpg?raw=true',use_column_width=True)   

    elif b == 'door lock':
        time.sleep(2)
        st.text('...')
        time.sleep(2)               
        st.text('I send you a picture of the keyboard. Just the ten numbers, pad and asterisk. I need your help to search the code to pass inside. Any idea?')
        time.sleep(4)
        st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/keyboard.jpg?raw=true',use_column_width=True) 
        time.sleep(2)
        st.text('If you do not know the code, keep investigating. If you know it, just give a moment to Sarah to get prepared.')
        time.sleep(10)
        switch_page('Chat2')


    else:
        time.sleep(2)
        st.text('...')
        time.sleep(2)               
        st.text("I don't think that would be interesting to check")    



    










