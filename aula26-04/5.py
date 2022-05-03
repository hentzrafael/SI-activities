n = int(input("Digite o número a ser buscado: "))
encontrado = False
for i in range(10):
    n2 = int(input("Digite um número: "))
    if n2 == n:
        encontrado = True

if encontrado:
    print("NUMERO ENCONTRADO")
else:
    print("NUMERO NÃO ENCONTRADO")