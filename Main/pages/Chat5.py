import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain
import matplotlib.pyplot as plt
import pandas as pd

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
    stoggle('Do you need a hint?', "Try to web scrapping the pages with the XPaths and find the keys.")
    stoggle('Do you need an extra hint?', "The first is what you need to get the final key 😉")

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
        switch_page('Chat4')

with col3:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')

st.success('Conexion stablished remotely.')

# Contenido

st.markdown("We are in the hacker's computer, buddy! Good job. Oh, it seems he or she was hurry. The browsing history is open. Let's check what he or she was looking for... The screen is sending to your computer. ")


links=[
'https://www.reddit.com/topics/r-1/',
'https://es.investing.com/crypto/',
'https://www.nytimes.com/topic/organization/wikileaks',
'https://github.com/topics/web-hacking',
'https://en.wikipedia.org/wiki/Elon_Musk ',
'https://www.fbi.gov/investigate/cyber',
'https://ktflash.gitbooks.io/ceh_v9/content/62_trojan_concepts.html'
]

st.code(links)



st.markdown("We have to investigate these links. There are no more links, so werid, don't you think? Oh, yes, I found a note with something strange written on it. I will use the mobile text reader and I will send you the text, give me a minute.")



st.image('https://github.com/jquintanac/Pythonscape/blob/main/imgs/note.jpg?raw=true',use_column_width=True)



xpaths=[
'//*[@id="Tesla"]',
'//*[@id="collection-WikiLeaks"]/header/div/div[2]/div/div/h1',
'//*[@id="main-content"]/div/div[4]/div[2]/div[3]/div/p[1]/span/strong/a',
'//*[@id="DataTables_Table_0"]/tbody/tr[3]/td[3]/a',
'//*[@id="what-is-a-trojan"]/span',
'/html/body/div[1]/div[5]/main/div[2]/div[2]/div/div[1]/article[39]/div[1]/div/div[1]/h3/a[1]',
'/html/body/div[2]/div[1]/div[2]/div[469]/a']

st.code(xpaths)


c=st.text_input("What do you think she or he is looking for? I think something of these keys are conected somehow.", '')

if c != '':
    c= c.lower()
    if c == 'twitter':
        time.sleep(3)
        st.markdown("Oh, it's a possibility, of course. Elon Musk, hacking, cryptocurrency. Something is going to happen with Twitter. We have to stop it!")
        time.sleep(5)               
        switch_page('Chat6')
    else:
        time.sleep(2)
        st.markdown("I don't see the connection, buddy. I think is another thing we are missing. Think, Sarah, think, buddy!")















