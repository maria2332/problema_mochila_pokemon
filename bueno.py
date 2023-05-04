import pandas as pd

# Cargar el archivo CSV
df_pokemon = pd.read_csv("pokemon.csv")

# Eliminar las columnas especificadas
df_pokemon = df_pokemon.drop(columns=["abilities", "against_bug", "against_dark", "against_dragon", "against_electric", "against_fairy", "against_fight", "against_fire", "against_flying", "against_ghost", "against_grass", "against_ground", "against_ice", "against_normal", "against_poison", "against_psychic", "against_rock", "against_steel", "against_water", "attack", "base_egg_steps", "base_happiness", "classfication", "defense", "experience_growth", "height_m", "hp", "japanese_name", "percentage_male", "pokedex_number", "sp_attack", "sp_defense", "speed", "type1", "type2", "weight_kg", "generation", "is_legendary"])

# Guardar el archivo CSV actualizado
df_pokemon.to_csv("pokemon_nombre_beneficio_peso.csv", index=False)