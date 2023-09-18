sexo =str(input("informe seu sexo (digite F para feminino e M para masculino): "))
h = float(input("informe sua altura (em metros): "))
if sexo == "M" or sexo == "m":
    print(" Seu peso ideal é {:.2f}".format(72.7*h-58))
else:
    print("Seu peso ideal é {:.2f}".format(62.1*h- 44.7))

