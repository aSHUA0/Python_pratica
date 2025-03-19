import copy

produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
 ]

novos_produtos = [
    {**produto,'nome': produto['nome'], 'preco': round(produto['preco'] * 1.10, 2)}
    for produto in copy.deepcopy(produtos)
]

print(produtos)
print(novos_produtos)

produtos_decrescentes = sorted(copy.deepcopy(novos_produtos), key=lambda obj: obj['nome'], reverse=True)

produtos_crescentes = sorted(copy.deepcopy(novos_produtos), key=lambda obj: obj['nome'])

produtos_ordenados_por_preco = sorted(copy.deepcopy(novos_produtos), key=lambda obj: obj['preco'])

print(produtos_crescentes)
print(produtos_decrescentes)
print(produtos_ordenados_por_preco)
