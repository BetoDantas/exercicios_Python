a = float(input("digite o comprimento de uma reta : "))
b = float(input("digite o valor de uma segunda reta : "))
c = float(input("digte o valor da terceira reta : "))
if a+b > c and c+b > a and a+c > b:
    print(" essas retas formam um triângulo ")
else:
    print("essas retas não formam um triângulo ")