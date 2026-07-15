# --- Tipos de datos en Python ---

# 1. Numéricos
entero = 10                  # int
decimal = 3.14               # float
complejo = 1 + 2j            # complex

# 2. Secuencias y Texto
cadena = "Hola"              # str
lista = [1, 2, 3]            # list (Mutable)
tupla = (1, 2, 3)            # tuple (Inmutable)

# 3. Colecciones Especiales
diccionario = {'a': 1}       # dict (Mutable)
conjunto = {1, 2, 3}         # set (Mutable)

# 4. Otros
es_cierto = True             # bool
nada = None                  # NoneType

# --- Visualización ---
print("int:", entero, "| tipo:", type(entero))
print("float:", decimal, "| tipo:", type(decimal))
print("complex:", complejo, "| tipo:", type(complejo))
print("str:", cadena, "| tipo:", type(cadena))
print("list:", lista, "| tipo:", type(lista))
print("tuple:", tupla, "| tipo:", type(tupla))
print("dict:", diccionario, "| tipo:", type(diccionario))
print("set:", conjunto, "| tipo:", type(conjunto))
print("bool:", es_cierto, "| tipo:", type(es_cierto))
print("NoneType:", nada, "| tipo:", type(nada))