'''A Secretaria de Meio Ambiente que controla o índice de poluição mantém 3 grupos de insdústrias que são altamente poluentes ao meio ambiente. O índice de poluição aceitável 
varia de 0,05 até 0,25. Se o índice sobre para 0,3 as indústrias do 1º grupo são intimadas para suspenderem as atividades, se o índice crescer para 0,4 as indústrias do 1º e 2º grupo 
são intimadas para suspenderem as atividades, se o índice atingir 0,5 todos os grupos devem ser notificados a paralisarem suas atividades. Faça um algoritmo que leia
 o índice de poluição medido e emita a notificação adequada aos diferentes grupos de empresas.
 '''
 
#entradas
indice = float(input("Informe o índice de poluição: "))

#processamento
if indice >= 0.3 and indice < 0.4:
    print("Indústriais do Grupo 1 devem suspender as atividades")
elif indice >= 0.4 and indice < 0.5:
    print("Indústrias dos Grupos 1 e 2 devem suspender as atividades")
elif indice >= 0.5:
    print("Todos os Grupos de Indústrias devem suspender as atividades")
else:
    print("Liberada as atividades industriais para todos os grupos")
