# 📁 Carpeta: `09-tuplas/`

## 💊 Píldora 09: Tuplas (`tuple`)

Las tuplas son colecciones **ordenadas** e **inmutables**. A diferencia de las listas, una vez creada una tupla, **no puedes añadir, eliminar ni cambiar sus elementos**.

---

### 📝 Sintaxis y Creación
Se utilizan paréntesis `()`.

* **Creación:** `t = (1, 2, 3)`
* **¡Cuidado!:** Para una tupla de un solo elemento, **debes incluir una coma**: `t = (1,)` (si no, Python lo interpreta solo como un número entre paréntesis).

---

### 🚀 ¿Por qué usar Tuplas en lugar de Listas?
1. **Seguridad:** Los datos están protegidos contra cambios accidentales.
2. **Rendimiento:** Al ser inmutables, son más rápidas y ocupan menos memoria que las listas.
3. **Uso común:** Ideales para datos que no deben cambiar, como coordenadas, fechas o configuraciones fijas.

---

### 🔧 Operaciones Principales

| Operación | Ejemplo | Nota |
| :--- | :--- | :--- |
| **Acceso** | `t[0]` | Funciona igual que en listas (índices). |
| **Desempaquetado** | `a, b, c = t` | Asigna cada elemento a una variable diferente. |

---

#### Métodos de las Tuplas

Al ser **inmutables**, las tuplas tienen menos métodos que las listas (no tienen `.append()`, `.remove()`, ni `.sort()`, porque no pueden cambiar), pero sí tienen **dos métodos fundamentales** que son muy útiles para consultar información:

Como la tupla no puede cambiar, estos métodos solo sirven para "preguntar" cosas sobre ella:

| Método | Qué hace | Ejemplo | Salida |
| --- | --- | --- | --- |
| **`.count(x)`** | Cuenta cuántas veces aparece `x`. | `(1, 2, 2, 3).count(2)` | `2` |
| **`.index(x)`** | Devuelve el índice de la primera aparición de `x`. | `("a", "b", "c").index("b")` | `1` |

---

### ¿Por qué no tienen más métodos?

Es importante explicarles a tus alumnos el **porqué**:

* **Listas:** Son dinámicas, necesitan métodos para crecer, encogerse y reorganizarse.
* **Tuplas:** Son estáticas. Si necesitas ordenar una tupla, no existe `.sort()` porque eso requeriría cambiar la tupla. Lo que haces es usar la función global `sorted(tupla)`, la cual **te devuelve una lista nueva**.

#### Ejemplo de este "truco" de conversión:

```python
mi_tupla = (3, 1, 2)
# Como la tupla no tiene .sort(), convertimos a lista o usamos sorted()
tupla_ordenada = tuple(sorted(mi_tupla))
print(tupla_ordenada) # (1, 2, 3)

```

---

### 💻 Ejemplos de uso
[🐍 Ver ejemplo de Tuplas](./ejemplos/basico_tuplas.py)
[🐍 Ver ejemplo de métodos con Tuplas](./ejemplos/metodos_tuplas.py)

---

### 💡 Nota

> *"Si una lista es una caja donde puedes meter, sacar y cambiar cosas (como una mochila), una tupla es como un archivo en PDF: una vez que lo creas, está listo para ser leído, pero no puedes cambiar su contenido original."*