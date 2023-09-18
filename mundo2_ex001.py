casa = float(input("qual o valor da casa ? R$"))
sal = float(input("quanto você ganha ? R$"))
anos = int(input("em quantos anos você pretende pagar ? "))
parcela = (casa/anos)/12

if parcela > sal*0.3:
    print("infelizmente você não pode financiar essa casa ")
    print("esssa aprcela excedeu 30% na sua cota salarial")
else:
    print("parabéns pelo seu imóvel !!!")
    print("suas parcelas serão de R${:.2f} ao mês".format(parcela))
