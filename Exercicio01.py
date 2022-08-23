'''Faça um algoritmo que carregue um vetor de 5 elementos inteiros e em seguida armazene em um vetor apenas os números pares maiores que 0.
No final deve mostrar os elementos do vetor na tela.
'''
#variáveis
vetor = [] # Esse tipo de dado no Python é chamado de 'lista'
pares = [] # aqui há duas listas vazias

for n in range(1, 6):
    vetor.append(n) # O .append adiciona o número recebido no vetor.
    if n % 2 == 0:
        pares.append(n)
for p in pares:
    print(p)
    
