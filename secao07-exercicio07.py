'''Sua organização acaba de contratar um estagiário para trabalhar no suporte de informática, com a intenção de fazer levantamento nas sucatas encontradas
nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testanto e anotando o estado de cada um deles, para verificar
o que se pode aproveitar deles. Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número inde-
terminado de entradas, cada um contendo: um número de identificação do mouse e o tipo de defeito:
1 - necessita esfera;
2 - necessita limpeza;
3 - necessita troca do cabo ou conector;
4 - quebrado ou inutilizado.

Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100
    Situação                                Quantidade      Percentual
- necessita esfera;                         40              40%
- necessita limpeza;                        30              30%
- necessita troca do cabo ou conector;      15              15%
- quebrado ou inutilizado.                  15              15%
'''
#variáveis
quantidade = 0
sit1 = 0
sit2 = 0
sit3 = 0
sit4 = 0

#entrada/processamento
identificacao = int(input("Informe a identificação: "))
while identificacao != 0:
    print("(1) Necessita Esfera")
    print("(2) Necessita Limpeza")
    print("(3) Necessita Troca do Cabo ou Conector")
    print("(4) Quebrado ou Inutilizado")
    #entrada
    defeito = int(input("Informe o número do defeito: "))
    #processamento
    if defeito == 1:
        sit1 = sit1 + 1
    elif defeito == 2:
        sit2 = sit2 + 1
    elif defeito == 3:
        sit3 = sit3 + 1
    elif defeito == 4:
        sit4 = sit4 + 1
    quantidade = quantidade +1
    
    identificacao = int(input("Informe a identificação: "))

p1 = sit1 / quantidade * 100.0
p2 = sit2 / quantidade * 100.0
p3 = sit3 / quantidade * 100.0
p4 = sit4 / quantidade * 100.0
#saída
print("Quantidade de Mouses: {0}".format(quantidade))
print("             Situação                        Quantidade      Percentual")
print("1 - Necessita Esfera                            {0}             {1:.2f}%".format(sit1, p1))
print("2 - Necessita Limpeza                           {0}             {1:.2f}%".format(sit2, p2))
print("3 - Necessita Troca do Cabo ou Conector         {0}             {1:.2f}%".format(sit3, p3))
print("4 - Quebrado ou Inutilizado                     {0}             {1:.2f}%".format(sit4, p4))
