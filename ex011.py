largura = float(input('qual a largura dessa parede (em metros)? metros '))
altura = float(input('qual a altura dessa parede (em metros)? metros '))
area = largura * altura
litros = area/2
print('essa parede tem {:.2f}m²'.format(area))
print('sabe-se que cada litro de tinta pinta 2m², logo você precisará de {}l de tinta para pintar essa parede.'.format(litros))
