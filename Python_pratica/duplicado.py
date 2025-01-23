lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

aux = 0
numero = 0
duplicada = 0
numero_duplicado = []


for row in lista_de_listas_de_inteiros:
    indice_duplicada = []

    for element in row:
        numero = element
        indice = row.index(element) + 1

        while indice < len(row):
            duplicada = row[indice]
            indice += 1
            if duplicada == numero:
                indice_duplicada.append(indice - 1)
        
    if indice_duplicada != []:
        numero_duplicado.append(row[min(indice_duplicada)])
            
    else:
        numero_duplicado.append('Nenhum')
        continue


num = 1
for element in numero_duplicado:
    linha = f'O {num}º conjunto tem {element} duplicado mais próximo'
    print (linha)
    num += 1
