import matplotlib.pyplot as plt

ent = open("dolarsal.txt")
valores = []
fechas = []
linea = ent.readline().rstrip('\n')
while linea != '':
    lista = linea.split(" ")
    fecha = lista[0]
    valor = float(lista[1])
    fechas.append(fecha)
    valores.append(valor)
    linea = ent.readline().rstrip('\n')
ent.close()

largo = len(fechas)
meses = []
pesos = []

#Promedio para Enero
i = 0
cont = 0
suma = 0

while i < largo:
    if fechas[i][5:7] == "01":
        suma = suma + valores[i]
        cont = cont + 1
    i = i + 1
promedio = suma / cont
meses.append('Enero')
pesos.append(promedio)

#Promedio para Febrero
i = 0
cont = 0
suma = 0
while i < largo:
    if fechas[i][5:7] == "02":
        suma = suma + valores[i]
        cont = cont + 1
    i = i + 1
promedio = suma / cont
meses.append('Febrero')
pesos.append(promedio)

#Promedio para Marzo
i = 0
cont = 0
suma = 0
while i < largo:
    if fechas[i][5:7] == "03":
        suma = suma + valores[i]
        cont = cont + 1
    i = i + 1
promedio = suma / cont
meses.append('Marzo')
pesos.append(promedio)

#Promedio para Abril
i = 0
cont = 0
suma = 0
while i < largo:
    if fechas[i][5:7] == "04":
        suma = suma + valores[i]
        cont = cont + 1
    i = i + 1
promedio = suma / cont
meses.append('Abril')
pesos.append(promedio)
print(meses, pesos)

#Promedio para Mayo
i = 0
cont = 0
suma = 0
while i < largo:
    if fechas[i][5:7] == "05":
        suma = suma + valores[i]
        cont = cont + 1
    i = i + 1
promedio = suma / cont
meses.append('Mayo')
pesos.append(promedio)

print(meses)
print(pesos)
plt.title("Valor promedio mensual del dolar")
plt.plot(meses, pesos)
plt.show()


