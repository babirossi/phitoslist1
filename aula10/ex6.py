numero = input("Digite o número de telefone: ")
numero = numero.replace("-", "")

if len(numero) == 8:
    numero = "9" + numero

if len(numero) == 9:
    numero = numero[:5] + "-" + numero[5:]
print("Número de telefone corrigido:", numero)