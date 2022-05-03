string = """
O que você mais gosta de fazer nos finais de semana:
1) Dormir
2) Estudar algoritmos
3) Passear
4) Outros
0) Sair
"""
entradas = {"1":0,"2":0,"3":0,"4":0}
total = 0
escolha = '1'
while escolha != '0':
    print(string)
    escolha = input()
    if escolha in entradas.keys():
        entradas[escolha] += 1
        total += 1
if total >0:
    print("Total de votos: {}".format(total))

    print("Total Dormir: {}".format(entradas["1"]))
    print("% Dormir: {:.2f}%".format((entradas["1"]/total)*100))

    print("Total Estudar algoritmos: {}".format(entradas["2"]))
    print("%% Estudar algoritmos: {:.2f}%".format((entradas["2"]/total)*100))

    print("Total Passear: {}".format(entradas["3"]))
    print("% Passear: {:.2f}%".format((entradas["3"]/total)*100))

    print("Total Outros: {}".format(entradas["4"]))
    print("% Outros: {:.2f}%".format((entradas["4"]/total)*100))
    maior = 0
    chaveMaior = ""
    for chave,voto in entradas.items():
        if voto > maior:
            maior = voto
            chaveMaior = chave
    print("A escolha com mais votos foi a: {}".format(chaveMaior))