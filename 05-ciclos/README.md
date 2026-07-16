# 📁 Carpeta: `05-ciclos/`

## 💊 Píldora 05: Ciclos (Estructuras de Repetición)

Los ciclos nos permiten ejecutar un bloque de código varias veces. Existen dos tipos principales en Python:

---

### 1. El ciclo `while`
Se usa cuando **no sabemos cuántas veces** se debe repetir el proceso; continúa mientras la condición sea `True`.

```python
while condicion:
    # Código que se repite
    # IMPORTANTE: ¡Cambia la condición para evitar un bucle infinito!

```

> ⚠️ **Precaución:** Si la condición nunca cambia, crearás un "bucle infinito" y tu programa no se detendrá.

---

### 2. El ciclo `for`

Es la opción preferida para **recorrer secuencias** (listas, cadenas, rangos).

```python
for elemento in secuencia:
    # Código que se ejecuta para cada elemento

```

* **`range()`**: Muy útil con `for` para repetir algo un número de veces específico:
* `range(5)` → genera números del 0 al 4.
* `range(1, 6)` → genera números del 1 al 5.



---

### 3. Control de Ciclos

A veces necesitamos alterar el flujo natural:

| Comando | Acción |
| --- | --- |
| `break` | Termina el ciclo inmediatamente y sale de él. |
| `continue` | Salta la iteración actual y pasa a la siguiente. |

---

### 💻 Ejemplos de uso

* [🐍 Ejemplo con `while`](./ejemplos/while_basico.py)
* [🐍 Ejemplo con for `range()`](./ejemplos/for_range.py)
* [🐍 Ejemplo con generador de índices `range()`](./ejemplos/for_range.py)
* [🐍 Ejemplo con for en cadenas](./ejemplos/for_cadenas.py)
* [🐍 Ejemplo con `for` en listas](./ejemplos/for_lista.py)
* [🐍 Control con `break` y `continue`](./ejemplos/control_ciclos.py)

---

### 💡 Nota

> **¿Cuál elegir?**
> * Usa **`for`** cuando sepas de antemano cuántos elementos hay o quieres recorrer algo.
> * Usa **`while`** cuando el ciclo dependa de una condición lógica que cambia durante la ejecución (como esperar a que el usuario escriba 'salir').
