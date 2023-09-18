cad = int(input(" Quantas pessoas deseja cadasrtar ? "))
sum = 0
maior_idade = 0
mulheres = sexo = 'f'
for c in range (0,cad):
    print("======[{}° Pessoa]===== ".format(c+1))
    nome = str(input("Nome: ")).strip().upper()
    idade = int(input("Idade: "))
    sexo=str(input("Sexo (M/F): ")).strip().upper()
    sum+=idade
    sexo.count("f")

print("\nA média de idade desse grupo é de {} anos".format((int(sum/cad))))
if idade > maior_idade:
    print("{} tem {} anos e é a pessoa mais velha desse grupo cadastrado".format(nome, idade))
if sexo == "F":
    print("há {} mulheres nesse grupo".format(sexo.count("f")))











