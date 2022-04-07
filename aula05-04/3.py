meses = {
    '1':'Janeiro',
    '2':'Fevereiro',
    '3':'Março',
    '4':'Abril',
    '5':'Maio',
    '6':'Junho',
    '7':'Julho',
    '8':'Agosto',
    '9':'Setembro',
    '10':'Outubro',
    '11':'Novembro',
    '12':'Dezembro'
}
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))

print("Chapecó, {} / {} / {}".format(dia, meses[str(mes)],ano))