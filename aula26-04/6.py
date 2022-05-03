N = int(input())
for numero in range(N):
    entrada = int(input())
    i = 1
    divisores = 0
    while i <= entrada:
        if entrada % i == 0:
            divisores += 1
        i +=1
    if divisores > 2:
        print("{} nao eh primo".format(entrada))
    elif divisores == 2:
        print("{} eh primo".format(entrada))
