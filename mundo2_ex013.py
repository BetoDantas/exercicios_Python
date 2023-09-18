print("{:=^50}".format(" TABUADA "))
n = int(input("Informe o qual tabuada você quer: "))
for c in range(1,11):
    print("{} x {} = {}".format(n,c,c*n))
