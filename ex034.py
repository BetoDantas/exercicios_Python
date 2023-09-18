sal = float(input("informe o seu salário : "))
if sal > 1250:
    print("seu novo salário com um aumneto de 10% é R${}".format(sal+(sal*0.10)))
else:
    print("o seu salário com aumento de 15% é R${}".format(sal+(sal*0.15)))