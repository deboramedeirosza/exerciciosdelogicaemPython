''' Elebore um algoritmo que leia um número. Se positivo armazene-o em 'a', se for negativo, em 'b'.
No final mostrar resultado.
'''
#entrada
numero = int(input("Informe um número: "))

#processamento
if numero > 0:
    a = numero
    print("{0} é um valor positivo".format(a))
else:
    b = numero
    print("{0} é um valor negativo".format(b))
