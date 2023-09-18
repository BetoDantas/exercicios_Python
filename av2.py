a= int(input("digite um número: "))
b=int(input("digite outro numero: "))
c=int(input("digite mais um numero: "))
if a>b and a>c and b>c :
    print(c,b,a)
elif b>a and b>c and a>c:
    print(c,a,b)
elif c>a and c>b and b>a:
    print(a,b,c)
elif b>a and a<c :
    print(a,c,b)
elif c>a and a>b:
    print(b,a,c)