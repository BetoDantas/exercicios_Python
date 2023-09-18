print("-=-"*20)
print("                JOGO DO PAR OU ÍMPAR           ")
print("-=-"*20)
par= int(input("digite um número inteiro para eu lhe dizer se é par ou ímpar : "))
x = par%2
if x==0:
    print("\n{} é um número par".format(par))
else:
    print("\n{} é um número ímpar".format(par))