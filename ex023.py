n1 = int(input('digite um número de 0 a 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000%10
print('analisando o numero...')
print('esse numero tem {} unidae(s) '.format(u))
print('esse numero tem {} dezena(s) '.format(d))
print('esse numero tem {} centena(s)'.format(c))
print('esse numero tem {} milhar'.format(m))


