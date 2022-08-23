'''João da Silva, pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido
pelo regulamento de pesca do estado de São Paulo (50kg) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um algoritmo que leia a variável 'p' (peso de peixes) e verifique se há excesso. Se houver, gravar na variável 'e' (excesso) e na variável
'm' o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo 'zero'.
'''

#variáveis
e = 0
m = 0

#entrada
p = float(input("Informe o peso: "))
#processamento
if p > 50:
    e = p - 50
    m = e * 4
print("Peso: {0} kg ".format(p))
print("Excesso: {0} kg".format(e))
print("Multa: R$ {0:.2f}".format(m))
    
