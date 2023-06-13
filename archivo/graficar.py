import matplotlib.pyplot as plt

ent = open("dolarsal_2022.txt")
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

plt.title("Valor dolar")
plt.plot(valores)
plt.show()


