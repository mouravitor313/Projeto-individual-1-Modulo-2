###########################
#  Trabalho individual 1  #
#         Modulo2         #
###########################

dicionario = {}

def add_input (dicionario):
    menu = 1
    while (menu != 0):
        cont = 0
        menu = int(input('Quantas pessoas adicionar ao sistema? (Digite 0 para encerrar o programa) '))
        while (cont != menu):
            cont = cont + 1
            name = input('Digite um nome para adicionar ao sistema: ')
            e = input('Digite a nota da entrevista dessa pessoa: ')
            t = input('Digite a nota teste teórico dessa pessoa: ')
            p = input('Digite a nota teste prático dessa pessoa: ')
            s = input('Digite a nota de soft skills dessa pessoa: ')
            if dicionario.get(name):
                print(f'{name} já está no sistema! ')
            else:
                dicionario[name] = (f'e_{e}'), (f't_{t}'), (f'p_{p}'), (f's_{s}')
            print(dicionario)
            if cont == menu:
                break
        if menu <= 0:
            break
    return dicionario

lista = [dicionario]

def achar (dicionario):
    sair = "S"
    while sair != "N":
        key = str.title(input('Pesquisar (digite um nome): '))
        if key in dicionario:
            print(f'O {key} conseguiu as notas: {dicionario[key]}')
        else:
            print("Não temos essa pessoa em nossa base de dados")    
        sair = str.upper(input("Deseja buscar por mais alguém? [S/N] "))

while(True):
    choice = input('Deseja adicionar uma pessoa ao sistema ou pesquisar por alguém? (1 para adicionar, 2 para pesquisar e 3 para sair) ')
    if choice == '1':
        add_input(dicionario)
    elif choice == '2':
        achar(dicionario)
    elif choice == '3':
        break
    else:
        print('Opção inválida!')