texto = input("Digite um texto: ")
espacos = texto.count(" ")
vogais = 0
vogais += texto.lower().count("a")
vogais += texto.lower().count("e")
vogais += texto.lower().count("i")
vogais += texto.lower().count("o")
vogais += texto.lower().count("u")

print("Quantidade de espaços em branco:", espacos)
print("Quantidade de vogais (a, e, i, o, u):", vogais)