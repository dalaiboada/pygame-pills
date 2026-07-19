def reporte_ventas(*productos, **detalles):
  print("Productos:", productos)
  print("Detalles adicionales:", detalles)

reporte_ventas("Laptop", "Mouse", moneda="USD", fecha="2026-07-19")