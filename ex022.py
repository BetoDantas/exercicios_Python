nome = str(input('Digite o seu nome completo : ')).strip()
print('O seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
nome1 = nome.split()
print('seu primeiro nome é {} e tem {} letras'.format(nome1[0],len(nome1[0])))
















