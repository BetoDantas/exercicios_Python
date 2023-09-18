
n = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
     'treze','catorze','quize','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    intervalo = int(input("Digite um número entre 0 e 20: "))
    if 0<=intervalo<=20:
        print("O número digitado foi {}".format(n[intervalo]))
        break
    elif intervalo>20:
        print("\ntente novamente, ",end = '')
    elif intervalo<0:
       print("\nTente novamente, ",end ="")





