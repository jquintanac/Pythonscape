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
    stoggle('Do you need a hint?', "Import the dict to search the name of the police that contacted to you for a new case.")
    stoggle('Do you need an extra hint?', "Her name is Sarah Q. Lake. Noted her phone number.")

# Titulo

st.markdown("<h1 style='text-align: center; color: blue;'>CODES CITY POLICE DEPARTMENT", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Simple is better than complex", unsafe_allow_html=True)
st.title('')
st.markdown("<h4 style='text-align: center; color: black;'>Agenda", unsafe_allow_html=True)


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


# Contenido

agenda={'Michael Burn': '321-845-698',
        'Jonas K. Rowling': '654-887-329',
        'Alexandra Knockton': '411-035-158',
        'Aeria Windrunner': '647-885-011',
        'Matt Gallner': '021-333-874',
        'Viktor Feroe': '458-999-932',
        'Claire Littleton': '398-774-963',
        'Samantha Miller': '113-800-000',
        'Zoe Wellington': '321-774-859',
        'Kyo Tsunaga': '322-140-841',
        'Abril Green': '409-850-916',
        'Arianna Smaller': '106-843-933',
        'Rea Hayes': '613-078-132',
        'Anna Müller': '460-900-701',
        'Olyvia Vinter': '158-911-034',
        'Drake McLamb': '065-841-369',
        'Sara Paolini': '551-883-997',
        'Alexander Biserov': '197-463-820',
        'Leonard Morningstar': '034-974-621',
        'Sarah J. Purker': '971-301-444',
        'Andrea Scott': '379-801-641',
        'Brooke Amice': '179-011-301',
        'John Terry': '411-888-300',
        'Manuel Erak': '039-975-885',
        'Mara O. Caulfield': '222-874-685',
        'Abigail Collewood': '197-877-310',
        'Khalomer Prince': '136-410-800',
        'Hotaru Black': '777-420-441',
        'Sarah Q. Lake': '215-465-875',
        'Akane A. Hernandez': '169-036-036',
        'Alice Winters': '178-222-351',
        'Nathan Lyne': '130-809-445',
        'Nathaniel J. Holmes': '301-845-633',
        'Lauren Salvatore': '403-877-988',
        'Alexandra Marauder': '411-035-158',
        'Nina Crane': '333-758-885',
        'Michael Wellington': '148-874-111',
        'Gabrielle Vik': '143-032-550',
        "Keith O'Malley": '310-202-808',
        'Max Tyler': '668-820-210',
        'Adam Tomlinson': '340-200-179',
        'Oliver Bloom': '166-952-963',
        'Daniel Davis': '774-874-633',
        'Nellie Bloom': '200-753-951',
        'Jock Buchanan': '175-951-885',
        'Violet Lovelace': '239-887-312',
        'Elisabeth Harmon': '175-800-830',
        'Katherine Halliwell': '409-903-985',
        'Callum Barnes': '555-202-630',
        'Quinn Graham': '660-602-520',
        'Juliet Smith': '103-406-709',
        'Effie McDoughal': '927-120-655',
        'Layton Foster': '458-996-020',
        'Emily Watts': '438-700-903', }


st.code(agenda, language='python')

st.write(agenda)

