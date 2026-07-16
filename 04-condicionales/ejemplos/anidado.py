# Programa: Verificar acceso basándose en edad Y membresía
edad = 20
tiene_membresia = True

if edad >= 18:
    # Este if está dentro del primero (anidado)
    if tiene_membresia:
        print("Acceso VIP concedido.")
    else:
        print("Acceso estándar concedido.")
else:
    print("Acceso denegado: debes ser mayor de edad.")