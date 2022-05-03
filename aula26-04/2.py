nAlunos = int(input("Quantos alunos tem na turma de algoritmos: "))

soma = 0
for aluno in range(nAlunos):
    nota = float(input("Digite a nota: "))
    soma += nota

print("Média da turma: {}".format(soma/nAlunos))
