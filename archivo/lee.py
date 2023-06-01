ar = open("ejemplo.txt")
linea = ar.readline().rstrip('\n')
while linea != '':
    lista = linea.split(" ")
    print(lista)
    linea=ar.readline().rstrip('\n')
ar.close()