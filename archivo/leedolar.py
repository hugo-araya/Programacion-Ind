ent = open("dolar.txt")
sal = open("dolarsal.txt", "w")

linea = ent.readline().rstrip('\n')
while linea != '':
    lista = linea.split("\t")
    if lista[1] != '':
        fecha = lista[0]
        valor = lista[1]
        valor = valor.replace(',','.')
        sal.write(fecha+" "+valor+'\n')
    linea = ent.readline().rstrip('\n')
ent.close()
sal.close()
