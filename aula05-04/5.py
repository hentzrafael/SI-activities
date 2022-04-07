entrada = input().split(' ')
if entrada[0] == '1':
    preco = 4
elif entrada[0] == '2':
    preco = 4.5
elif entrada[0] =='3':
    preco = 5
elif entrada[0] == '4':
    preco = 2
elif entrada[0] == '5':
    preco = 1.5

print("Total: R$ {:.2f}".format(int(entrada[1])*preco))