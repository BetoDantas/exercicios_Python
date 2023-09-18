num = int(input("digite um número intero : "))
print("escolha a forma que deseja ler esse número ")
menu = int(input("\n1 - binário\n2 - octal\n3 - hexadecimal\n sua opção: "))
if menu == 1:
    print("em binário {}".format(bin(num)[2:]))
elif menu == 2:
    print("em octal {}".format(oct(num)[2:]))
elif menu == 3:
    print("em hexadecimal {}".format(hex(num)[2:]))
else:
    print("opção inválida")
