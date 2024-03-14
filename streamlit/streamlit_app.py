import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Idioma", ["Português", 'English'], 
        # icons=['house', 'gear'], 
        menu_icon="cast", default_index=1)
    
selected2 = option_menu(None, ["Currículo", "Portifólio", "Certificados", "Sobre"], 
    # icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    on_change = st.write(1))

var = str(selected2)
st.write(var)
if var == 'Currículo':
    print('Salve')
else: print ('Não salve')