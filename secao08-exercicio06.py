'''Faça um programa que receba um código numérico inteiro e um vetor de cinco posições de números reais.
Se o código for zero, termine o programa. Se o código for 1, mostre o vetor na ordem direta.
Se o código for 2 , mostre o vetor na ordem inversa.
'''

#variáveis
vetor = []

#entrada
codigo = int(input("Informe um código: "))

#processamento
if codigo != 0 and codigo <= 2:
    
    for n in range(0, 5):
        num = float(input("Informe um número real: "))
        vetor.append(num)
    if codigo == 1:
        for n in vetor:
            print(n)
    if codigo == 2:
        vetor.reverse()
        for n in vetor:
            print(n)
