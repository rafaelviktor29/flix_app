from datetime import datetime
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from .service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de atores')
        actors_df = pd.json_normalize(actors)

        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid'
        )
    else:
        st.warning('Nenhum ator/atriz encontrado')

    st.title('Cadastrar novo(a) ator/atriz')
    name = st.text_input('Nome do(a) ator/atriz')
    birthday = st.date_input(
        label='Data de nascimento',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown = ['BRAZIL', 'USA', 'UK']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown,
    )
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar ator/atriz. Verifique os campos.')
