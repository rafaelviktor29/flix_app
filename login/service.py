import streamlit as st
from api.service import Auth


def login(username, password):
    auth_service = Auth()
    reponse = auth_service.get_token(
        username=username,
        password=password
    )
    if reponse.get('error'):
        st.error(f'Falha ao realizar o login: {reponse.get("error")}')
    else:
        st.session_state.token = reponse.get('access')
        st.rerun()


def logout():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
