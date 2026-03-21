import pygame

pygame.init()

ventana = pygame.display.set_mode((400, 200))

while True:
  for evento in pygame.event.get(): 
    if evento.type == pygame.QUIT:
      pygame.quit()
      exit()

  pygame.display.update()

pygame.quit()