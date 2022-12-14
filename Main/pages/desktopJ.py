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
st.text('')
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imgs/james.png?raw=true")
st.sidebar.markdown('Your ID: 381455')
st.sidebar.markdown('Your mail: js@ccpd.com')
st.sidebar.markdown('Your phone number: 455-887-212')
boton=st.sidebar.button('Log off')
if boton:
    switch_page("Main")

# Titulo


st.markdown("<h4 style='text-align: center; color: white;'>Desktop", unsafe_allow_html=True)

# Funciones escritorio

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/schedule.png?raw=true', width=170)
    schedule=st.button('Schedule')
    if schedule:
        switch_page("Schedule")    
with col2:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/mail.png?raw=true', width=170)
    mail=st.button('Mail')
    if mail:
        switch_page("Mail") 
with col3:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/files.png?raw=true', width=170)
    files=st.button('Files')
    if files:
        switch_page("Files") 

col4, col5, col6 = st.columns([1,1,1])

with col4:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/pc.png?raw=true', width=170)
    programs=st.button('Programs')
    if programs:
        switch_page("Programs")    
with col5:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/chat.png?raw=true', width=170)
    chat=st.button('Chat')
    if chat:
        switch_page("Chat") 
with col6:
    st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/agenda.png?raw=true', width=170)
    agenda=st.button('Agenda')
    if agenda:
        switch_page("Agenda") 