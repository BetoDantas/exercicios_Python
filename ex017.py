co = float(input('Digite a medida do cateto oposto  (somente os numeros): '))
ca = float(input('Digite a medida do cateto adjacente  (somente os numeros):  '))
hip = ((co**2) + (ca**2))**(1/2)
print('a hipotenusa vale {:.2f}'.format(hip))
