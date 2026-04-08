# 📁 Carpeta: `00-introduccion-poo/`

## 💊 Píldora 00: Programación Orientada a Objetos (POO)

Antes de entrar de lleno a Pygame, necesitamos entender la **POO**.

La POO es simplemente una forma de organizar nuestro código para que se parezca al mundo real. En lugar de tener variables y funciones sueltas por todo el archivo, las agrupamos en "paquetes" llamados  **Clases** .

---

### 🧠 La Lógica de las Clases

Para entenderlo fácilmente, piensa en una Clase como una Caja de Herramientas que agrupa dos cosas:

- **Atributos** $\approx$ **Variables**: Son los datos o características. (Ej: nombre, edad, color).
- **Métodos** $\approx$ **Funciones**: Son las acciones que se pueden realizar con esos datos. (Ej: saludar, correr, calcular).

**¿Cuál es la ventaja?** Que la Clase agrupa todo lo que le pertenece a un mismo concepto en un solo lugar.

---

### 🛠️ POO en Python

#### Glosario de términos

| Término               | ¿Qué hace?                                                                                                                                                            |
| :--------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`class`**    | Palabra clave para crear nuestro molde (clase).                                                                                                                         |
| **`__init__`** | El**Constructor**. Es la función que se ejecuta automáticamente al crear un objeto.<br />Nos permite definir qué variables (atributos) tendrá nuestra clase  |
| **`self`**     | Hace referencia "a uno mismo". Sirve para que el objeto guarde su propia información.                                                                                  |
| **`def`**      | Palabra clave para crear una función (método). Siempre recibe `self` como primer parámetro.                                                                        |
| **`super()`**  | Se usa en la herencia para llamar a las funciones del "padre".                                                                                                          |

#### Estructura de una clase

```python
class NombreClase:
  def __init__(self, nombre_atributo1, nombre_atributo2):
    self.nombre_atributo1 = nombre_atributo1
    self.nombre_atributo2 = nombre_atributo2

  def nombre_metodo1(self):
    # Aquí va el código que queremos que haga el método
  
    # Ejemplo: Si queremos mostrar el atributo 1 (nombre_atributo1)
    print(self.nombre_atributo1) 
    # Se usa self para acceder a los atributos de la clase
```

#### Ejemplo de uso

```python
class Estudiante:
  def __init__(self, nombre, apellido, edad):
    # Atributos: Guardamos la información
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad

  def saludar(self):
    # Método: Una acción
    print(f"Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años.")
```

> **💡 TIP:**
> **`Self` es obligatorio**: Dentro de una clase (**solo dentro de la clase**), para usar una variable propia, siempre debes poner `self.` antes. Si no lo haces, Python pensará que es una variable local (cualquier otra variable suelta en el código que no es una característica de la clase).
>
> Así mismo, **cada método** lleva como primer parámetro `self`

***¡Felicidades! 🎉*** Con este código ya tienes tu primera **clase Estudiante**
**Responde**: *¿Cuántos atributos tiene?* *¿cuáles son?* *¿cuántos métodos tiene?* *¿cómo se llama?*

---

### 🧬 Herencia: El "Power-Up" de la POO

La herencia permite que una clase "hija" herede las características de una clase "padre". Es vital en Pygame porque nuestros personajes heredarán funciones de la clase `pygame.sprite.Sprite`.

---

### 💻 Ejemplos Mínimos

#### 1. Crear una Clase y Objetos

```python
class Estudiante:
    def __init__(self, nombre, apellido, edad):
        # Atributos: Guardamos la información
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        # Método: Una acción
        print(f"Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años.")

# Creamos dos objetos (instancias) diferentes con el mismo molde
estudiante1 = Estudiante("Ana", "Gomez", 20)
estudiante2 = Estudiante("José", "García", 15)

estudiante1.saludar()
```

#### 2. Uso de Herencia y `super()`

Cuando una clase hija tiene su propio `__init__`, debemos usar `super().__init__()` para no romper la conexión con el padre.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def correr(self):
        print(f"{self.nombre} está corriendo")

class Gato(Animal):
    def __init__(self, nombre, edad):
        # Llamamos al constructor del padre para guardar el nombre
        super().__init__(nombre)
        self.edad = edad

    def maullar(self):
        print("¡Miau, miau!")

gatito = Gato("Giacomino", 2)
gatito.correr()  # Heredado de Animal
gatito.maullar() # Propio de Gato
```

---

### 💡 Tips para curiosos

* **Variables con `**kwargs`**: En clases como `ListaPrecios`, podemos usar `**services` para recibir un número ilimitado de nombres y valores. Es muy útil para catálogos o inventarios.
* **El nombre de las clases**: Por convención, las clases siempre empiezan con **Mayúscula** (`Persona`), mientras que los objetos empiezan con **minúscula** (`p1`).

---

### 🚀 Reto para el Alumno

1. Crea una clase llamada `Mascota` con el atributo `nombre`.
2. Crea una clase hija llamada `Perro` que herede de `Mascota` y tenga un método `ladrar`.
3. ¡Instancia a **Arthur** y haz que ladre!

---
