nCamisetas = int(input())
if nCamisetas <= 30:
    unitario = 25.5
else:
    unitario = 20.5

print("Cada aluno pagará {:.2f} por cada camiseta".format(unitario))