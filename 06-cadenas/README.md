# 📁 Carpeta: `06-cadenas/`

## 💊 Píldora 06: Manejo de Cadenas (Strings)

Las cadenas son secuencias inmutables de caracteres. En Python, son objetos muy versátiles que podemos manipular fácilmente.

---

### ✍️ Creación y Operaciones Básicas

```python
texto1 = 'Hola'         # Comillas simples
texto2 = "Mundo"        # Comillas dobles
texto3 = """Esto permite
multilínea"""           # Comillas triples

```

| Operación     | Sintaxis          | Descripción                        |
| -------------- | ----------------- | ----------------------------------- |
| Concatenación | `s1 + s2`       | Une dos cadenas.                    |
| Repetición    | `s * 3`         | Repite la cadena 3 veces.           |
| Pertenencia    | `"a" in "hola"` | Retorna `True` si está presente. |

---

### 🔪 Indexación y Slicing (Rebanado)

Como las cadenas son secuencias, puedes acceder a sus posiciones (índices desde 0).

* **Indexación:** `s[0]` (primero), `s[-1]` (último).
* **Slicing `[inicio:fin:paso]`:**
* `s[0:4]` → Desde 0 hasta antes de 4.
* `s[::2]` → Toma uno, salta uno.
* `s[::-1]` → **¡Truco! Invierte la cadena.**

---

### 🛠️ Funciones Nativas para Cadenas

A diferencia de los métodos, estas funciones son globales y reciben la cadena como un parámetro.

| Función              | Qué hace                            | Ejemplo         | Salida            |
| --------------------- | ------------------------------------ | --------------- | ----------------- |
| **`len(s)`**  | Devuelve la longitud total.          | `len("Hola")` | `4`             |
| **`str(x)`**  | Convierte cualquier valor a `str`. | `str(10)`     | `"10"`          |
| **`type(s)`** | Devuelve el tipo de dato.            | `type("A")`   | `<class 'str'>` |

---

### ⚙️ Métodos de Objeto

A diferencia de las funciones nativas (como `len()`), los métodos se llaman con un punto: `variable.metodo()`.

| Método                     | Qué hacer                            | Ejemplo                                       | Salida                                          |
| --------------------------- | ------------------------------------ | --------------------------------------------- | ------------------------------------------------ |
| `.upper()` / `.lower()` | Mayúsculas / Minúsculas            | `"abc".upper()`                | `"ABC"`                                         |
| `.strip()`                | Quita espacios en extremos           | `" hola ".strip()`             | `"hola"`                                        |
| `.replace(a, b)`          | Sustituye el texto `a` por `b`   | `"gato".replace("g", "p")`    | `"pato"`                                        |
| `.find(x)`                | Índice de la primera ocurrencia     | `"hola".find("o")`                 | `3`                                             |
| `.startswith(x)`          | ¿Empieza con `x`?                 | `"hola".startswith("h")`        | `True`                                          |
| `.endswith(x)`            | ¿Termina con `x`?                 | `"archivo.py".endswith(".py")` | `True`                                          |
| `.join(lista)`            | Une elementos de una lista usando la cadena como separador. | `"-".join(['a', 'b', 'c'])`| `'a-b-c'`                                       |
---

### 💻 Ejemplos de uso

* [🐍 Concatenacion](./ejemplos/concatenacion.py)
* [🐍 Funciones nativas](./ejemplos/funciones_nativas.py)
* [🐍 Operaciones y Slicing](./ejemplos/basico_slicing.py)
* [🐍 Uso de Métodos](./ejemplos/metodos.py)
* [🐍 Metodo `.join()`](./ejemplos/metodo_join.py)

---

### 💡 Un consejo

Dado que las cadenas en Python son **inmutables** (no puedes cambiar un solo carácter como `s[0] = 'X'`), es importante que aprendan que los métodos como `.replace()` o `.upper()` **no modifican la original**, sino que devuelven una **nueva cadena**. Es un concepto que suele causar confusión al principio.
