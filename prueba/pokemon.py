import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('pokedex_actualizado.csv')

# Eliminar las columnas especificadas
columnas_eliminar = ["TIPO_1", "TIPO_2", "PUNTOS_DE_VIDA", "PUNTOS_ATAQUE", "PUNTOS_DEFENSA", "PUNTOS_ATAQUE_ESPECIAL", "PUNTO_DEFENSA_ESPECIAL", "PUNTOS_VELOCIDAD", "NOMBRE_GENERATIONS", "LEGENDARIO"]
df = df.drop(columns=columnas_eliminar)

# Guardar el nuevo DataFrame en un archivo CSV
df.to_csv('pokedex_actualizado_sin_columnas.csv', index=False)