from datetime import date
atual = date.today().year
nas = int(input("Informe sua data de nascimento : "))
idade = atual - nas
print("\nVocê tem {} anos ".format(idade))
if idade<18:
    print("\nVocê se alistará em {}".format(atual+(18-idade)))
elif idade==18:
    print("\nSeu alistamento será este ano")
elif idade>18:
    print("\nSeu período de alistamento foi em {}".format(atual-(idade-18)))
    print("Aliste-se AGORA MESMO!!!")