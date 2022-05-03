base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

resultado = base
for i in range(expoente-1):
    resultado *= base

print("O resultado é: {}".format(resultado))