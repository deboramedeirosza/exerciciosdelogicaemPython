'''Faça um programa que carregue um vetor de dez números inteiros.
Calcule e mostre os números superiores a 50 e suas respectivas posições.
Mostrar mensagem se não existir nenhum número nesta condição.
'''

#variáveis
vetor = []
maior50 = False

#entrada
for n in range(0, 10):
    num = int(input("Informe um número {0}/10: ".format(n+1)))
    vetor.append(num)
for n in vetor:
    if n > 50:
        print("O número {0} está na posição {1} do vetor.".format(n, vetor.index(n))) # a função '.index' mostra a posição no vetor.
        maior50 = True
if maior50 == False:
        print("Não há número superior a 50.")
