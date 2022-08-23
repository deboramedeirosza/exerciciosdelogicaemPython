'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando mensagem de erro e voltando a pedir as informações.'''

nome = input("Informe o nome: ")
senha = input("Informe a senha: ")

while nome == senha:
    print("Nome e senha tem que ser diferente.")
    nome = input("Informe o nome: ")
    senha = input("Informe a senha: ")
