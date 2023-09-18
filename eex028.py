from random import choice
n =[0,1,2,3,4,5]
print("-=-"*20)
print("                    ADIVINHA                      ")
print("-=-"*20)
print( "Tente adivinhar qual número eu estou pensando !" )
print("para ficar mais fácil vou dar uma dica. \na dica é a seguinte... é um número de 0 a 5.")
n1 = int(input("Qual número eu estou pensando ? "))
n2 = choice(n)
if n1== n2:
    print("UAU PARABÉNS VOCÊ ACERTOU EM CHEIO!!!")
else:
    print("EROOOOU! ")
    print("o número era {}".format(n2))
