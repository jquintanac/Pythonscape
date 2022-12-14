import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain

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
with st.sidebar:
    st.title('Hints')
    stoggle('Do you need a hint?', "Try to figure out the pattern in the string, just a few letters are in it, right? Which ones?")
    stoggle('Do you need an extra hint?', "The count not only set how many letters of each are...😋 ")

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
        switch_page('Chat2')

with col3:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')


# Contenido


alarm=st.empty()
with alarm.container():
    rain(
        emoji="🚨",
        font_size=54,
        falling_speed=5,
        animation_length='infinite')

st.markdown('')
st.markdown('Buddy, we have a problem here. An alarm has been switched on and probably the hacker now know we are here. I am going to try to stablish a conexion with you and the hacker operative system. This way you can help me as if you were here. Give me a minute...')
time.sleep(3)
conex=st.empty()
conex.error('The conexion has not been stablished.')

off=st.empty()

st.markdown('The CPU is throwing a huge weird message. I write it for you. It must be on your computer now.')
time.sleep(3)
st.code('lpaildrfnitfehdaluifsluedourlsiatffyuehlrdauiaseffnloriusrelhuraoldnueustaoreulylfsreduunrolaefuifldesnhuradfedlrfnefsal')

c=off.text_input('Conexion with the SO, enter the code lowcase with spaces:', '')

if c != '':
    c= c.lower()
    if c == 'python is dareful':
        with alarm.container():
            rain(
            emoji="🚨",
            font_size=54,
            falling_speed=5,
            animation_length=0)
        conex.success('The conexion has been stablished.')
        st.warning('Alarm sound off. Security mode activated as a caution tool.')
        st.markdown('Nice, buddy. We are conected to the hacker computer. Let me see where we can start.')
        time.sleep(10)
        switch_page('Chat4')
    else:
        st.text('Wrong code, I think. Try again.')









#


# Alarma on/off









