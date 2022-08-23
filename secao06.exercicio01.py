# Ler uma variável numérica n e imprimi-la somente se a mesma for maior que 100, caso contrário imprimi-la com o valor zero.

#entrada
n = int(input("Informe um número: "))
#processamento
if n > 100:
    print(n)
else:
    n = 0
    print(n)
    
''' A organização dos blocos no Python não é feita por meio de chaves {}, mas sim pela identação do código, ou seja, pelos espaços tipo parágrafo que é dado.
Por padrão se organiza os blocos com 4 espaços, nunca o TAB pq o programa pode apresentar erros.
'''
