sum = 0
cont = 0
for c in range(1,501,2):
    if c%3==0:
        sum+=c
        cont+=1
print("a soma dos valores deu {}".format(sum))
print("são {} multiplos de 3 ".format(cont))