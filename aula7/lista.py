lista = ['A', 'B', 'C', 6]
print (lista[-2])
#numero positivo vai contar de frente para traz
#numero negativo vai contar de tras para frente 

lista.append('E')
print(lista)

lista  = lista + ['F', 'G']
print(lista)

#adiciona na posição que eu colocar

lista.insert (3, 'casa')
print(lista)

#remove o que você colovcar no comando 
lista.remove('casa')
print(lista)

lista2 = [2,3,5,21,1,41,25,123,54,4]
lista2.sort(reverse=True)
print(lista2)

#Contar quantos letra ou número tem 
print(lista)
print(lista.count('A'))

#coloca a letra em baixo 
var = lista.pop(0)
print(lista)
print(var)

#deleta o tanto que voc?ê colocar 
del lista[2:4]
print(lista)

#limpa a lista inteira
lista.clear
print(lista)