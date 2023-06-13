import matplotlib.pyplot as plt

ent = open("dolarsal_2021.txt")
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

#Promedio para Junio
i = 0
cont = 0
suma = 0

while i < largo:
    if fechas[i][5:7] == "06":
        suma = suma + valores[i]
        cont = cont + 1
    i = i + 1
promedio = suma / cont
meses.append('Junio')
pesos.append(promedio)

#Promedio para Julio
i = 0
cont = 0
suma = 0
while i < largo:
    if fechas[i][5:7] == "07":
        suma = suma + valores[i]
        cont = cont + 1
    i = i + 1
promedio = suma / cont
meses.append('Julio')
pesos.append(promedio)

#Promedio para Agosto
i = 0
cont = 0
suma = 0
while i < largo:
    if fechas[i][5:7] == "08":
        suma = suma + valores[i]
        cont = cont + 1
    i = i + 1
promedio = suma / cont
meses.append('Agosto')
pesos.append(promedio)

#Promedio para Septiembre
i = 0
cont = 0
suma = 0
while i < largo:
    if fechas[i][5:7] == "09":
        suma = suma + valores[i]
        cont = cont + 1
    i = i + 1
promedio = suma / cont
meses.append('Septiembre')
pesos.append(promedio)
print(meses, pesos)

#Promedio para Octubre
i = 0
cont = 0
suma = 0
while i < largo:
    if fechas[i][5:7] == "10":
        suma = suma + valores[i]
        cont = cont + 1
    i = i + 1
promedio = suma / cont
meses.append('Octubre')
pesos.append(promedio)

#Promedio para Noviembre
i = 0
cont = 0
suma = 0
while i < largo:
    if fechas[i][5:7] == "11":
        suma = suma + valores[i]
        cont = cont + 1
    i = i + 1
promedio = suma / cont
meses.append('Noviembre')
pesos.append(promedio)
print(meses, pesos)

#Promedio para Diciembre
i = 0
cont = 0
suma = 0
while i < largo:
    if fechas[i][5:7] == "12":
        suma = suma + valores[i]
        cont = cont + 1
    i = i + 1
promedio = suma / cont
meses.append('Diciembre')
pesos.append(promedio)


print(meses)
print(pesos)
plt.title("Valor promedio mensual del dolar : 2022")
plt.xlabel('Meses')
plt.ylabel('Valores en $')
plt.grid(True)
plt.plot(meses, pesos, 'g*--')
plt.legend(loc="lower right", title="2021", frameon=False)
plt.show()


