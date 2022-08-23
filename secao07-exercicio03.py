'''Elabore um programa que gera e escreve os números ímpares dos números entre 100 e 200.'''

#processamento
for i in range(100, 201):
    if i % 2 == 1: #pode-se usar tb 'i % 2 != 0' que tb identifica se é ímpar.
        print(i)
