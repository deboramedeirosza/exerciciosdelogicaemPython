''' Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar, e se é positivo ou negativo.'''

#entrada
num = int(input("Informe um número: "))

#processamento
if num %2 == 0:
    if num > 0:
        print("O número {0} é par e positivo".format(num))
    else:
        print("O número {0} é par e negativo".format(num))
else:
    if num > 0:
        print("O número {0} é ímpar e positivo".format(num))
    else:
        print("O número {0} é ímpar e negativo".format(num))
