import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from movies.service import MovieService
from .service import ReviewService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.write('Lista de avaliações')
        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=reviews_df,
            reload_data=True,
            key='reviews_grid'
        )
    else:
        st.warning('Nenhuma avaliação encontrado')

    st.title('Enviar avaliação')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))

    st.write('Avaliação')
    stars = st.feedback('stars')
    if stars:
        stars_value = stars + 1
    else:
        stars_value = 0

    comment = st.text_area('Comentário')

    if st.button('Enviar'):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars_value,
            comment=comment
        )
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao enviar avaliação. Verifique os campos.')
