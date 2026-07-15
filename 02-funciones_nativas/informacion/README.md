# 🔍 Funciones de Información y Análisis

Estas funciones nos ayudan a entender qué tenemos entre manos cuando el código se complica.

| Función | ¿Qué hace? | Ejemplo |
| --- | --- | --- |
| **`len(x)`** | Devuelve la longitud (cantidad de elementos). | `len("Hola")` → `4` |
| **`type(x)`** | Indica qué tipo de dato es `x`. | `type(10)` → `<class 'int'>` |
| **`id(x)`** | Muestra la dirección única en memoria de `x`. | `id(10)` → `1407...` |
| **`dir(x)`** | Lista todos los métodos y atributos de `x`. | `dir("abc")` → `['__add__', ...]` |
| **`help(x)`** | Muestra la documentación de `x`. | `help("abc")`, `help("abc".upper)` → `Help on method upper...` |

> **💡 TIP:**
> * Usa **`type()`** si sospechas que una variable no es del tipo que esperabas.
> * Usa **`dir()`** cuando quieras descubrir qué puedes hacer con un objeto (por ejemplo, qué métodos tiene una cadena).

### Ejemplos de uso
Prueba con los siguientes ejemplos en tu intérprete de Python:
    ├── [🐍 Longitud de una cadena (len)](./ejemplos/longitud.py)
    ├── [🐍 Tipo de dato (type)](./ejemplos/tipo.py)
    ├── [🐍 Dirección en memoria (id)](./ejemplos/direccion_memoria.py)
    ├── [🐍 Métodos y atributos (dir)](./ejemplos/metodos.py)
    └── [🐍 Documentación (help)](./ejemplos/documentacion.py)