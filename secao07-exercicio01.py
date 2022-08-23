'''
Faça um algoritmo que determine o maior entre N números. A condição de parada é a entrada de um valor 0, ou seja, o algoritmo
deve ficar calculando o maior até que a entreda seja igual a 0 (zero).
'''
#variáveis
maior = 0
#entrada
numero = int(input("Informe um número: "))

#processamento
while numero != 0:
    if numero > maior:
        maior = numero
    numero = int(input("Informe um número: "))
print("O maior número é {0}".format(maior))
