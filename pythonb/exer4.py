num = int(input("Infome um número CDU: "))

centena = num // 100
dezena = (num % 100) // 10
unidade = (num % 10)

print(num, "\nCentena:", centena, "\nDezena:", dezena, "\nUnidade:", unidade)