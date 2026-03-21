## 🎨 Guía de Colores en Pygame

En Pygame, un color se define mediante el sistema **RGB** (Red, Green, Blue).

### 1. Colores por Nombre (Strings)
Pygame reconoce más de 600 nombres de colores estándar. Es la forma más fácil de empezar porque no necesitas recordar números.

**Ejemplos de prueba:**
* `ventana.fill("royalblue")` (Un azul vibrante)
* `ventana.fill("firebrick")` (Un rojo oscuro elegante)
* `ventana.fill("gold")` (Amarillo brillante)
* `ventana.fill("forestgreen")` (Verde naturaleza)

### 2. Colores Personalizados (Tuplas RGB)
Si quieres un color exacto que no tiene nombre, usamos una **tupla** con tres números. Cada número va del **0** (apagado) al **255** (máxima intensidad).

$$Color = (Rojo, Verde, Azul)$$

| Color | Tupla RGB | Resultado |
| :--- | :--- | :--- |
| **Negro** | `(0, 0, 0)` | Ausencia total de luz. |
| **Blanco** | `(255, 255, 255)` | Máxima intensidad de los tres. |
| **Gris Medio** | `(128, 128, 128)` | Intensidad a la mitad. |
| **Rosa Neón** | `(255, 20, 147)` | Mucho rojo, poco verde, algo de azul. |



---

### 🛠️ Cómo implementarlo en el código

Para mantener el código limpio, es una **buena práctica** definir tus colores como constantes al principio del archivo (debajo de las dimensiones de la ventana).

```python
# --- Definición de Colores ---
# Puedes usar nombres
COLOR_FONDO = "darkslategray"

# O puedes crear tus propios colores RGB
NARANJA_CLARO = (255, 165, 0)
VERDE_MINT = (152, 255, 152)
MORADO_SUAVE = (150, 120, 200)

# --- En el Bucle Principal ---
ventana.fill(NARANJA_CLARO) # Usando la variable personalizada
```

---

### 📚 Recursos y Documentación

Para encontrar el color perfecto, puedes consultar estos enlaces:

* **[Lista Oficial de Nombres en Pygame](https://www.pygame.org/docs/ref/color_list.html):** Aquí están todos los nombres de texto que Pygame entiende (como "aquamarine" o "burlywood").
* **[Selector de Color de Google](https://www.google.com/search?q=color+picker):** Puedes elegir un color visualmente y copiar el código **RGB** (ej: 255, 87, 51) para usarlo en tu tupla.
* **[Adobe Color](https://color.adobe.com/):** Ideal para que aprendas a crear paletas de colores que combinen bien entre sí.
