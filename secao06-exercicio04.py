'''Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule o peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7 * altura) - 58
Para mulheres: (62.1 * altura) - 44.7
'''

#entradas
altura = float(input("Informe a altura: "))
sexo = input("Informe o sexo [F/M]: ")

#processamento
if sexo.lower() == 'm': #função do .lower é converter para minúsculo. Não precisa importar nada pq esta função está incluída no tipo de dado que ta recebendo, que no caso é o string. 
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print("Sexo não reconhecido.")
print("O peso ideal é {0:.2f}".format(peso_ideal))
