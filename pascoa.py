total = float(0)
tamanho = int(input("informe o tamanho do ovo! 1=pequeno, 2=medio, 3= grande"))
if tamanho == 1:
    total = 7.80
elif tamanho ==2:
    total = 12.90
elif tamanho == 3:
    total = 23.95
    
sabor = int(input("informe o sabor do ovo! 1=choc preto, 2=cho branco, 3= choc ao leite"))
if sabor ==1:
    total = total + 9.67
elif sabor ==2:
    total = total = 4.50
elif sabor ==3:
    total = total + 9.32
else:
    print("produto inválido")

recheio = int(input("informe o recheio do ovo! 1=choc preto, 2= choc branco"))
if recheio ==1:
    total = total + 4.83
elif recheio ==2:
    total = total + 2.25
elif recheio ==3:
    total = total + (4.83/2) + (2.25/2)
else:
    print("produto inválido")

adicional = int(input("informe o segundo recheio! 1= kitkat, 2=m&m, 3= todos"))
if adicional ==1:
    total = total + 4.67
elif adicional ==2:
    total = total + 5.43
elif adicional ==3:
    total = total + 10.10

presente = int(input("informe se é presente ou entrega! 1=presente, 2= entrega"))
if presente ==1:
    total = total + 2.50
elif presente ==2:
    total = total + 5.00
pagamento = int(input("informe tipo de pagamento! 1=cartão, 2=din/pix"))
if pagamento == 1:
    total = total + 3.30
elif pagamento ==2:
    total = total *0.9

quantidade = int(input("informe quantidade de ovos"))
total = total * quantidade
print (total)

