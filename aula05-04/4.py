nome = input('Digite o seu nome: ')
ddd = int(input('Digite o DDD do telefone: '))
numero = int(input('Digite o número de celular sem espaços: '))

print('Olá, {}'.format(nome))
if ddd == 49:
    print('{} VOCÊ LIGOU PARA UM TELEFONE PARA O VELHO OESTE'.format(nome))
elif ddd == 48:
    print('{} VOCÊ LIGOU PARA UM TELEFONE PARA O LITORAL'.format(nome))
elif ddd == 47:
    print('{} VOCÊ LIGOU PARA UM TELEFONE PARA A REGIÃO DE JOINVILLE'.format(nome))
else:
    print('{} VOCÊ LIGOU PARA UM TELEFONE PARA FORA DE SC'.format(nome))





