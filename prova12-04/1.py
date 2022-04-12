
nome = input("Digite o seu nome: ")
print("Coloque S ou s para os sintomas que possui, caso contrário dê enter:")
diarreia = input("Diarreia: ")
coriza = input("Coriza: ")
dorDeGarganta = input("Dor de garganta: ")
dorNoCorpo = input("Dor no corpo: ")
tosse = input("Tosse: ")
febre = input("Febre: ")
perdaPaladarOlfato = input("Perda de paladar e olfato: ")
dificuldadeRespirar = input("Dificuldade para respirar: ")

pontos = 0
if diarreia == "S" or diarreia == "s":
    pontos += 0.5
if coriza == "S" or coriza == "s":
    pontos += 0.5
if dorDeGarganta == "S" or dorDeGarganta == "s":
    pontos += 1
if dorNoCorpo == "S" or dorNoCorpo == "s":
    pontos += 1
if tosse == "S" or tosse == "s":
    pontos += 1
if febre == "S" or febre == "s":
    pontos += 2
if perdaPaladarOlfato == "S" or perdaPaladarOlfato == "s":
    pontos += 4
if dificuldadeRespirar == "S" or dificuldadeRespirar == "s":
    pontos += 3

if pontos > 7:
    print("{}, POR FAVOR, PROCURE O QUANTO ANTES UM ATENDIMENTO MÉDICO.".format(nome.upper()))
elif pontos <= 7:
    print("{}, ATENDIMENTO PERMITIDO, SEMPRE FIQUE ATENTO AOS POSSIVEIS SINTOMAS.".format(nome.upper()))

print(pontos)