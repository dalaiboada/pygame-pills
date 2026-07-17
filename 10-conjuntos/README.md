# 📁 Carpeta: `10-conjuntos/`

## 💊 Píldora 10: Conjuntos (`set`)

Los conjuntos son colecciones **desordenadas** y **sin elementos duplicados**. Son extremadamente rápidos para verificar pertenencia y realizar operaciones matemáticas.

---

### 📝 Sintaxis y Creación
Se usan llaves `{ }` (ojo: si están vacías `{}` crean un diccionario, usa `set()` para un conjunto vacío).

* **Creación:** `s = {1, 2, 3}`
* **Característica:** **No tienen índice** (no puedes hacer `s[0]`). Intentar acceder a un elemento por su posición causará un error.

---

### 🛠️ Métodos Principales

| Método | Qué hace | Ejemplo |
| :--- | :--- | :--- |
| `.add(x)` | Añade el elemento `x`. | `s.add(4)` |
| `.remove(x)` | Elimina `x` (da error si no existe). | `s.remove(4)` |
| `.discard(x)` | Elimina `x` (no da error si no existe). | `s.discard(4)` |
| `set(lista)` | Convierte una lista a `set`. | `set([1, 1, 2])` → `{1, 2}` |

---

### 📐 Operaciones de Conjuntos (Matemáticas)

| Operación | Sintaxis | ¿Qué hace? |
| :--- | :--- | :--- |
| **Unión** | `s1 \| s2` | Une ambos conjuntos eliminando duplicados. |
| **Intersección** | `s1 & s2` | Devuelve solo los elementos presentes en **ambos**. |
| **Diferencia** | `s1 - s2` | Elementos que están en `s1` pero **no** en `s2`. |

---

### 💻 Ejemplo de uso
[🐍 Ver operaciones con conjuntos](./ejemplos/uso_conjuntos.py)

---

### 💡 Un Tip

A veces intentan crear un conjunto vacío usando `{}`. Es importante recordarles:

> "Si escribes `c = {}`, Python creará un **diccionario vacío**. Para un **conjunto vacío**, debes usar explícitamente `c = set()`."