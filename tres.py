# Resolver ax + b = c

a = int(input('Coeficiente a: '))
b = int(input('Coeficiente b: '))
c = int(input('Coeficiente c: '))

if a == 0:
    print('La ecuacion no se puede resolver')
else:
    x = (c - b)/a
    print('El valor de x es : ', x)
print('Fin del programa')
print('Chaooo')


