import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatisticas de filmes')

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por gênero')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes por gênero'
        )
        st.plotly_chart(fig)

    st.subheader('Total de filmes cadastrados:')
    st.write(movie_stats['total_movies'])

    for genre in movie_stats['movies_by_genre']:
        st.write(f'{genre['genre__name']}: {genre['count']}')

    st.subheader('Total de avaliações enviadas:')
    st.write(movie_stats['total_reviews'])

    st.subheader('Média geral de estrelas nas avaliações:')
    st.write(movie_stats['average_stars'])
