frase = str(input("Digite uma frase : ")).strip().upper()
print("essa frase tem {} letra(s)".format(len(frase) - frase.count(" ")))
print("essa frase tem {} letras A".format(frase.count("A")))
print("a primeira letra [a] está na posição {}".format(frase.find("A")+1))
if frase.find("A")<=8:
    print("a ultima letra [a] está na posição {}".format(frase.rfind("A")))


