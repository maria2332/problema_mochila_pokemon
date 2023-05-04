import pandas as pd

# Lee el archivo CSV actualizado y convierte los datos a un DataFrame de pandas.
df_pokedex_actualizado = pd.read_csv("pokedex_actualizado.csv")

# Selecciona solo las columnas "Nombre" y "Total" del DataFrame actualizado.
df_NOMBRE_TOTAL = df_pokedex_actualizado[["NOMBRE", "TOTAL"]]

# Guarda el DataFrame con las columnas seleccionadas como un archivo CSV.
df_NOMBRE_TOTAL.to_csv("pokedex_NOMBRE_TOTAL.csv", index=False)

# Imprime un mensaje de confirmación.
print("El archivo CSV con las columnas 'Nombre' y 'Total' ha sido guardado con éxito.")