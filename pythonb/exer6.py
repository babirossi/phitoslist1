salario = int(input("Informe seu salário minimo: "))
watts = int(input("Quantidade de quilowatts: "))

result =  (salario / 7)
result2  = (result / watts)
result3 = (result * watts)
desconto = (0.1 * result3)
desconto2 = (result3 - desconto)

print ("O valor do quilowatt: ", result2)
print ("valor a pagar: ", result3)
print ("O valor a ser pago com um desconto de 10% é: ", desconto2)