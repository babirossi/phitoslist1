def verific(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'
    
Valor = float(input("Digite um número: "))
resultado = verific(Valor)
print(f'O sinal do valor é: {resultado}')