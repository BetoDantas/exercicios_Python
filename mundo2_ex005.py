nota1 = float(input("Informe sua primera nota: "))
nota2 = float(input("\nInforme sua segunda nota: "))
media = (nota1+nota2)/2
print("\nSua média foi de {:.2f} ".format(media))
if media<7:
    print("média inferior a 7\nSituação: Reprovado ")
elif media>=7:
    print("Parabéns\nVocê passou de ano")