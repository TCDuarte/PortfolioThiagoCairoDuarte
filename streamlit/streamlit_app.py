########## LIVRARIAS ##########

import streamlit as st
from streamlit_option_menu import option_menu
import requests
import base64

########## DECLARAÇÃO DAS VARIÁVEIS CHAVES ##########

username = 'TCDuarte'
repository_name = 'PortfolioThiagoCairoDuarte'

########## DECLARAÇÃO DAS FUNÇÕES ##########

def get_file_from_github(file_path):
  """
  Função para abrir os arquivos de texto do repositório.
  Com o objetivo de não sobrecarregar o código com textos, os mesmos foram salvos dentro do repositório.
  Por se tratar de um repositório público, não necessita de uma etapa de autenticação.

  Argumentos:
      file_path (str): Caminho para o arquivo.

  Returns:
      str: Texto contido dentro do arquivo.
  """
  language = 'EN' if selectedLanguage == 'English' else 'PT'
  # URL da API baseada nos demais parâmetros
  url = f"https://api.github.com/repos/{username}/{repository_name}/contents/streamlit/texts/{language}/{file_path}"
  # Request
  response = requests.get(url)

  # Checa se a request obteve sucesso
  if response.status_code == 200:
    data = response.json()
    
    # Decodificação do arquivo em texto
    file_content = base64.b64decode(data["content"]).decode("utf-8")
    return file_content
  else:
    print(f"Error: {response.status_code}")
    return None

########## CONFIGURAÇÃO DO STREAMLIT ##########

with st.sidebar:
    img = 'IMG'
    selectedLanguage = option_menu('Idioma', ['Português', 'English'],
        menu_icon='cast', default_index=1)
    
selected2 = option_menu(None, ['Currículo', 'Portifólio', 'Certificados', 'Sobre'], 
    icons=['file-earmark-text', 'clipboard-data', 'patch-check', 'info-lg'], 
    menu_icon='cast', default_index=0, orientation='horizontal')

########## ABA - CURRÍCULO ##########
if selected2 == 'Currículo':
    cv = get_file_from_github(r'cv.txt')
    st.write(f"{cv}")
    
########## ABA - PORTIFÓLIO ##########   
elif selected2 == 'Portifólio':
    st.write('Salve2')
    
########## ABA - CERTIFICADOS ##########
elif selected2 == 'Certificados':
    st.write('Salve3')

########## ABA - SOBRE ##########
else: st.write ('Não salve')