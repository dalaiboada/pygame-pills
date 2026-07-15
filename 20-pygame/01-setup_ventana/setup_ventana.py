from pygame import *

# Ventana
ANCHO = 400
ALTO = 200

ventana = display.set_mode((ANCHO, ALTO))
display.set_caption("Mi Primera Ventana")

ejecutando = True

# Bucle principal
while ejecutando:
    # Eventos
    for evento in event.get(): 
        if evento.type == QUIT: # cerrar la ventana
            ejecutando = False 

    # Renderizado
    ventana.fill("royalblue")

    display.update()

quit()