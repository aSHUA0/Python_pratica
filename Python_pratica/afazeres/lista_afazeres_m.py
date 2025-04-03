import os
import json

def escrever(lista):
    with open('C:\\Users\\aSHUA\\Desktop\\Python\\afazeres\\lista_afazer.json', 'w', encoding='utf8') as arquivo:
        json.dump(lista, 
                  arquivo, 
                  ensure_ascii=False,
                  indent=2)


def adicionar(tarefa, lista):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa')
        return
    lista.append(tarefa)
    escrever(lista)
    listar(lista)

def listar(lista):
    with open('C:\\Users\\aSHUA\\Desktop\\Python\\afazeres\\lista_afazer.json', 'r', encoding='utf8') as arquivo:
        lista = json.load(arquivo)
        
    if len(lista) < 1:
        print()
        print('Nada a listar')
        print()
        return
    else:
        print()
        for i in lista:
            print(i)
        print()

def desfazer(lista, desfazer):
    if len(lista) < 1:
        print()
        print('Nada a desfazer')
        print()
        return
    else:
        desfazer.append(lista[-1])
        lista.pop()
        escrever(lista)
        print()
        listar(lista)

def refazer(lista, refazer, desfazer):
    if len(desfazer) < 1:
        print()
        print('Nada para refazer')
        print()
        return
    else:   
        refazer.append(desfazer[-1])
        desfazer.pop()
        lista.append(refazer[-1])
        escrever(lista)
        print()
        listar(lista)

def sair():
    os.system('cls')
    print('Fechando o programa')
    return exit()