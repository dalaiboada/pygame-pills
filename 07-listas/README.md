# 📁 Carpeta: `07-listas/`

## 💊 Píldora 07: Listas (`list`)

Las listas son colecciones **ordenadas** y **mutables** de elementos. Pueden almacenar datos de distintos tipos (enteros, strings, booleanos) e incluso otras listas.

---

### 1. Creación, Acceso y Mutabilidad

```python
lista = [1, "hola", 3.14, True]
print(lista[0])    # Acceso: 1
lista[1] = "mundo" # Mutabilidad: ¡Podemos cambiar elementos!

```

---

### 2. Métodos Principales (Modifican la lista original)

Estos métodos cambian la estructura de la lista en memoria:

| Método           | Qué hace                               | Ejemplo                  |
| ----------------- | --------------------------------------- | ------------------------ |
| `.append(x)`    | Agrega `x` al final.                  | `lista.append(5)`      |
| `.insert(i, x)` | Inserta `x` en la posición `i`.    | `lista.insert(0, "A")` |
| `.pop(i)`       | Elimina y retorna el elemento en `i`. | `lista.pop(0)`         |
| `.remove(x)`    | Elimina la primera aparición de `x`. | `lista.remove("hola")` |
| `.sort()`       | Ordena la lista (mutándola).           | `lista.sort()`         |
| `.reverse()`    | Invierte el orden.                      | `lista.reverse()`      |

---

### 3. Funciones Útiles (Trabajan sobre la lista)

Estas funciones reciben la lista como parámetro y devuelven un resultado, sin modificar la original (excepto `sorted()` que devuelve una nueva).

| Función           | Qué hace                                    | Ejemplo                                |
| ------------------ | -------------------------------------------- | -------------------------------------- |
| `len(lista)`     | Cantidad de elementos.                       | `len([1, 2, 3])` → `3`            |
| `sum(lista)`     | Suma de elementos (solo números).           | `sum([1, 2, 3])` → `6`            |
| `min/max(lista)` | Valor mínimo o máximo.                     | `min([1, 2, 3])` → `1`            |
| `sorted(lista)`  | **Devuelve una nueva** lista ordenada. | `sorted([3, 1, 2])` → `[1, 2, 3]` |

---

### 💻 Ejemplos de uso

* [🐍 Creación, Acceso y Mutación](./ejemplos/basico_listas.py)
* [🐍 Métodos de modificación](./ejemplos/metodos_lista.py)
* [🐍 Funciones de análisis](./ejemplos/funciones_lista.py)

### 💡 Nota

> *"Los métodos como `.sort()` o `.append()` son como editar un documento abierto; cambias el original. Funciones como `sorted()` son como usar 'Guardar como...'; dejas el original intacto y creas uno nuevo."*
