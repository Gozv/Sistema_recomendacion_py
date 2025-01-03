import pandas as pd

def recomendar_por_genero(genero, movies_df):
    peliculas_recomendadas = movies_df[movies_df['genres'].apply(lambda x: genero in x)]
    return peliculas_recomendadas[['movieId', 'title', 'genres']]

def recomendar_por_generos(generos, movies_df):
    peliculas_recomendadas = movies_df[movies_df['genres'].apply(lambda x: any(genre in x for genre in generos))]
    return peliculas_recomendadas[['movieId', 'title', 'genres']]

def recomendar_por_generos_todos(generos, movies_df):
    peliculas_recomendadas = movies_df[movies_df['genres'].apply(lambda x: all(genre in x for genre in generos))]
    return peliculas_recomendadas[['movieId', 'title', 'genres']]
