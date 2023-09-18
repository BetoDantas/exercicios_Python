peso = float(input("Informe qunatos KG você possui: "))
altura = float(input("Informe sua altura: "))
imc = peso/(altura**2)
if imc<18.5:
    print("imc {:.2f}, desnutrido".format(imc))
elif imc>=18.5 and imc<25:
    print(" \nimc {:.2f}, tá sarado(a) ".format(imc))
elif imc>=25 and imc<=30:
    print("\nimc {:.2f}, ta gordinho".format(imc))
elif imc>=31 and imc<=40:
    print("\nimc {:.2f}, obesidade".format(imc))
elif imc>40:
    print("\nobesidade Morbida, imc {:.2f}".format(imc))
