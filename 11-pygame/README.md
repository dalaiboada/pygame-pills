# 🎮 Módulo: Pygame

Bienvenido al módulo de **Pygame**, donde aprenderemos los fundamentos de la programación de videojuegos 2D en Python.

---

## 📂 Contenido del Módulo

| Carpeta / Tema       | Nivel      | Descripción                                                                                                                      |
| :------------------- | :--------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| `01-setup_ventana` | 💚 Básico | Configuración de la ventana y ciclo principal. └─ 💡**Tips:** [Guía de configuración](./01-setup_ventana/Tips/configuracion_ventana.md) y [Guía de colores](./01-setup_ventana/Tips/guia_de_colores.md) |

---

## 🚀 Cómo usar este material

1. Asegúrate de tener Python instalado.
2. Instala Pygame:
   ```bash
   pip install pygame
   ```
3. Entra en la carpeta del ejemplo y ejecuta el archivo:
   ```bash
   python setup_ventana.py
   ```

---

## Estructura de un juego en Pygame

Todo juego en Pygame sigue esta estructura básica:

```
1. Inicialización      →  pygame.init()
2. Crear ventana       →  pygame.display.set_mode((ancho, alto))
3. Bucle principal     →  while ejecutando:
4. Gestionar eventos   →  pygame.event.get()
5. Dibujar             →  ventana.fill() / pygame.display.update()
6. Salir limpiamente   →  pygame.quit()
```

---

**Nota:** Estos ejemplos son puntos de partida. ¡Siéntanse libres de modificar el código y experimentar con sus propias mecánicas!
