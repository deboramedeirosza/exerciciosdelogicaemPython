'''Faça um algoritmo que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

#variáveis/entradas
valor_hora = float(input("Informe o valor da hora de trabalho: "))
qtd_horas = int(input("Informe quantas horas foram trabalhadas: "))

#processamento
salario = (valor_hora * qtd_horas)

#saída
print("O salário total é de R$ {0:.2f}".format(salario))
