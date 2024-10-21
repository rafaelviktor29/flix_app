import streamlit as st
from actors.page import show_actors
from genres.page import show_genres
from login.page import show_login
from movies.page import show_movies
from reviews.page import show_reviews
from home.page import show_home


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Flix App')

        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Início', 'Gêneros', 'Atores', 'Filmes', 'Avaliações']
        )

        option = {
            'Início': show_home,
            'Gêneros': show_genres,
            'Atores': show_actors,
            'Filmes': show_movies,
            'Avaliações': show_reviews
        }

        option[menu_option]()


if __name__ == '__main__':
    main()
