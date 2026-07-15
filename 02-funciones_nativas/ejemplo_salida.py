# --- Ejemplos de Entrada y Salida ---

# 1. Concatenación
print("Concatenacion con comas:", "Python", 3.14)
print("Concatenacion con +:" + " " + "Python")

# 2. Parámetros adicionales
print("Uso de sep:", "A", "B", "C", sep="-")            # separación entre cadenas

print("Uso de end:", "Cargando", end="...")             # quitar salto de línea
print("Listo!")

# 3. Interpolación
nombre = "Ana"
edad = 25
print(f"Hola {nombre}, tienes {edad}.")
