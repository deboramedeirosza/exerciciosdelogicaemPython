''' Elabore um algoritmo que leia as variáveis 'c' e 'n', respectivamente código e número de horas trabalhadas de um operário. Calcule o salário sabendo-se que ele ganha R$ 10,00/hora.
Quando o número de horas exceder a 50 calcule o excesso de pagamento armazenando-o na variável 'e'. Caso contrário zerar tal variável. A hora excedente de trabalho vale R$ 20,00/hora.
No final do processamento imprirmir salário total e salário excedente.
'''
#entradas
c = int(input("Informe o código do operário: "))
n = float(input("Informe quantas horas foram trabalhadas: "))
e = 0

#processamento
if n > 50:
    e = n -50
    n = n -e
salario_excedente = e * 20
salario_normal = n * 10
salario_total = salario_excedente + salario_normal

#saída
print("O salário total é de R$ {0:.2f}".format(salario_total))
print("O salário excedente é de R$ {0:.2f}".format(salario_excedente))
