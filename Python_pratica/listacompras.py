import os

lista_de_compras = []
lista_quantidade = []
letras_permitidas = 'ials'

while True:
    opcao = input('Selecione uma opção:\n [i]nserir [a]pagar [l]istar [s]air: ')
    if len(opcao) > 1:
        print('Opção invalida, tente novamente')
        continue
    if opcao not in letras_permitidas:
        print('Opção invalida, tente novamente')
        continue
     
     #parte das opções
    
    if opcao == 'i':
        item = input('Digite o nome do item: ')
        quantidade = input('Digite a quantidade: ')
        lista_de_compras.append(item)
        lista_quantidade.append(quantidade)
        os.system('cls')
    
    elif opcao == 'a':
        try:
            produto_lista = lista_de_compras[0]
            validacao = True
        except:
            validacao = None
        if validacao is None:
            print('Sua lista está vazia')
            continue
        
        os.system('cls')

        for indice, nome in enumerate(lista_de_compras):
            print(f'Indice:{indice} Produto: {nome}')

        codigo = input('Digite o indice do produto: ')
        try:
            codigo_int = int(codigo)
            del lista_de_compras[codigo_int]
            del lista_quantidade[codigo_int]
        except ValueError:
            print('Por favor digite número int.')
            continue
        except IndexError:
            print('Índice não existe na lista')
            continue
        except Exception:
            print('Erro desconhecido')
            continue
        
        print('Produto apagado com sucesso')
    
    elif opcao == 'l':
        try:
            produto_lista = lista_de_compras[0]
            validacao = True
        except:
            validacao = None
        if validacao is None:
            print('Sua lista está vazia')
            continue
        
        os.system('cls')

        for indice, nome in enumerate(lista_de_compras):
                print(f'Indice:{indice} Produto: {nome}')
    
    elif opcao == 's':
        os.system('cls')
        break

print('A sua lista de compras ficou assim: ')
for indice, produto in enumerate(lista_de_compras):
    print(produto, lista_quantidade[indice])