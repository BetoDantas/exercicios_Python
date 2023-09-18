from random import choice
from time import sleep
print('-=-' * 20 )
print('{}ADVINHA MISERA'.format(' ' * 10 ))
print('-=-' * 20 )
n = choice([0,1,2,3,4,5])
n1 = int(input('digite um numero  inteiro de 0 a 5 e veja se consegue acerta : '))
print('HUMMMM...')
sleep(2)
if n1==n:
    print('SORTE DE PRINCIPIANTE XD')
    print('pensei no {} tbm'.format(n))
else:
    print('\nmais sorte na proxima... kkk')
    print('\no numero em que pensei foi {} '.format(n))



