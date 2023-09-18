x = int(input("Digite um número inteiro : "))
y = int(input("Digite outro número inteiro : "))
z = int(input("Digite mais um número inteiro : "))
if x<y and x>y:
    print("{} é o maior".format(x))
if y>x and y>z:
    print(" {} é o maior ".format(y))
if z>x and z>y:
    print("{} é o maior".format(z))
