print("Digite os dados da Chapecoense!")

vitorias = int(input("Quantas vitórias? "))
empates = int(input("Quantos empates? "))
derrotas = int(input("Quantas derrotas? "))
totalPontos = vitorias*3 + empates
deixadosDeGanhar = empates*2 + derrotas*3
aproveitamento = totalPontos/((vitorias+empates+derrotas)*3)
print("Pontos totais: {}".format(totalPontos))
print("Pontos de vitórias: {}".format(vitorias*3))
print("Pontos de empates: {}".format(empates))
print("Pontos que deixou de ganhar: {}".format(deixadosDeGanhar))
print("Aproveitamento: {:.2f}%".format(aproveitamento*100))

if aproveitamento > 0.8:
    print("Se mantivermos este percentual temos chance de subir para a A.")
elif aproveitamento >= 0.5 and aproveitamento <= 0.8:
    print("Se mantivermos este percentual temos chance de permanecer na B.")
elif aproveitamento < 0.5:
    print("Se mantivermos este percentual vamos cair para C.")