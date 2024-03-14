########## LIVRARIAS ##########

import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import requests

with st.sidebar:
    selectedLanguage = option_menu('Idioma', ['Português', 'English'], 
        # icons=['house', 'gear'], 
        menu_icon='cast', default_index=1)
    
selected2 = option_menu(None, ['Currículo', 'Portifólio', 'Certificados', 'Sobre'], 
    icons=['file-earmark-text', 'clipboard-data', 'patch-check', 'info-lg'], 
    menu_icon='cast', default_index=0, orientation='horizontal')


username = 'TCDuarte'
repository_name = 'PortfolioThiagoCairoDuarte'

def get_file_from_github(file_path, pat=None):
  """
  This function retrieves the content of a file from a public GitHub repository using the GitHub API.

  Args:
      username (str): The username of the repository owner.
      repository_name (str): The name of the repository.
      file_path (str): The path to the file within the repository.
      pat (str, optional): A Personal Access Token for authentication (optional for public repos).

  Returns:
      str: The content of the file (decoded from base64), or None if unsuccessful.
  """

  # Build the API URL
  url = f"https://api.github.com/repos/{username}/{repository_name}/contents/{file_path}"

  # Set up authentication if provided
  auth = (username, pat) if pat else None

  # Send the request
  response = requests.get(url, auth=auth)

  # Check for successful response
  if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Access and decode the file content
    return data["content"].encode("utf-8").decode("base64")
  else:
    print(f"Error: {response.status_code}")
    return None





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