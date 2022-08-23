''' Ler um número e verificar se ele é par ou ímpar. Quando for par armazenar esse valor em 'p' e quando for ímpar armazená-lo em 'i'.
Exibir 'p' e 'i' no final do processamento.
'''
#variáveis
p = 0
i = 0
#entrada
numero = int(input("Informe um número: "))

#processamento
if(numero % 2 == 0):
    p = numero
    print("{0} é um número par.".format(numero))
else:
    i = numero
    print("{0} é um número ímpar.".format(numero))
