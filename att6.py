lista_convidados= ['Neymar','Messi','Cristiano','Mbappe','Vini jr']
for convidados in lista_convidados:
    print(convidados,'você foi convidado paro o jantar.')
lista_naopresentes= ['Neymar']
for naovai in lista_naopresentes:
    print(naovai,'desistiu de ir')
lista_convidados.insert(0,'gabigol')
del lista_convidados[1]
print('Gabigol, você foi convidado para o jantar.')
for vdd in lista_convidados:
    print(vdd,'o jantar ainda está de pé!')