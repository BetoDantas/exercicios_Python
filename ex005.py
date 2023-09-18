n1 = float(input('digite um numero : '))
n2 = float(input('digite outro numero : '))
soma = n1+n2
subtracao = n1-n2
multiplicacao = n1*n2
divisao = n1/n2
divisaointeira = n1//n2
restodadivisao = n1%n2
potencia = n1**n2
raiz = n1**(1/n2)
print('a soma vale {} \na subtração vale {} \na multiplicação vale {}'.format(soma,subtracao,multiplicacao))
print('a divisão vale {} \na divisão inteira vale {} \no resto da divisão é {}'.format(divisao,divisaointeira,restodadivisao))
print('a potencia é igual a {}  \na raiz quadrada vale {:.2f}'.format(potencia,raiz))
