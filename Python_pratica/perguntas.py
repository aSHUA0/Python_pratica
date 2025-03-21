def verificador(num):
    if num in range(1, 4):
        return num
    else:
        print('A sua resposta tem que ser um número dentro das opções')
        exit()

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

right = 0
wrong = 0
lista = ['Pergunta','Opções','Resposta']

for i in perguntas:
    for x in lista:
        if x == 'Resposta':
            try:
                resposta = int(input('Resposta: '))
            except:
                print('A sua resposta tem que ser um número dentro das opções')
                exit()
            verificador(resposta)
            if resposta == aux:
                print('Resposta correta')
                right += 1
            else:
                print('Resposta errada')
                wrong += 1
        elif x == 'Opções':
            for idx, opcao in enumerate(i[x]):
                if opcao == i['Resposta']:
                    aux = idx +1
                opcoes = f'{idx}) {opcao}'
                print(opcoes)
        else: 
            pergunta = f'{x} : {i[x]}'
            print(pergunta)

resp_right = f'Você acertou {right} perguntas'
resp_wrong = f'Você errou {wrong} perguntas'
print(resp_right)
print(resp_wrong)
