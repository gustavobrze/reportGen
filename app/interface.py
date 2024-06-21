import streamlit as st
from base import client_list
from generate_pdf import genPDF

st.title("Gerador de Relatórios")

sheet = st.file_uploader('Selecione a planilha:')

if sheet:
    
    clients = client_list(sheet)

    client = st.selectbox("Selecione um cliente:", clients)

    if st.button("Gerar PDF"):
    # Gerar PDF com base no nome selecionado e dados da planilha
        genPDF(sheet, client)