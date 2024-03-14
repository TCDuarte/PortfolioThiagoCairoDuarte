########## LIVRARIAS ##########

import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selectedLanguage = option_menu("Idioma", ["Português", 'English'], 
        # icons=['house', 'gear'], 
        menu_icon="cast", default_index=1)
    
selected2 = option_menu(None, ["Currículo", "Portifólio", "Certificados", "Sobre"], 
    icons=['file-earmark-text', 'clipboard-data', "patch-check", 'info-lg'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

########## CURRÍCULO ##########
if selected2 == 'Currículo':
    st.write('Salve')
    
########## PORTIFÓLIO ##########   
elif selected2 == 'Portifólio':
    st.write('Salve2')
    
########## CERTIFICADOS ##########
elif selected2 == 'Certificados':
    st.write('Salve3')
    
########## SOBRE ##########
else: st.write ('Não salve')