import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.image_in_tables import table_with_images
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

def add_bg_from_url():    st.markdown(         f"""         <style>         .stApp {{             background-image: url("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/background2.jpg?raw=true");             background-attachment: fixed;             background-size: cover         }}         </style>         """,         unsafe_allow_html=True     )

add_bg_from_url() 

#Sidebar: Ocultar nombres sidebar y login

no_sidebar_style = """    <style>        div[data-testid="stSidebarNav"] {display: none;}    </style>"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
st.sidebar.image("https://github.com/jquintanac/Pythonscape/blob/main/imagenes/logo.png?raw=true", use_column_width=True)
st.sidebar.markdown('Welcome to the Codes City Police Service')


# Titulo


st.title('')
st.markdown("<h4 style='text-align: center; color: white;'>Files", unsafe_allow_html=True)



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
data= [
['Documentation case 1254B','2022-11-18','https://github.com/jquintanac/Pythonscape/blob/main/imagenes/pdf.png?raw=true'],
['Speed limit record 5542X','2022-11-15','https://github.com/jquintanac/Pythonscape/blob/main/imagenes/video.png?raw=true'],
['Thief caption 5433B','2022-11-15','https://github.com/jquintanac/Pythonscape/blob/main/imagenes/jpeg.png?raw=true'],
['Identification Marga D. Bell 1147P','2022-11-13','https://github.com/jquintanac/Pythonscape/blob/main/imagenes/pdf.png?raw=true'],
['Identification Matthew Prats 1147P','2022-11-13','https://github.com/jquintanac/Pythonscape/blob/main/imagenes/pdf.png?raw=true'],
['Market robbery 4497I','2022-11-05','https://github.com/jquintanac/Pythonscape/blob/main/imagenes/video.png?raw=true'],
['Suspects st Madisson 13 9400O','2022-11-02','https://github.com/jquintanac/Pythonscape/blob/main/imagenes/jpeg.png?raw=true'],
['...','...','...']]
df = pd.DataFrame(data, columns=['File name', 'Date', 'Download'])



df_html = table_with_images(df=df, url_columns=("Download",))

st.markdown(df_html, unsafe_allow_html=True)











