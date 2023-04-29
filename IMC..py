peso = float(input ("informe seu peso"))
altura = float(input("informe sua altura"))
imc = peso/altura*altura
if imc<18.5:
    print("magreza)")
elif imc >=18.5 and imc <24.9:
        print("normal")
elif imc >=24.9 and imc <29.9:
    print("sobrepeso")
elif imc <=29.9 and imc <34.9:
    print("obesidade1")
else:
    print("obesidade2")


