print("-=-"*20)
print("{:^50}".format(" Progressão Aritmética "))
print("-=-"*20)

raz = int(input("Informe a razão: "))
y = int(input("Informe o primeiro Termo do intervalo: "))
z = int(input("Informe o segundo Termo do intervalo: "))
for c in range(y, z+1, raz):
    print(c,end=" ")
    print("->",end=" ")
print("Fim da Progressão")
