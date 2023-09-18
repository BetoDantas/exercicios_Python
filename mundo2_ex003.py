x = int(input("digite um npumero inteiro: "))
y = int(input("\ndigite outro número inteiro:  "))
if x>y:
    print("{} é maior que {}".format(x,y))
elif x==y:
    print("{} é igual a {}".format(x,y))
else:
    print("\n{} é maior que {}".format(y,x))