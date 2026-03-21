# 📁 Carpeta: `pills/01-setup-ventana/`

### 💊 Píldora 1: Configuración de la Ventana

En esta primera píldora aprenderemos los cimientos de cualquier juego en Pygame:
**cómo abrir una ventana, mantenerla abierta y cerrarla correctamente.**

---

### 📘 Conceptos Fundamentales

#### El "Game Loop" (Bucle de Juego)

Un videojuego no es una aplicación estática; es un programa que se ejecuta muchísimas veces por segundo (generalmente 60). En cada vuelta del bucle, el ordenador:

1. **Revisa qué pulsaste** (Entradas/Input).
2. **Calcula posiciones** (Lógica/Update).
3. **Dibuja los cambios** (Renderizado).

#### El Sistema de Eventos

Pygame guarda todas las acciones del usuario (teclado, ratón, cerrar ventana) en una "cola" o lista. Es nuestra responsabilidad vaciar esa lista en cada fotograma usando `pygame.event.get()`.

---

### 🛠️ Glosario de Funciones Usadas

| Función                                             | Descripción                                                                                            |
| :--------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| **`pygame.init()`**                          | Inicializa todos los módulos internos de Pygame. Debe ir siempre al principio.                         |
| **`pygame.display.set_mode((ancho, alto))`** | Crea la ventana de juego. Nota los**dobles paréntesis**: espera una "tupla" con las dimensiones. |
| **`pygame.display.set_caption("Texto")`**    | Define el título que aparecerá en la barra superior de la ventana.                                    |
| **`ventana.fill("color")`**                  | Borra todo lo anterior pintando la pantalla de un solo color.                                           |
| **`pygame.display.update()`**                | Actualiza la ventana física para mostrar lo que hemos dibujado en la memoria de la computadora.        |
| **`pygame.quit()`**                          | Cierra los módulos de Pygame de forma segura cuando terminamos el bucle.                               |

---

### 🚀 Reto para el Alumno

1. Cambia el tamaño de la ventana a **1280x720** (HD).
2. Busca en la documentación o prueba nombres de colores y cambia el fondo a `"skyblue"` o `"indianred"`.

   Para aprender más sobre cómo personalizar el aspecto de tu ventana, revisa nuestra:
   [Guía de Colores y Personalización](./Tips/guia_de_colores.md "Click para ver la Guía")
3. Cambia el título de la ventana por tu propio nombre.

---

## 2. `setup_ventana.py` (Código Comentado)

```python
import pygame

# 1. CONFIGURACIÓN E INICIALIZACIÓN
# Preparamos los motores de Pygame
pygame.init()

# Definimos constantes para las dimensiones (Buena práctica: en mayúsculas)
ANCHO = 800
ALTO = 600

# Creamos la superficie principal de dibujo (la ventana)
# Usamos dobles paréntesis porque set_mode espera una tupla (x, y)
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Le damos un título a nuestra ventana
pygame.display.set_caption("Pygame Pills: Mi Primera Ventana")

# Esta variable controla si el bucle sigue corriendo
ejecutando = True

# 2. BUCLE PRINCIPAL (GAME LOOP)
while ejecutando:
  
    # --- GESTIÓN DE EVENTOS (ENTRADAS) ---
    # Revisamos la lista de cosas que han pasado
    for evento in pygame.event.get():
        # Si el evento detectado es que el usuario pulsó la [X] de cerrar
        if evento.type == pygame.QUIT:
            ejecutando = False

    # --- DIBUJO (RENDERIZADO) ---
    # Paso 1: Limpiar el lienzo con un color de fondo
    # Puedes usar nombres como "black", "white", "red", "steelblue", etc.
    ventana.fill("darkslategray")

    # Paso 2: Mostrar lo que hemos dibujado en el monitor
    pygame.display.update()

# 3. FINALIZACIÓN
# Cerramos Pygame y liberamos los recursos del sistema
pygame.quit()
```

---
