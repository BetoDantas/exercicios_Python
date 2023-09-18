km=float(input("quantos km você percorrerá durante a viagem : "))
if km<=200:
    print("a sau passagem vai custar R${} ".format(km*0.50))
else :
    print(" sua passagem vai custar R$ {}".format(km*0.45))