# Inicialización
contador = 0                
total_suma = 0            # acumuladores

# Supongamos que procesamos 3 números: 10, 20, 30
for valor in [10, 20, 30]:
  contador += 1       # El contador nos dice cuántas veces hemos pasado
  total_suma += valor # El acumulador guarda el resultado total

print("Veces procesadas:", contador)
print("Suma total:", total_suma)