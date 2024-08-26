while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Algum dos números digitados são inválidos')
        continue

    operadores_validos = '+-/*'

    if operador not in operadores_validos:
        print('Algum dos operadores digitados são inválidos')
        continue
    elif len(operador) > 1:
        print('Digite somente um operador válido')
        continue

    #Parte dos calculos

    if operador == '*':
        resultado = num_1_float * num_2_float
        print('O resultado da multiplicação é: ',resultado)
    elif operador == '/':
        resultado = num_1_float / num_2_float
        print('O resultado da divisão é: ',resultado)
    elif operador == '-':
        resultado = num_1_float - num_2_float
        print('O resultado da subtração é: ',resultado)
    else:
        resultado = num_1_float + num_2_float
        print('O resultado da adição é: ',resultado)

    #########
    sair = input('Deseja sair?[S - sim, N - não] : ').lower().startswith('s')

    if sair is True:
        break