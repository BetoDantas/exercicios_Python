n = int(input(" Informe em que ano estamos: "))
cont1 = 0
cont = 0
for c in range(1,7):
    p = int(input("Em que ano a {} pessoa nasceu ?  ".format(c)))
    cont1+=p
if n-p>=18:
    print("há {} pessoas maior de idade ".format(cont1))

