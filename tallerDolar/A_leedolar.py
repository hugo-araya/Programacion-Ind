ent = open("dol_2021.txt")
sal = open("dolarsal_2021.txt", "w")

linea = ent.readline().rstrip('\n')
while linea != '':
    lista = linea.split("\t")
    if lista[1] != '':
        fecha = lista[0]
        valor = lista[1]
        valor = valor.replace('.', '')
        valor = valor.replace(',','.')
        lisfecha = fecha.split('.')
        if lisfecha[1] == 'ene':
            mes = '01'
        if lisfecha[1] == 'feb':
            mes = '02'
        if lisfecha[1] == 'mar':
            mes = '03'
        if lisfecha[1] == 'abr':
            mes = '04'
        if lisfecha[1] == 'may':
            mes = '05'
        if lisfecha[1] == 'jun':
            mes = '06'
        if lisfecha[1] == 'jul':
            mes = '07'
        if lisfecha[1] == 'ago':
            mes = '08'
        if lisfecha[1] == 'sept':
            mes = '09'
        if lisfecha[1] == 'oct':
            mes = '10'
        if lisfecha[1] == 'nov':
            mes = '11'
        if lisfecha[1] == 'dic':
            mes = '12'
        fecha = lisfecha[2]+'/'+mes+'/'+lisfecha[0]
        sal.write(fecha+" "+valor+'\n')
    linea = ent.readline().rstrip('\n')
ent.close()
sal.close()
