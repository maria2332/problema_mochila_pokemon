# sumar las columnas PUNTOS_DE_VIDA,PUNTOS_ATAQUE,PUNTOS_DEFENSA,PUNTOS_ATAQUE_ESPECIAL,PUNTO_DEFENSA_ESPECIAL,PUNTOS_VELOCIDAD y crear una nueva columna llamada TOTAL y agregarla al final del dataframe original (pokedex.csv)
import pandas as pd

# Lee el archivo CSV y convierte los datos a un DataFrame de pandas.
df = pd.read_csv("pokedex.csv")

# Suma las columnas de puntos y crea una nueva columna llamada TOTAL.
df["TOTAL"] = df["PUNTOS_DE_VIDA"] + df["PUNTOS_ATAQUE"] + df["PUNTOS_DEFENSA"] + df["PUNTOS_ATAQUE_ESPECIAL"] + df["PUNTO_DEFENSA_ESPECIAL"] + df["PUNTOS_VELOCIDAD"]

# Imprime el DataFrame actualizado.
print(df)