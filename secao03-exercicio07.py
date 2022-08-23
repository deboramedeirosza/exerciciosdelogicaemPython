# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule o peso ideal, usando a seguinte fórmula: (72.7 * altura) - 58.

#variável/entrada
altura = float(input("Informe a altura: "))

#processamento
peso_ideal = (72.7 * altura) - 58

#saída
print("O peso ideal é de {0:.2f}".format(peso_ideal))
