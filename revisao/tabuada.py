geralacertos = 0
geralerros =0
while True:
  acertos = 0
  erros =0
  numero = int(input('Digite o numero para treinar a tabuada '))
  for x in range(1,11):
      resultado = numero * x
      respota = int(input(f'Digite a resposta de {numero} x {x} ='))
      if respota == resultado:
        print('ACERTOU!!')
        acerto =acerto +1
      else:
        print(f'ERROU o resultado de {numero} x {x} = {resultado}')
        erros = erros +1
  print(f'Acertos {acerto} - Erros {erros}')
  geralerros = geralerros + erros
  geralacertos = geralacertos +acertos
  continuar = input('Desenja parar (S/N)')
  if continuar.upper() == 'S':
    break
print(f'Acertos {geralacertos} - Erros {geralerros}')

     
