import pandas as pd
from sklearn.decomposition import TruncatedSVD

# Cargar los datos de ratings (usuario, película, calificación)
ratings = pd.read_csv('data/ratings.csv')

# Crear la matriz de usuario-película
user_movie_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Aplicar SVD
svd = TruncatedSVD(n_components=20)  # Usamos 20 componentes (puedes ajustar este número)
matrix_decomposicion = svd.fit_transform(user_movie_matrix)

# Producir la aproximación de la matriz original
reconstructed_matrix = svd.inverse_transform(matrix_decomposicion)

# Convertir a DataFrame para visualización
reconstructed_df = pd.DataFrame(reconstructed_matrix, columns=user_movie_matrix.columns)


def recomendar_hibrido(usuario_id, user_movie_matrix, movies_df, n=10):
    # Recomendación colaborativa usando la matriz descompuesta
    usuario_idx = user_movie_matrix.index.get_loc(usuario_id)
    recomendaciones = reconstructed_df.iloc[usuario_idx]
    recomendaciones = recomendaciones.sort_values(ascending=False)

    # Recomendación basada en género
    generos_preferidos = ['Comedy', 'Action']  # O lo que prefieras
    peliculas_por_genero = movies_df[
        movies_df['genres'].apply(lambda x: any(genre in x for genre in generos_preferidos))]

    # Combinar ambos métodos de recomendación (puedes ajustar cómo combinarlos)
    peliculas_recomendadas = recomendaciones.head(n).index
    peliculas_recomendadas = movies_df[movies_df['movieId'].isin(peliculas_recomendadas)]

    # Puedes combinar la recomendación colaborativa con la filtración por género si deseas
    # Aquí combinamos ambos métodos de forma sencilla, pero puedes experimentar con el enfoque
    peliculas_finales = pd.concat([peliculas_recomendadas, peliculas_por_genero]).drop_duplicates()

    return peliculas_finales[['movieId', 'title', 'genres']]
