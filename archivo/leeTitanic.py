ent = open('titanic3.txt')
sal = open('titanicClean.txt','w')
linea = ent.readline().rstrip('\n')
while linea!='':
    lista = linea.split(',')
    nombre = lista[2]+lista[3]
    print(nombre)
    dato = lista[0]+','+lista[1]+','+nombre+','+lista[4]+','+lista[5]+','+lista[6]+','+lista[7]+','+lista[8]+','+lista[9]+','+lista[10]+','+lista[11]+','+lista[12]+','+lista[13]+','+lista[14]+','+lista[15]+'\n'
    sal.write(dato)
    linea = ent.readline().rstrip('\n')
sal.close()
