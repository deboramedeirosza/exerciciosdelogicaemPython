'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

 Tabuada de 5:
 5 X 1 = 5
 5 X 2 = 10
  ...
 5 X 10 = 50
 '''
#entrada
numero = int(input("Informe um número: "))
#processamento
while numero > 10 or numero < 1:
    print("O número deve ser entre 1 e 10.")
    numero = int(input("Informe um número: "))
    print("Tabuada de {0}".format(numero))
    for i in range(1, 11):
        resultado = numero * i
        print("{0} X {1} = {2}".format(numero, i, resultado))
