# 📁 Carpeta: `01-tipos_de_datos/`

## 💊 Píldora 01: Tipos de Datos y Mutabilidad

Antes de escribir programas complejos, debemos entender qué tipo de información maneja Python y cómo se comporta en la memoria.

---

## 📋 Resumen de Tipos

| Tipo         | Ejemplo                      | ¿Es mutable? | ¿Qué es?                                   |
| :----------- | :--------------------------- | :-----------: | -------------------------------------------- |
| `int`      | `42`, `-7`, `0`        |     ❌ No     | Números enteros. Sin decimales.             |
| `float`    | `3.14`, `-0.5`, `1e3` |     ❌ No     | Números con decimales.                      |
| `complex`  | `1 + 2j`                   |     ❌ No     | Un número **complejo**               |
| `str`      | `"hola"`, `'Python'`     |     ❌ No     | Cadenas de texto. Se definen con comillas.   |
| `list`     | `[1, 2, 3]`                |    ✅ Sí    | Colección ordenada                          |
| `tuple`    | `(1, 2, 3)`                |     ❌ No     | Colección ordenada                          |
| `dict`     | `{'a': 1}`                 |    ✅ Sí    | Pares clave-valor.                           |
| `set`      | `{1, 2, 3}`                |    ✅ Sí    | Colección**sin duplicados** ni orden. |
| `bool`     | `True`, `False`          |     ❌ No     | Solo dos valores: verdadero o falso.         |
| `NoneType` | `None`                     |     ❌ No     | Valor Nulo.                                  |

---

## 🧠 Conceptos Clave

### 🔄 Mutable vs. Inmutable

> **Mutable (Modificable):** Puedes cambiar el contenido del objeto sin crear uno nuevo en memoria.
> *Ejemplos: `list`, `dict`, `set`.*

> **Inmutable (Fijo):** El contenido es permanente. Si intentas modificarlo, Python crea un nuevo objeto en memoria.
> *Ejemplos: `int`, `float`, `str`, `tuple`, `bool`.*

> **💡 TIP:**
> **Reasignar vs. Mutar**:
>
> - **Reasignar** es cambiar a dónde apunta el nombre de tu variable.
> - **Mutar** es cambiar lo que vive dentro de la memoria del objeto.

---

## 💡 Ejemplos Prácticos

Puedes encontrar ejemplos ejecutables en: [`ejemplos_tipos.py`](./ejemplo_tipos.py)
