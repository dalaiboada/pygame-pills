coordenadas = (40.4168, -3.7038) # Coordenadas de Madrid

# Acceso
print("Latitud:", coordenadas[0])

# Desempaquetado (Destructuring): Muy útil para funciones que retornan varios valores
lat, lon = coordenadas
print("Desempaquetado -> Lat:", lat, "Lon:", lon)

# Intento de modificación (esto daría error):
# coordenadas[0] = 0.0