########## LIVRARIAS ##########

import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Idioma", ["Português", 'English'], 
        # icons=['house', 'gear'], 
        menu_icon="cast", default_index=1)
    
selected2 = option_menu(None, ["Currículo", "Portifólio", "Certificados", "Sobre"], 
    # icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")



# var = str(selected2)
# st.write(var)

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