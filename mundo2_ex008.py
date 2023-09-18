preco = float(input("Informe o valor do valor da compra EX(R$19.99): R$ "))
pagamento = str(input("Informe a forma de pagamento ( Dinheiro (A vista), Cartão (A vista ou parcelado) ou Cheque (A vista) ): "))
y = str(input("informe se deseja parcelar, sim/não (disponível apenas para cartão): "))
if y=="sim" and pagamento=="cartão":
    vezes=int(input("\nInforme em qunatas vezes deseja parcelar (OBS: parcelamentos acima de 3x recebem juros): "))
    if vezes>=3:
        print("Suas parcelas serão de R${:.2f} ao mês".format((preco/vezes)*1.20))
elif y=="não" and pagamento=="dinheiro":
    print("Você recebeu um desconto de 10%\no valor do produto ficou R${:.2f}".format(preco-(preco*0.1)))
elif y=="não" and pagamento=="cartão":
    print("Você recebeu um desconto de 5%\novalor do produto ficou R${:.2f}".format(preco-(preco*0.05)))
elif y == "não" and pagamento == "cheque":
    print("Você recebeu um desconto de 10%\no valor do produto ficou R${:.2f}".format(preco - (preco * 0.1)))







