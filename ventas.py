
base = int(input('Sueldo base: $ '))
venta1 = int(input('Venta1: $ '))
venta2 = int(input('Venta2: $ '))
venta3 = int(input('Venta3: $ '))

comision = (venta1 + venta2 + venta3)*0.1
arecibir = base + comision

print('Comision: $', comision)
print('Sueldo a recibir: $', arecibir)
