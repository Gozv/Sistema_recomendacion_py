import psycopg2
import pandas as pd

# Establecer la conexión con PostgreSQL
conn = psycopg2.connect(
    dbname="Recomendacion_peliculas_hibrida",
    user="movie_recommend",
    password="123",
    host="localhost",
    port="5432"
)

# Crear un cursor para ejecutar las consultas
cursor = conn.cursor()

# Consulta SQL para obtener recomendaciones (ejemplo de géneros)
query = """
SELECT movieId, title, genres
FROM movies
WHERE genres LIKE '%Comedy%' 
ORDER BY movieId
LIMIT 5;
"""

# Ejecutar la consulta
cursor.execute(query)

# Obtener los resultados
result = cursor.fetchall()

# Crear un DataFrame con los resultados
df = pd.DataFrame(result, columns=["movieId", "title", "genres"])

# Guardar el DataFrame en un archivo CSV
df.to_csv('recomendaciones_comedy.csv', index=False)

# Cerrar la conexión
cursor.close()
conn.close()

print("Recomendaciones guardadas en 'recomendaciones_comedy.csv'")
