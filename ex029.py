print('-=-'*20)
print('{:<20}RADAR ELETRONICO'.format(""))
print('-=-'*20)
x = int(input("qual a velocidade do carro em km/h ? "))
if x>80:
    print("você está acima da velocidade permitida!! ")
    print("a sua multa será de R$ {}".format((x-80)*7))
else :
    print("você está andando em uma velocidade permitida na pista")
