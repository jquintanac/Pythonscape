#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import regex as re
import time
import random
from PIL import Image
from streamlit_extras.switch_page_button import switch_page


# Cabecera

st.markdown("<h1 style='text-align: center; color: blue;'>CODES CITY POLICE DEPARTMENT", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Simple is better than complex", unsafe_allow_html=True)
st.title('')

st.markdown('Welcome to the Codes City Police Service. Please, login with the correct ID and your password below.')


# Inicio de sesión



a=st.text_input('ID', '')

if a != '':
    if a=='381455':
        st.text('Correct ID. Welcome back James!')
        b=st.text_input('Password', '')
        if b != '':
            if b== '2400':
                st.text('Correct password. Access allowed.')
            else:
                st.text('Wrong password. Try again!')           
    elif a=='641228':
        st.text('Correct ID. Welcome back Scarlett!')
        b=st.text_input('Password', '')
        if b != '':
            if b== '768':
                st.text('Correct password. Access allowed.')
                st.button('Continue',on_click=switch_page('desktop'))
            else:
                st.text('Wrong password. Try again!')           
    else:
        st.text('Wrong ID. Try again!')

# %%
