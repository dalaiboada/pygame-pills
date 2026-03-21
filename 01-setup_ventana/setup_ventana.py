import pygame

pygame.init()

# Ventana
ANCHO = 400
ALTO = 200

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Píldora 1: Mi Primera Ventana")

ejecutando = True

# Bucle principal
while ejecutando:
    # Eventos
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: # cerrar la ventana
            ejecutando = False 

    # Renderizado
    ventana.fill("royalblue")

    pygame.display.update()

pygame.quit()