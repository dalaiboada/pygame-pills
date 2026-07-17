# 📁 Carpeta: `08-diccionarios/`

## 💊 Píldora 08: Diccionarios (`dict`)

Los diccionarios almacenan elementos en pares de **clave:valor**. Son mutables y permiten realizar búsquedas extremadamente rápidas mediante la clave.

---

### 1. Creación y Acceso
```python
usuario = {
  "nombre": "Ana", 
  "edad": 25
}

print(usuario["nombre"])      # Acceso: "Ana"
usuario["ciudad"] = "Madrid"  # Añade clave nueva
usuario["edad"] = 26          # Modifica clave existente

```

---

### 2. Métodos Principales

| Método | Qué hace | Ejemplo |
| --- | --- | --- |
| `.get(k)` | Obtiene el valor (sin error si no existe). | `usuario.get("email")` |
| `.keys()` | Retorna todas las claves. | `usuario.keys()` |
| `.values()` | Retorna todos los valores. | `usuario.values()` |
| `.items()` | Retorna pares (clave, valor) en tuplas. | `usuario.items()` |
| `.pop(k)` | Elimina la clave y retorna su valor. | `usuario.pop("edad")` |
| `.update(d)` | Fusiona otro diccionario en el actual. | `usuario.update({"x": 1})` |

---

### 3. Funciones y Operaciones

* `len(d)`: Cantidad de pares clave-valor.
* `del d[k]`: Elimina una clave permanentemente.
* `k in d`: Verifica si la clave `k` existe en el diccionario.

---

### ⚠️ Notas Importantes

* **Claves únicas:** Las claves deben ser inmutables (strings, números, tuplas). **No** puedes usar una lista como clave.
* **Seguridad:** Usa `.get()` en lugar de `[]` si no estás seguro de que la clave existe; así evitarás el error `KeyError`.
* **Iteración:** La forma más eficiente de recorrerlos es `.items()`:
```python
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

```

* Mientras las listas son para colecciones donde el orden importa y los elementos se acceden por posición (0, 1, 2...), **los diccionarios son para colecciones donde el "nombre" o "identificador" (clave) es lo que importa.**
