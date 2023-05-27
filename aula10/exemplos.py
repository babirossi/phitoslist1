cidade = 'São Carlos'
endereco = 'Rua Cândido Padim, 25 - Vila Prado'
completo = cidade + endereco
print(cidade.startswith('São'))
print(cidade.endswith('los'))
print('Rua' in completo)
print('Avenida' not in completo)


texto = 'Python é uma linguagem de programação. Python é simples. Python é organizado. Python é uma excelente linguagem.'
print(texto.count('é'))
print(texto.find('Python',25,50))
print(texto.rfind('lingua'))
print(texto.index('é'))
print(texto.rindex('é'))

texto = 'BOLA ROXA'
fim = len(texto)
for i range(len(texto)):
    comeco = posicao
    print(texto.find('O', comeco+1, fim))
    posicao = texto.find('O')
