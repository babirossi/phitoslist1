texto1 = input('Digite o primero texto: ')
texto2 = input('Digite o segundo texto: ')

tamanho_texto1 = len(texto1)
tamanho_texto2 = len(texto2)

tamanhosiguais = tamanho_texto1 == tamanho_texto2

conteudo = texto1 == texto2

print("Conteúdo da primeira string:", texto1)
print("Comprimento da primeira string:", tamanho_texto1)

print("Conteúdo da segunda string:", texto2)
print("Comprimento da segunda string:", tamanho_texto2)

# Verifica se as strings têm o mesmo comprimento e são iguais ou diferentes no conteúdo
if tamanhosiguais:
    if conteudo:
        print("As duas strings têm o mesmo comprimento e são iguais no conteúdo.")
    else:
        print("As duas strings têm o mesmo comprimento, mas são diferentes no conteúdo.")
else:
    print("As duas strings têm comprimentos diferentes.")