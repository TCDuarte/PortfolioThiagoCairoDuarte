########## LIVRARIAS ##########

import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.card import card
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
  st.write(response.status_code)
  # Checa se a request obteve sucesso
  if response.status_code == 200:
    data = response.json()
    
    # Decodificação do arquivo em texto
    file_content = base64.b64decode(data["content"]).decode("utf-8")
    return file_content
  else:
    print(f"Error: {response.status_code}")
    return None

def stringToList(serie):
    finalList = []
    for x in serie:
        if x.count(';') > 0:
            valueList = x.split('; ')
            finalList.append(valueList)
        else:
            finalList.append([x])
    return finalList

########## CONFIGURAÇÃO DO STREAMLIT ##########
st.set_page_config(layout = 'wide')
with st.sidebar:
    st.image('https://github.com/TCDuarte/PortfolioThiagoCairoDuarte/blob/main/streamlit/imgs/profile.png?raw=true',
             use_column_width = 'auto')
    st.write(f'**Thiago Cairo Duarte**')
    st.write('15 99771-7474')
    st.write('thiago.cairo.duarte@gmail.com')
    st.write('https://www.linkedin.com/in/tcduarte/')
    selectedLanguage = option_menu('Idioma', ['Português', 'English'],
        menu_icon='cast', default_index=0)
    
options = ['Currículo', 'Portifólio', 'Certificados', 'Sobre'] if selectedLanguage == 'Português' else ['Curriculum', 'Portfolio', 'Certificates', 'About']

selected2 = option_menu(None, 
                        options, 
                        icons=['file-earmark-text', 'clipboard-data', 'patch-check', 'info-lg'], 
                        menu_icon='cast', default_index=0, orientation='horizontal')

title = str(selected2) if selected2 != options[0] else 'Thiago Cairo Duarte'
st.header(str(title))
st.divider()
########## ABA - CURRÍCULO ##########
if selected2 == options[0]:
    cv = get_file_from_github(r'cv.txt')
    st.write(f"{cv}")
    
########## ABA - PORTIFÓLIO ##########   
elif selected2 == options[1]:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        def example():
            card(
                title="",
                text="Inclusor de certificações",
                image="https://github.com/TCDuarte/PortfolioThiagoCairoDuarte/blob/main/streamlit/imgs/portifolio_pictures/cert_includ.png?raw=true",
                url="https://docs.google.com/spreadsheets/d/12lkSbB5lPSyyEMMUkw35cFwOrVYnq3k2NVO11-6oF8g/edit#gid=0",
            )
        example()
    with col2:
        def example():
            card(
                title="",
                text="Inclusor de certificações",
                image="https://github.com/TCDuarte/PortfolioThiagoCairoDuarte/blob/main/streamlit/imgs/portifolio_pictures/cert_includ.png?raw=true",
                url="https://docs.google.com/spreadsheets/d/12lkSbB5lPSyyEMMUkw35cFwOrVYnq3k2NVO11-6oF8g/edit#gid=0",
            )
        example()
    with col3:
        def example():
            card(
                title="",
                text="Inclusor de certificações",
                image="https://github.com/TCDuarte/PortfolioThiagoCairoDuarte/blob/main/streamlit/imgs/portifolio_pictures/cert_includ.png?raw=true",
                url="https://docs.google.com/spreadsheets/d/12lkSbB5lPSyyEMMUkw35cFwOrVYnq3k2NVO11-6oF8g/edit#gid=0",
            )
        example()
    with col4:
        def example():
            card(
                title="",
                text="Inclusor de certificações",
                image="https://github.com/TCDuarte/PortfolioThiagoCairoDuarte/blob/main/streamlit/imgs/portifolio_pictures/cert_includ.png?raw=true",
                url="https://docs.google.com/spreadsheets/d/12lkSbB5lPSyyEMMUkw35cFwOrVYnq3k2NVO11-6oF8g/edit#gid=0",
            )
        example()
    
########## ABA - CERTIFICADOS ##########
elif selected2 == options[2]:
    link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTWcpEoQTEqt5KbiDsphxgdTwIPuWszrNLWL-zwxm-WajTZ_PlKRmqg3vOzc_EFrA-5aZ1KSqaFvMPC/pub?gid=1545264035&single=true&output=csv'
    certificates = pd.read_csv(link)
    certificates['Tags'] = stringToList(certificates['Tags'])
    columnNames = ['Nome', 
                   'Data', 
                   'Instituição'] if selectedLanguage != 'English' else ['Name',
                                                                         'Date',
                                                                         'Institution']
    certificates.rename(columns = {certificates.columns[0]: columnNames[0],
                                 certificates.columns[1]: columnNames[1],
                                 certificates.columns[2]: columnNames[2]},
                        inplace = True)
    certificates.set_index([certificates.columns[0]],
                           inplace = True)
    st.dataframe(certificates)

########## ABA - SOBRE ##########
else: st.write ('Não salve')

