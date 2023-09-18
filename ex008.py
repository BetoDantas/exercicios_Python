print('Você está querendo trocar a rede de fios de sua casa,\nmas para isso você deve comprar uma determinada quantidade de fios em metros. ')
metros = float(input('Quantos metros de fio você comprou? '))
mm = 1000*metros
cm = 100*metros
dm = 10*metros
dam = metros/10
hm = metros/100
km = metros/1000
print('E por motivo de curiosidade quer saber quanto vale essa medida em mm,cm,dm,dam,hm e km: ')
print('Então vou ajuda-lo.\nEm milímetros essa medida é {:.2f}mm,\nem centímetros essa medida é equivalente a {:.2f}cm e em decímetro é igual a {}dm'.format(mm,cm,dm))
print('Já em dacametro é {}dam, em hectometro vale {}hm \ne em km equivale a {}km'.format(dam,hm,km))
