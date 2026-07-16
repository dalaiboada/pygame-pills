archivo = "  documento.txt  "

limpio = archivo.strip()
print("Limpio:", limpio)

if limpio.endswith(".txt"):
    print("Es un archivo de texto.")

partes = limpio.split(".")
print("Nombre y extensión:", partes)