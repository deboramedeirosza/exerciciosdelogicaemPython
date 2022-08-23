'''Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem: "Múltiplo de 10".'''

#processamento
for n in range(1, 101):#no python se coloca 1 número a mais de onde se quer ir. i = n -1.
    print(n)
    if n % 10 == 0:
        print("Múltiplo de 10")
