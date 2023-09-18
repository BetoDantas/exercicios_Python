import random

lista = ["pedra", "papel","tesoura"]
maquina = (random.choice(lista))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
op=str(input("Escolha\npedra\npapel\ntesoura:\n "))
print(maquina)
if op=="pedra" and maquina=="papel":
    print("Você Perdeu")
elif op=="pedra" and maquina=="tesoura":
    print("Você Venceu ")
elif op=="pedra" and maquina=="pedra":
    print("Empate")
elif op=="papel" and maquina=="pedra":
    print("você venceu")
elif op=="papel" and maquina=="tesoura":
    print("você perdeu")
elif op=="papel" and maquina=="papel":
    print("empate")
elif op == "tesoura" and maquina == "pedra":
    print("você perdeu")
elif op == "tesoura" and maquina == "papel":
    print("você venceu")
elif op == "tesoura" and maquina == "tesoura":
    print("empate")


