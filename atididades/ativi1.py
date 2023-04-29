produtos = ["tomate","batata","limão"]
estoque = [100, 200,50]
min_estoque = [10,20,5]
for num in range(len(produtos)):
    print(f'O produto {produtos[num]} tem estoque {estoque[num]} e o estouque mínimo é {min_estoque[num]}')

prod = input("Digite o nome do produto: ")
qnt = int(input("Digite a quantidade do produto: "))
mini = int(input("Digite o minimo para este produto: "))

produtos.append(prod)
estoque.append(qnt)
min_estoque.append(mini)


for num in range(len(produtos)):
    if estoque[num] <= min_estoque[num]:
        print(f'Produto{produtos[num]} com quantidade mínima')

lista = []
for num in range(len(produtos)):
    lista.append([produtos[num], estoque[num], min_estoque[num]])
print(lista)

while True:
    busca = input("Digite o nome do produto para ser apagado: ")
    if busca in produtos:
        break
    else:
        print("Produto não encontradoo!!!")

ind = produtos.index(busca)
produtos.remove(busca)
estoque.remove(estoque[ind])
min_estoque.remove(min_estoque[ind])
print(produtos, estoque, min_estoque)

pedidos = []
while True:
    ped_prod = input("Digite o produto que deseja comprar: ")
    ped_qnt = input("Digite a quantidade de produtos: ")
    pedidos.append([ped_prod, ped_qnt])
    repete = input("Deseja continuar S/N: ")
    if repete.upper() == 'N':
        break
print(pedidos)

for itens in pedidos:
    if itens[0] not in produtos:
        print(f'Produto {itens[0]} não tem')
    elif itens [1] > estoque[produtos.index(itens[0])]:
        print("Saldo insuficiente!")