import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Linguagem", ["Português", 'English'], 
        # icons=['house', 'gear'], 
        menu_icon="cast", default_index=1)
    selected
    
print (selected)