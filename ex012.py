preço = float(input('Qual o preço do produto? R$ '))
desconto = preço * 0.05
newpreço = preço - desconto
print('O produto com 5% de desconto custa {:.2f}R$'.format(newpreço))
