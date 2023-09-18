from datetime import date

ano=int(input("Em qual ano estamos ? Para analisarmos o ano atual digite 0 : "))
if ano == 0 :
    ano = date.today().year
bissexto =  ano % 4
if bissexto == 0:
    print(" esse é um ano bissexto ")
else :
    print (" esse ano não é bissexto :( ")
