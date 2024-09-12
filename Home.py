# +----------------------------------------------------------
# <<<>>> PÁGINA PRINCIPAL <<<>>>
# +----------------------------------------------------------

# -- Import libraries
import streamlit as st
import pandas as pd
import mysql.connector
#import services.kmlnFunctions as kml

# -- Sets the screen orientation
st.set_page_config(
    page_title="SDQ - Samba de Quintal",
    page_icon="",
    #layout="wide",
    initial_sidebar_state="collapsed",
)

with st.container():
 
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    cpfCliente = col1.text_input(label="Informe o CPF")
    col2.text = "Nome do Cliente"
    btnFilter = col3.button(label="Pesquisa")

    # -- Display Coupom Balance
    if btnFilter:
        with st.spinner("Processando Pesquisa..."):

            connection = mysql.connector.connect(
                host='sql5.freesqldatabase.com',
                user='sql5731090',
                password='tMVHg2MvKe',
                database='sql5731090',
            )

            cursor = connection.cursor()

            strQuery = "Select * from vendasSDQ Where CPF = '" + cpfCliente + "'"

            cursor.execute(strQuery)

            data = cursor.fetchall()

            df = pd.DataFrame(data,columns=cursor.column_names)

            df



