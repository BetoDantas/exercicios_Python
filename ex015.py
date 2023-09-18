dias = float(input('Quantos dias o carro foi alugado?  '))
km = float(input('Quantos km o carro percorreu ? '))
valor = dias*60 + km*0.15
print('o valor do aluguel ficou {:.2f}R$'.format(valor))


