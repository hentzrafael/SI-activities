nome = input("Digite o seu nome: ")
horasEstudoSemana = int(input("Quantas horas você estuda algoritmos por semana? "))
notaEsperada = float(input("Digite a nota que você espera tirar na prova de Algoritmos e Lógica de Programação: "))

if horasEstudoSemana < 2 and notaEsperada >= 7.0:
    print("O resultado é que você precisa estudar mais.")
elif horasEstudoSemana >= 3:
    if notaEsperada > 7.0:
        print("O resultado será você esta tranquilo.")
    else:
        print("O resultado será você deve prestar mais atenção.")
