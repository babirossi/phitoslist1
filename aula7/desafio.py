lista = []
listaPar = []
listaImpar = []
somaPar = 0
somaImpar = 0
while True:
    adicionar = int(input("Informe um numero: (0 para sair): "))

    lista.append(adicionar)
    print(lista)

    if (adicionar == 0):
        break

#percorrendo a lista
for x in lista:
    if x%2==0:
        listaPar.append(x)
        somaPar+=x
    else:
        listaImpar.append(x)
        somaImpar+=x
listaPar.sort()
listaImpar.sort()
print("\n")
print("°" * 60)
print(f'Os numeros pares são: {listaPar} e sua somatoria é {somaPar}')
print(f'Os numeros impares são: {listaImpar} e sua somatoria é {somaImpar}')
print("°" * 60)
