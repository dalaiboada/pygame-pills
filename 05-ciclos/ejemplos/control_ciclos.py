# Programa: Demostración de break y continue
for i in range(1, 6):
    if i == 2:
        continue  # Salta el 2
    if i == 5:
        break     # Se detiene al llegar a 5
    print("Valor:", i)