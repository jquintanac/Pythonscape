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
with st.sidebar:
    st.title('Hints')
    stoggle('Do you need a hint?', "It seems that the doormat contains some numbers and they are perfectly placed, don't they?")
    stoggle('Do you need an extra hint?', "Numbers are placed as matrixes so you have to operate with both. Is the result familiar?")



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
        switch_page('Chat')

with col3:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')




# Chat



st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/doorhacker.png?raw=true',use_column_width=True)



b=st.text_input('Sarah should check the mailbox, doormat or door lock?', '')
if b != '':
    b= b.lower()
    if b == 'mailbox':
        time.sleep(2)
        st.text('...')
        time.sleep(2)
        st.markdown('Just magazines, advertisement... No letters to check the hacker data. Sh*t!')

    elif b == 'doormat':
        time.sleep(2)
        st.text('...')
        time.sleep(2)
        st.markdown('Nothing on the floor, under de doormat. Either over it. But...')
        time.sleep(2)
        st.text('...')
        time.sleep(2) 
        st.markdown('Oh wait! There is something written in the doormat back. Maybe letters, numbers? What do you think?. Let me send you a picture of it') 
        time.sleep(2)
        st.text('...')
        time.sleep(4)
        st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/doormat.jpg?raw=true',use_column_width=True)   

    elif b == 'door lock':
        time.sleep(2)
        st.text('...')
        time.sleep(2)               
        st.markdown('I send you a picture of the keyboard. Just the ten numbers, pad and asterisk. I need your help to search the code to pass inside. Any idea?')
        time.sleep(4)
        st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/keyboard.jpg?raw=true',use_column_width=True) 
        time.sleep(2)
        st.markdown('If you do not know the code, keep investigating. If you know it, just give a moment to Sarah to get prepared.')
        time.sleep(10)
        switch_page('Chat2')


    else:
        time.sleep(2)
        st.text('...')
        time.sleep(2)               
        st.markdown("I don't think that would be interesting to check")    



    











