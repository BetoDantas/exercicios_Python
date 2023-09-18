idade = int(input("Informe a idade do atleta: "))
if idade <=9:
    print("\nEste atleta pertence a categoria: MIRIN\n")
elif idade>9 and idade<=14:
    print("Este atleta pertence a categoria: INFANTIL\n")
elif idade>14 and idade<=19:
    print("Este atleta pertence a categoria: JUNIOR")
elif idade>19 and idade<=25:
    print("Este atleta pertence a categoria: SÊNIOR")
elif idade>25:
    print("Este atleta pertence a categoria: MASTER")


