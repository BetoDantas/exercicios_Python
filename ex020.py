from  random import shuffle
a1 = input('qual o primeiro aluno ? ')
a2 = input('qual o segundo alundo ? ')
a3 = input('qual o terceiro aluno ? ')
a4 = input('qual o quarto aluno? ')
v = [a1,a2,a3,a4]
shuffle(v)
print('a ordem do trabalho será :')
print(v)
