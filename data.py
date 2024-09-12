# +----------------------------------------------------------
# <<<>>> PÁGINA PRINCIPAL <<<>>>
# +----------------------------------------------------------

# -- Import libraries
import streamlit as st
import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host='sql5.freesqldatabase.com',
    user='sql5731090',
    password='tMVHg2MvKe',
    database='sql5731090',
)

print('connected')

cursor = connection.cursor()

cursor.execute("Select * from vendasSDQ Where CPF = '31965713866'")

data = cursor.fetchall()

st.title('SDQ - SAMBA DE QUINTAL - 10 ANOS')

df = pd.DataFrame(data,columns=cursor.column_names)

df