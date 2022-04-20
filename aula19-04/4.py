numero = int(input("Digite um valor para saber a tabuada: "))

for i in range(11):
    print("{} * {} = {}".format(numero,i,(numero*i)))