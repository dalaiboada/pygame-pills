# 🚀 Configuración Avanzada de la Ventana

Si ya dominas cómo abrir una ventana básica, es hora de aprender a controlar cómo se comporta en el sistema operativo. Pygame nos permite modificar desde el icono hasta si la ventana se puede estirar o no.

### 🚩 Las "Flags" (Banderas) de Pantalla

Las banderas son indicadores que le pasan instrucciones extra a `pygame.display.set_mode()`. Se colocan después del tamaño de la ventana.

| Propiedad                      | Código en Pygame     | ¿Qué hace?                                                              |
| :----------------------------- | :-------------------- | :------------------------------------------------------------------------ |
| **Pantalla Completa**    | `pygame.FULLSCREEN` | El juego ocupa todo el monitor.                                           |
| **Sin Bordes**           | `pygame.NOFRAME`    | Quita la barra superior (cerrar, minimizar).                              |
| **Redimensionable**      | `pygame.RESIZABLE`  | Permite que el usuario cambie el tamaño con el ratón.                   |
| **Escalado Inteligente** | `pygame.SCALED`     | Ajusta la resolución a pantallas modernas (4K/Retina) sin verse borroso. |

#### 🛠️ Ejemplo: Ventana Redimensionable

```python

# Ventana de 800x600 que el usuario puede estirar
ventana = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

```

> **Tip para Pro:** Si quieres usar varias banderas a la vez, únalas con el símbolo: ``|`` (llamado "pipe"):
>
>
> `ventana = pygame.display.set_mode((800, 600), pygame.FULLSCREEN | pygame.SCALED)`

---

### 🖼️ Personalizando el Icono

Por defecto, Pygame muestra un logo genérico. Para cambiarlo, necesitas una imagen pequeña (preferiblemente de **32x32** o **64x64** píxeles).

```python
# 1. Cargamos la imagen desde nuestra carpeta
icono = pygame.image.load("./01-setup_ventana/nombre_imagen.png")

# 2. Se la asignamos a la ventana
pygame.display.set_icon(icono)
```

---

### 🖱️ Control del Cursor (Ratón)

A veces, en juegos de terror o de disparos, no queremos que el cursor del sistema distraiga al jugador.

* **Ocultar el ratón:** `pygame.mouse.set_visible(False)`
* **Bloquear el ratón dentro del juego:** `pygame.event.set_grab(True)`
  *(Esto evita que el ratón se salga de la ventana, ideal para juegos de mucha acción).*

---

### 🕵️ ¿Cómo ver la info de la ventana actual?

Si en algún momento del código necesitas saber qué tamaño tiene la ventana (porque el usuario la redimensionó, por ejemplo), puedes usar:

```python
ancho_actual = ventana.get_width()
alto_actual = ventana.get_height()
```

---

### 💡 Reto para Curiosos

Intenta crear una ventana que sea `RESIZABLE`. Luego, dentro del **Bucle Principal**, imprime por consola el ancho y el alto cada vez que cambies el tamaño de la ventana con el ratón. ¿Ves cómo cambian los números en tiempo real?
