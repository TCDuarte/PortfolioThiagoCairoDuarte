########## LIVRARIAS ##########

import pandas as pd
import streamlit as st
import json
from streamlit_option_menu import option_menu
from streamlit_extras.card import card
from streamlit_extras.tags import tagger_component

########## DECLARAÇÃO DAS VARIÁVEIS CHAVES ##########

username = 'TCDuarte'
repository_name = 'PortfolioThiagoCairoDuarte'
style = "<style>h2 {text-align: center;}</style>"

########## DECLARAÇÃO DAS FUNÇÕES ##########

def return_text(text):
    pathing = 'EN' if selectedLanguage == 'English' else 'PT'
    with open(f"texts/{pathing}/{text}.txt", "r") as file:
        textContent = file.read()
    return textContent

def stringToList(serie):
    finalList = []
    for x in serie:
        if x.count(';') > 0:
            valueList = x.split('; ')
            finalList.append(valueList)
        else:
            finalList.append([x])
    return finalList

def add_col_index(df):
    listN = []
    b = 0
    colNun = 1
    while b < len(df.index):
        listN.append(colNun)
        b += 1
        colNun = colNun + 1 if colNun != 4 else 1
    return listN

def find_color(value, data):
    for item in data:
        if value in item.values():
            return list(item.keys())[0]  # Get the first key (color)
    return None

def tag_color_list(tagsList):
    colorList = []
    with open(r'data/color_reference.json', 'r') as jsonfile:
        colorReference = json.load(jsonfile)
    for x in tagsList:
        coloredTag = str(find_color(x, colorReference))
        colorList.append(coloredTag)
    return colorList

def add_to_portfolium_page(data, number):
    filteredDf = data[data['column'] == number]
    for index, row in filteredDf.iterrows():
        projectName = row['nameEN'] if selectedLanguage == 'English' else row['namePT']
        st.write(fr"<h1 style='text-align: center; font-size: 16px; color: grey;'>{projectName}</h1>", unsafe_allow_html=True)
        card(
            title = "",
            text = row['nameEN'] if selectedLanguage == 'English' else row['namePT'],
            image = row['file'],
            url = row['url'],
            styles={
                "card": {
                    "width": "250px",
                    "height": "250px",
                    "border-radius": "30px",
                    "margin-top": -40,
                    "margin-bottom": -50}
                    }
                )
        tagger_component(
            "",
            row['tags'],
            color_name = tag_color_list(row['tags']),
        )
        st.divider()

########## CONFIGURAÇÃO DO STREAMLIT ##########
st.set_page_config(layout = 'wide')
with st.sidebar:
    st.image('https://github.com/TCDuarte/PortfolioThiagoCairoDuarte/blob/main/streamlit/imgs/profile.png?raw=true',
             use_column_width = 'auto')
    st.write(f'**Thiago Cairo Duarte**')
    st.write('📱 15 99771-7474')
    st.write('✉️ thiago.cairo.duarte@gmail.com')
    st.write('https://www.linkedin.com/in/tcduarte/')
    selectedLanguage = option_menu('Idioma', ['Português', 'English'],
        menu_icon='cast', default_index=0)
    
options = ['Portifólio', 'Certificados', 'Currículo'] if selectedLanguage == 'Português' else ['Portfolio', 'Certificates', 'Curriculum']

selected2 = option_menu(None, 
                        options, 
                        icons=['file-earmark-text', 'clipboard-data', 'patch-check', 'info-lg'], 
                        menu_icon='cast', default_index=0, orientation='horizontal')

title = str(selected2) if selected2 != options[0] else 'Thiago Cairo Duarte'
st.divider()
st.write(fr"<h1 style='text-align: center; font-size: 40px; color: white;'>{str(title)}</h1>", unsafe_allow_html=True)
st.divider()
########## ABA - CURRÍCULO ##########
if selected2 == options[0]:
    educ = 'Education' if selectedLanguage == 'English' else 'Formação Acadêmica'
    exp = 'Professional experience' if selectedLanguage == 'English' else 'Experiência Profissional'
    st.write(fr"<h1 style='font-size: 40px; color: white; font-family: Merriweather; font-weight: bold;'>{str(educ)}</h1>", unsafe_allow_html=True)
    st.write(return_text('education'))
    st.write(fr"<h1 style='font-size: 40px; color: white; font-family: Merriweather; font-weight: bold;'>{str(exp)}</h1>", unsafe_allow_html=True)
    st.write(return_text('experience'))
    st.divider()
    
########## ABA - PORTIFÓLIO ##########
elif selected2 == options[1]:
    portfolioData = pd.read_json('data/portfolio.json')
    portfolioData['column'] = add_col_index(portfolioData)
    cols = st.columns(4)
    for col_num, col in enumerate(cols, start=1):
        with col:
            add_to_portfolium_page(portfolioData, col_num)
        
########## ABA - CERTIFICADOS ##########
elif selected2 == options[2]:
    link = st.secrets['CERTIFICATES']
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

    manors = certificates[certificates.Manor == True].values.tolist()
    for x in manors:
        st.subheader(x[0])
        textSample = f'Institution: {x[2]} | Issued on {x[1]}' if selectedLanguage == 'English' else f'Instituição: {x[2]} | Emitido em {x[1]}'
        st.write(textSample)
        countRows = certificates['Manor_name'].str.contains(f'{x[0]}').sum()
        if countRows > 1:
            minors = certificates[(certificates.Manor == False) & (certificates.Manor_name == str(x[0]))].iloc[:, :3]
            label = 'Related certificates' if selectedLanguage == 'English' else 'Certificados relacionados'
            with st.popover(label):
                st.write(minors)
        st.divider()

########## ABA - SOBRE ##########
else: 
    st.write ('Não salve')