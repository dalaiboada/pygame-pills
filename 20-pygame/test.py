from pygame import *

ventana = display.set_mode((400, 200))

while True:
  for evento in event.get(): 
    if evento.type == QUIT:
      quit()
      exit()

  display.update()

quit()