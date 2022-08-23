'''
Elabora um algoritmo que dada a idade de um nadador classifique-o em uma das seguintes categorias:
 * infantil-a = 5 a 7 anos;
 * infantil-b = 8 a 11 anos;
 * juvenil-a = 12 a 13 anos;
 * juvenil-b = 14 a 17 anos;
 * adultos = maiores de 18 anos;
 '''
 
#entrada
idade = int(input("Informe a idade: "))

#processamento
if idade < 5:
    print("Não possui idade mínima para nadador")
elif idade >= 5 and idade <= 7:
    print("Aluno(a) com {0} anos de idade. Classificado para turma Infantil A.".format(idade))
elif idade >= 8 and idade <= 11:
    print("Aluno(a) com {0} anos de idade. Classificado para turma Infantil B.".format(idade))
elif idade >= 12 and idade <= 13:
    print("Aluno(a) com {0} anos de idade. Classificado para turma Juvenil A.".format(idade))
elif idade >= 14 and idade <= 17:
    print("Aluno(a) com {0} anos de idade. Classificado para turma Juvenil B.".format(idade))
elif idade >= 18:
    print("Aluno(a) com {0} anos de idade. Classificado para turma Adultos.".format(idade))
