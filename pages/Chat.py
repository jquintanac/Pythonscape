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
    stoggle('Do you need a hint?', "You need the phone number of the police that contacted to you recently for a new case.")
    stoggle('Do you need an extra hint?', "You have to put the Sara Q. Lake number and phone her.")

# Titulo

st.markdown("<h1 style='text-align: center; color: blue;'>CODES CITY POLICE DEPARTMENT", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Simple is better than complex", unsafe_allow_html=True)
st.title('')
st.markdown("<h4 style='text-align: center; color: black;'>Chat", unsafe_allow_html=True)


# Botones para volver


col1, col3, col2 = st.columns([1,1,1])

with col1:
    boton=st.button('Back to James desktop')
    if boton:
        switch_page('desktopJ')

with col2:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')


#Chat

st.markdown("<h5 style='text-align: center; color: black;'>Welcome to the Codes City Police Chat Service. Please, enter a correct phone number to conect with.", unsafe_allow_html=True)

a=st.text_input('Phone number to conect', '')
llamada=['The number you have dialed is not in service at this time. Please, check the number and try to call again.', "It's Pam. Who's calling? Hello?", "I'm not interested in buying anything. Bye."]

if a != '':
    if re.search('\w{3}-\w{3}-\w{3}', a):

        if a=='215-465-875':
            time.sleep(2)
            st.text('Trying to conect')
            time.sleep(5)
            st.text("Hey buddy. What' up? Sarah here. Give me a second...")
            time.sleep(5)
            st.text('I am here, buddy. I am in front of the hacker house. Nobody is inside, police confirmed to me before so... there I go.')
            time.sleep(2)
            st.text('...')
            time.sleep(2)           
            st.text('The door is locked and it has a security keyboard to go in. No keys. What more do I see... The mailbox is open and... well, the doormat is too new and big for the door, I think. I send you a picture.')
            time.sleep(4)
            st.image('https://github.com/jquintanac/Pythonscape/blob/main/imagenes/doorhacker.png?raw=true',use_column_width=True)
            time.sleep(2)
            st.text('...')
            time.sleep(2)
            st.text('What should do Sarah')           
            time.sleep(7)
            switch_page('Chat1')

        elif a== '455-887-212':
            time.sleep(2)
            st.text('Trying to conect')
            time.sleep(2)
            st.text('...')
            time.sleep(3)
            st.text("Impossible to conect with yourself. Try again!")

        else:
            time.sleep(2)
            st.text('Trying to conect')
            time.sleep(5)
            st.text('...')
            time.sleep(2)
            st.text(random.choice(llamada)) 
            time.sleep(2)
            st.text('The phone was hung up')       

    else:
        st.text('The providen number is not correct. Please, write a correct one.')









