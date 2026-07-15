# --- Ejemplos de Entrada, Salida y Conversión ---

# 1. Entrada y conversión de tipo
edad_texto = input("que edad tienes? ")
edad_numero = int(edad_texto)

# 2. Conversión a otros tipos
valor = 5
print("Entero a decimal:", float(valor))
print("Número a cadena:", str(valor))

# 3. Uso de bool
# Todo lo que no sea 0 o vacío, suele ser True
print("Booleano de 1:", bool(1))
print("Booleano de 0:", bool(0))