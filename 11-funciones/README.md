# 📁 Carpeta: `11-funciones/`

## 💊 Píldora 11: Funciones

Las funciones nos permiten agrupar código para ejecutar una tarea específica.

---

### 📝 Sintaxis Básica

Usamos la palabra reservada `def` para definirlas:

#### Procedimiento

```python
def nombre_funcion():
  # comandos

```

#### Función con parámetros y retorno

```python
def nombre_funcion(parametro1, parametro2):
  # comandos
  return ""

```

* **Parámetros:** Los valores que recibe la función entre paréntesis.
* **`return`:** Es el punto de salida donde la función entrega un resultado. Si no tiene `return`, la función devuelve `None`.

##### 💡 Notas:

> Un **procedimiento** es una función que **no devuelve** ningún valor, mientras que **una función sí lo hace**.

> Las funciones pueden ser **anidadas**, es decir, definidas dentro de otras funciones. Esto permite crear **clausuras** y encapsular comportamientos.

> En Python, las funciones son **objetos de primera clase**, lo que significa que **pueden ser asignadas a variables**, **pasadas como argumentos** a otras funciones y **retornadas desde otras funciones**.

---

### 🧱 Componentes de una Función

1. **Definición (`def`):** Crea la función en memoria.
   Al escribir `def saludar(nombre):`, estamos definiendo una función llamada `saludar` que recibe un parámetro llamado `nombre`.

  Con esto la hemos creado, pero aún no la hemos ejecutado. Para eso necesitamos hacer una **llamada** a la función.

- *Ejemplo:*

```python
  def mostrar_bienvenida():
    print("---------------------------------------------------------")
    print("       BIENVENIDO A PYTHON-PILLS        ")
    print("---------------------------------------------------------")
    print("     Presiona [ENTER] para comenzar...     ")
    print("---------------------------------------------------------")
```

2. **Llamada:** Ejecuta el código interno.

  Esto permite que la función ejecute los comandos que contiene.

- *Ejemplo:*

```python
  mostrar_bienvenida()  # Llamada a la función
```

3. **Parámetro**: Es la variable que pone en la **definición** de la función (el "contenedor" o la etiqueta).

   - *Ejemplo:*

```python
  def saludar(nombre):
    print("Hola", nombre)
```

4. **Argumento**: Es el valor real que se pasa al **llamar** a la función.

- *Ejemplo:*

```python
  saludar("Alice") # "Alice" es el argumento que se pasa al parámetro "nombre"
```

5. **Valor de retorno *(`return`)***: El resultado que sale de la función hacia el programa principal.

- *Ejemplo:*

```python
  def sumar(a, b):
    return a + b

  resultado = sumar(5, 3)
  print("El resultado es:", resultado) # imprime: El resultado es: 8
```

---

### 🔄 Argumentos Avanzados

* **Argumentos por defecto:** Si no pasamos un valor, usa uno predeterminado.

```python
def saludar(nombre = "Desconocido"):
  print("Hola", nombre)
```

Todos los parámetros con valores por defecto deben ir **al final** de la lista de parámetros.

* **Argumentos variables (`*args`):** Para recibir un número indeterminado de parámetros.

```python
def mostrar_ingredientes(*lista_ingredientes):
  print("Ingredientes:")

  for ingrediente in lista_ingredientes:
    print("-", ingrediente)

```

* **Argumentos clave (`**kwargs`):** Para recibir un diccionario de parámetros.

```python
def mostrar_configuracion(**opciones):
  print("=== CONFIGURACIÓN ACTUAL ===")
  
  # recorrer el diccionario
  for clave, valor in opciones.items():
      print(clave + ": " + str(valor))

# Al llamarlo, debes escribir Nombre_Variable = Valor
mostrar_configuracion(resolucion="1920x1080", volumen=80, pantalla_completa=True)

```

---

### 💻 Ejemplos de uso

* [🐍 Procedimiento](ejemplos/procedimiento.py)
* [🐍 Función básica y retorno](ejemplos/funcion_simple.py)
* [🐍 Parámetros por defecto](ejemplos/parametros_default.py)
* [🐍 Uso de `*args` y `**kwargs`](ejemplos/parametros_variables.py)

---

> "Una función es como un **contrato**. Tú me das unos datos de entrada (argumentos) y yo te prometo devolverte un resultado específico (valor de retorno) sin que tengas que preocuparte por cómo hice el trabajo interno."
