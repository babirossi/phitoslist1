x = int(input("\nInsira a largura da peça:"))
y = int(input("\n Insira a altura da peça: "))
m = int(input("\n Insira quantidade de peças no estoque:"))
i = 1
while i <= m:
    xi = int(input("\nqual a largura da peça do cliente:"))
    yi = int(input("\nQual a altura da peça do cliente:"))
    if xi > x or xi >y or yi > x or yi > y:
        print ("\nNão cabe")
    else:
        print("\nCabe")
