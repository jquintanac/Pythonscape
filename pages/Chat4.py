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

#Sidebar: Ocultar nombres sidebar
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')
with st.sidebar:
    st.title('Hints')
    stoggle('Do you need a hint?', "It seems that the dataframe given is for 10 x-axis and 10 y-axis, don't you think?")
    stoggle('Do you need an extra hint?', "You should see clairly a few letters to sort as a word. Check you have your axis from 0 to 5 as the Hi! figure.")

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
        switch_page('Chat3')

with col3:
    boton=st.button('Back to Scarlett desktop')
    if boton:
        switch_page('desktopS')

st.success('Conexion stablished remotely.')


# Encabezado


st.text('')
st.markdown('I share the screen for you but I think the hacker knows we are here. Take a look... Maybe is it an access control? The page is blocked and I can not give you access to the desktop.')


#Scatter hi!

x=[1.8,1.8,1.8,1.8,2.2,2.2,2.2,2.2,2,2,2.6,2.6,2.6,2.6,3.1,3.1,3.1,3.1,3.1,3.1]
y=[1.5,2,2.5,3,1.5,2,2.5,3,2.1,2.2,1.5,2,2.5,3,1.5,3,2.8,2.6,2.4,2.2]

df=pd.DataFrame(columns=['x','y'])
df['x']=x
df['y']=y

fig = plt.figure(figsize=(4.5,2))
plt.ylim(0,5)
plt.xlim(0,5)

plt.scatter(df['x'],df['y'])

st.write(fig)

st.markdown("<h1 style='text-align: center; color: black;'>Do you dare? 😶", unsafe_allow_html=True)
acceso=st.empty()
acceso.error('🔐 Restringed access 🔐  ⛔ Unauthorized permission  ⛔  ')

df=pd.read_csv('../scatter.csv')
st.code(df)

c=st.text_input("Are you trying to access to my computer? Let's see what you are able to!", '')

if c != '':
    c= c.lower()
    if c == 'peace':
        time.sleep(2)
        st.text('...')
        time.sleep(3)               
        st.text('Permitted access. Welcome back, master.')
        acceso.success('🔒 Permitted access 🔒  🆗 Authorized permission  🆗  ')
        time.sleep(6)
        switch_page('Chat5')
    else:
        time.sleep(2)
        st.text('...')
        time.sleep(3)               
        st.text('ERROR. F*ck... You can do it better, buddy. Any idea?')
        rain(
            emoji="🤣",
            font_size=54,
            falling_speed=8,
            animation_length=0.5)
