# Programa: Limpiar duplicados y operaciones matemáticas

lista_duplicada = [1, 2, 2, 3, 3, 3, 4]

conjunto = set(lista_duplicada)

print("Lista", lista_duplicada)
print("Lista limpia:", conjunto) # {1, 2, 3, 4}

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print("Union:", s1 | s2)          # {1, 2, 3, 4, 5}
print("Interseccion:", s1 & s2)  # {3}
print("Diferencia:", s1 - s2)    # {1, 2}