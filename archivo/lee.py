ar = open("ejemplo.txt")
linea = ar.readline().rstrip('\n')
suma = ""
while linea != '':
    lista = linea.split(" ")
    print(lista)
    suma = suma + lista[1]
    linea=ar.readline().rstrip('\n')
print(suma)
ar.close()