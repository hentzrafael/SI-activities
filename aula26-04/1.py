# Solicite o nome e o salário de 10 pessoas, ao final mostre a soma de todos os salários digitados
soma = 0
for pessoa in range(10):
    salario = float(input("Digite o seu salário: "))
    soma += salario

print("A soma dos salários é: {}".format(soma))