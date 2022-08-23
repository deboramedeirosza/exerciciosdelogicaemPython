'''Construa um algoritmo que leia 10 valores inteiros e positivos e:
 * a) Encontre o maior valor;
 * b) Encontre o menor valor;
 * c) Calcule a média dos números lidos.
 '''
#variáveis
maior = 0
menor = -1
soma = 0
#entrada/processamento
for i in range(1, 11):
    valor = int(input(f"Informe um valor {i}/10: "))
    while valor < 0:
        valor = int(input(f"Valor inválido. Informe um valor inteiro e positivo {i}/10: "))
    if valor > maior:
        maior = valor
    if menor == -1 or valor < menor:
        menor = valor
    soma = soma + valor
media = soma / 10
print("O maior valor é {0}".format(maior))
print("O menor valor é {0}".format(menor))
print("A média dos múmeros é {0}".format(media))
