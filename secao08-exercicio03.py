'''Faça um programa que carregue um vetor com 10 números inteiros. Mostre o vetor na ordem inversa a que foi digitado.'''

#variáveis
vetor = []

#entradas
for n in range(0, 10):
    num = int(input("Informe um valor para o vetor: "))
    vetor.append(num)
#processamento
vetor.reverse() # .reverse() é utilizada para invertar a sequência do vetor.
for n in vetor:
    print(n)
