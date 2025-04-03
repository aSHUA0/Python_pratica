import os

def palavra_min(palavra):
  retorno = ''
  for caracter in palavra:
    if caracter.isupper():
      retorno += caracter.lower()
    else:
      retorno += caracter
  return retorno

comandos = ['listar', 'desfazer', 'refazer', 'sair', 'limpar']
lista = []
desfazer = []
refazer = []

while True:
    print('Lista de Tarefas')
    print('Comandos: listar | desfazer | refazer | sair | limpar')
    tarefa = input('Digite uma tarefa ou comando: ')
    tarefa = palavra_min(tarefa)

    if tarefa in comandos:
        if tarefa == 'listar':
            if len(lista) < 1:
                print()
                print('Nada a listar')
                print()
            else:
                print()
                for i in lista:
                    print(i)
                print()
        
        elif tarefa == 'desfazer':
            if len(lista) < 1:
                print()
                print('Nada a desfazer')
                print()
            else:
                desfazer.append(lista[-1])
                lista.pop()
                print()
                for i in lista:
                    print(i)
                print()
        
        elif tarefa == 'refazer':
            if len(desfazer) < 1:
                print()
                print('Nada para refazer')
                print()
            else:   
                refazer.append(desfazer[-1])
                desfazer.pop()
                lista.append(refazer[-1])
                print()
                for i in lista:
                    print(i)
                print()

        elif tarefa == 'limpar':
           os.system('cls')

        else:
            os.system('cls')
            print('Fechando o programa')
            break              
    else:
        tarefa = tarefa.strip
        if not tarefa:
            print('Você digitou nada')
            print()
        else:
            lista.append(tarefa)
