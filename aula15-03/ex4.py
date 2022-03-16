#Faça um algoritmo para “Calcular o estoque médio de uma peça”, sendo que: 
#ESTOQUEMÉDIO = (QUANTIDADE MÍNIMA + QUANTIDADE MÁXIMA) /2

minimo = int(input("Digite a quantidade mínima: "))
maximo = int(input("Digite a quantidade máxima: "))

estoque_medio = (minimo + maximo) / 2
print("O estoque médio é {}".format(estoque_medio))