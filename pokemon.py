import pandas as pd

# Lee el archivo CSV y convierte los datos a un DataFrame de pandas.
df = pd.read_csv("pokemon.csv")

# Ordena los Pokemon por valor y días de disponibilidad.
df = df.sort_values(["value", "days_available"], ascending=[False, True])

# Inicializa una lista vacía para almacenar los Pokemon capturados y el valor total.
capturados = []
valor_total = 0

# Itera sobre los Pokemon ordenados y decide cuáles capturar.
for index, row in df.iterrows():
    # Verifica si el Pokemon aún está disponible.
    if row["days_available"] > 0:
        # Agrega el Pokemon a la lista de capturados y suma su valor al valor total.
        capturados.append(row["pokemon"])
        valor_total += row["value"]
        # Actualiza el número de días de disponibilidad del Pokemon.
        df.loc[index, "days_available"] -= 1

# Imprime los Pokemon capturados y el valor total.
print("Pokemon capturados:", capturados)
print("Valor total:", valor_total)
