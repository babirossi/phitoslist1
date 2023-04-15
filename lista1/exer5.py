num = int(input("Infome um número CDU: "))

unidade = (num % 10)
dezena = (num % 100) // 10
centena = num // 100
print(num, "\nUnidade", unidade, "\nDezena:", dezena, "\nCentena:", centena)