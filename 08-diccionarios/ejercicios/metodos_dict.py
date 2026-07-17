# Uso de .get() y .items()
data = {"a": 1, "b": 2}

print("Valor de c:", data.get("c", "No encontrado")) # Manejo seguro

for k, v in data.items():
    print(f"Clave {k} tiene valor {v}")