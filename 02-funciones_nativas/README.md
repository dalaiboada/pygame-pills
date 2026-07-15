# 📁 Carpeta: `02-funciones_nativas/`

## 💊 Píldora 02: Funciones Nativas y Entrada/Salida

Las funciones nativas son herramientas que vienen "de fábrica" con Python. No necesitas instalar ni importar nada para usarlas; están siempre listas en el intérprete.

---

### 🧠 ¿Qué son las Funciones Nativas?

Son utilidades esenciales integradas en el lenguaje:

* **Entrada/Salida:** `print()`, `input()`
* **Conversión:** `int()`, `str()`, `float()`
* **Información:** `len()`, `type()`, `id()`, `dir()`
* **Matemáticas:** `max()`, `min()`, `abs()`, `sum()`, `round()`, `pow()`

---

### 📤 La función `print()`

Es la herramienta básica para mostrar información en consola. Por defecto, añade un salto de línea al final.

- **Uso Básico**

```python
print("Hola mundo")
```

#### 🔹Concatenación:

> Es unión de dos o más cadenas de texto mediante el operador

| Método                | Cómo funciona                                     | Ejemplo                                     |
| :--------------------- | :------------------------------------------------- | :------------------------------------------ |
| **Usando `+`** | Une cadenas. Requiere que**todo** sea texto. | `print("Hola " + "mundo")`  → Hola mundo |
| **Usando `,`** | Imprime objetos separados por un espacio.          | `print("Hola", 2026)` → Hola 2026        |

> **💡 TIP:**
> Con `+`, si sumas un número a una cadena, obtendrás un error. Debes convertir el número primero: `print("Edad: " + str(25))`. Con `,`, Python lo convierte automáticamente.

#### 🔹Parámetros Especiales:

* `sep`: Cambia el separador entre objetos (`print("A", "B", sep=",")` → `A,B`).
* `end`: Cambia el final de la impresión (`print("Hola", end="!")` → `Hola!`).

#### 🔹Interpolación de Cadenas

Es una técnica que permite insertar valores dentro de una cadena de texto.

```python
nombre = "Ana"
edad = 25
print(f"Hola {nombre}, tienes {edad} años.")

```

---

### 📥 La función `input()`

Permite que el usuario ingrese datos a través de la consola.

```python
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)
```

> ⚠️ Importante: `input()` siempre recibe la información como una cadena (str). Si necesitas un número, recuerda convertirlo usando int() o float().

---

### Siguientes pasos

Explorar otras funciones nativas útiles para la manipulación de datos y la interacción con el usuario.

- **Otras funciones nativas**:
  - [Conversión de tipos](./02-funciones_nativas/README.md#conversión-de-tipos): `int()`, `float()`, `str()`
  - [Información](./02-funciones_nativas/README.md#información): `len()`, `type()`, `id()`, `dir()`
  - [Matemáticas](./02-funciones_nativas/README.md#matemáticas): `max()`, `min()`, `abs()`, `sum()`, `round()`, `pow()`