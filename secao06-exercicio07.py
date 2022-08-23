''' Desenvolva um algoritmo que:
a) Leia 4 (quatro) números;
b) Calcule o quadrado de cada número;
c) Se o valor resultante do quadrado do terceiro número for >= 1000, imprima-o e finalize;
d) Caso contrário, imprima os valores lidos e seus respectivos quadrados.
'''

#entradas
n1 = int(input("Informe o número 1: "))
n2 = int(input("Informe o número 2: "))
n3 = int(input("Informe o número 3: "))
n4 = int(input("Informe o número 4: "))

#processamento
q1 = n1 ** 2
q2 = n2 ** 2
q3 = n3 ** 2
q4 = n4 ** 2

if q3 >= 1000:
    print(q3)
else:
    print("Número 1: {0}; Quadrado: {1}".format(n1, q1))
    print("Número 2: {0}; Quadrado: {1}".format(n2, q2))
    print("Número 3: {0}; Quadrado: {1}".format(n3, q3))
    print("Número 4: {0}; Quadrado: {1}".format(n4, q4))



