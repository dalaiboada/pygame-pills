def configurar_servidor(ip="127.0.0.1", puerto=8080):
  print("Conectado a", ip, "en", puerto)

configurar_servidor()                           # Usa los valores por defecto
configurar_servidor("192.168.1.1")              # Solo cambia el primero