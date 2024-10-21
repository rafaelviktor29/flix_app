import streamlit as st
from .service import login


def show_login():
    st.title('Login')

    username = st.text_input('Usuário')
    password = st.text_input('Senha', type='password')

    if st.button('Login'):
        login(
            username=username,
            password=password
        )
