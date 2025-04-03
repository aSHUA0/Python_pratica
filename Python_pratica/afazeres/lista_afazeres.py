from lista_afazeres_m import *

def palavra_min(palavra):
  retorno = ''
  for caracter in palavra:
    if caracter.isupper():
      retorno += caracter.lower()
    else:
      retorno += caracter
  return retorno


lista = []
lista_desfazer = []
lista_refazer = []


while True:

    print('Lista de Tarefas')
    print('Comandos: listar | desfazer | refazer | sair | limpar')
    tarefa = input('Digite uma tarefa ou comando: ')
    tarefa = palavra_min(tarefa)

    comandos = {
        'listar': lambda: listar(lista),
        'desfazer': lambda: desfazer(lista, lista_desfazer),
        'refazer': lambda: refazer(lista, lista_refazer, lista_desfazer),
        'sair': lambda: sair(),
        'limpar': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, lista)
        }
    
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()