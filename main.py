import pandas as pd
from src.recomendador import recomendar_por_genero, recomendar_por_generos, recomendar_por_generos_todos
from src.config import generos_preferidos
from src.colaborativo import recomendar_hibrido  # Ahora está bien importado

# Cargar el archivo CSV de películas
movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')

# Crear la matriz de usuario-película
user_movie_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Usar las funciones de recomendación
print("Recomendación de un solo género (Comedy):")
print(recomendar_por_genero('Comedy', movies).head())

print("\nRecomendación de varios géneros (Comedy y Action):")
print(recomendar_por_generos(['Comedy', 'Action'], movies).head())

print("\nRecomendación de todos los géneros seleccionados:")
print(recomendar_por_generos_todos(generos_preferidos, movies).head())

# Recomendación híbrida para el usuario con ID 1
print("\nRecomendación híbrida para el usuario 1:")
print(recomendar_hibrido(1, user_movie_matrix, movies).head())
