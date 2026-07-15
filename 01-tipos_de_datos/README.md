# 📁 Carpeta: `01-tipos_de_datos/`

## 💊 Píldora 01: Tipos de Datos y Mutabilidad

Antes de escribir programas complejos, debemos entender qué tipo de información maneja Python y cómo se comporta en la memoria.

---

## 📋 Resumen de Tipos

| Tipo         | Ejemplo       | ¿Es mutable? |
| :----------- | :------------ | :-----------: |
| `int`      | `10`        |     ❌ No     |
| `float`    | `3.14`      |     ❌ No     |
| `complex`  | `1 + 2j`    |     ❌ No     |
| `str`      | `'Hola'`    |     ❌ No     |
| `list`     | `[1, 2, 3]` |    ✅ Sí    |
| `tuple`    | `(1, 2, 3)` |     ❌ No     |
| `dict`     | `{'a': 1}`  |    ✅ Sí    |
| `set`      | `{1, 2, 3}` |    ✅ Sí    |
| `bool`     | `True`      |     ❌ No     |
| `NoneType` | `None`      |     ❌ No     |

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
