#Faça um algoritmo que receba um valor e escreva a informação 'Número é par' ou 'Número é ímpar' ou 'Número é neutro'
n = int(input('Digite um número: '))
if n==0:
    print('Número é neutro')
elif n%2==0:
    print('Número é par')
else:
    print('Número é ímpar')