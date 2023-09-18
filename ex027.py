nome = str(input("qual seu nome completo ? ")).strip().upper()
n = nome.split()
m = nome.split()
print("o seu primeiro nome é {}".format(n[0]))
if len(m)<=9:
    print("o seu ultimo nome é {}".format(n[len(m)-1]))
else:
    print("o seu ultimo nome é {}".format(n[len(n)+1]))
