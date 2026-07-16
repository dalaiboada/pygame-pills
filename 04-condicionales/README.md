# 📁 Carpeta: `04-condicionales/`

## 💊 Píldora 04: Estructuras Condicionales (`if`, `elif`, `else`)

Las estructuras condicionales permiten que tu programa **tome decisiones**. El código solo se ejecutará si se cumplen ciertas condiciones.

---

### 📝 Sintaxis
Python utiliza la indentación (espacios al inicio de la línea) para definir qué código pertenece a cada bloque.

```python
if condicion_1:
    # Código si condicion_1 es True
elif condicion_2:
    # Código si condicion_1 es False y condicion_2 es True
else:
    # Código si ninguna condición anterior se cumplió

```

* **`if`**: La condición obligatoria inicial.
* **`elif` (opcional)**: "Si no, si...". Puedes tener tantos como necesites para evaluar más casos.
* **`else` (opcional)**: El "caso por defecto". Solo puede haber uno y va al final.

---

### Ejemplo de uso

```python
# Ejemplo: Clasificación por edad
edad = 18

if edad < 13:
    print("Es un niño")
elif edad < 18:
    print("Es un adolescente")
else:
    print("Es un adulto")

```

---

### 🧱 Estructura Anidada (**if** dentro de otro **if**)
La anidación ocurre cuando colocamos **una estructura condicional dentro de otra**. Esto nos permite evaluar una segunda condición únicamente si la primera ya se cumplió.

```python
if edad >= 18:
    if tiene_membresia:
        print("Acceso VIP concedido.")
    else:
        print("Acceso estándar concedido.")
else:
    print("Acceso denegado: debes ser mayor de edad.")
```
---

### 💻 Ejemplos Prácticos

Puedes ejecutar este ejemplo para ver cómo el programa decide qué mensaje mostrar según el valor de la variable:

[🐍 Ver ejemplo if simple](./ejemplos/simple_if.py)
[🐍 Ver ejemplo if else](./ejemplos/if_else.py)
[🐍 Ver ejemplo if elif else](./ejemplos/elif_basico.py)
[🐍 Ver ejemplo elif multiple](./ejemplos/multi_elif.py)
[🐍 Ver ejemplo de anidación](./ejemplos/anidado.py)

---

### 💡 Puntos clave

1. **El orden importa:** Python evalúa las condiciones de arriba hacia abajo. En cuanto una es `True`, ejecuta su bloque y salta el resto.
2. **Indentación:** ¡Cuidado con los espacios! Si no mantienes la sangría, Python lanzará un error de indentación.
3. **Condición:** Debe ser siempre una expresión que resulte en `True` o `False`.



---

> **🚀 Reto para el Alumno:**
> Crea un archivo llamado `calificaciones.py`. Pide al usuario que ingrese una nota (de 0 a 100) usando `input()`.
> * Si la nota es mayor o igual a 90, imprime "Excelente".
> * Si es mayor o igual a 70, imprime "Aprobado".
> * Si es menor a 70, imprime "Reprobado".