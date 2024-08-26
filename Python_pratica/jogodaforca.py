import os

palavra_secreta = 'auanny'
repeticoes = 0
resposta = ''
letras_acertadas = ''


while True:
    resposta = input('Digite uma letra: ')

    if resposta == palavra_secreta:
        os.system('cls')
        print('PARABENS CRLH')
        break
    else:
        print('Errou a palavra')
    if len(resposta) > 1 :
        print('Digite somente uma letra para facilitar')
        continue
    
    if resposta in palavra_secreta:
        letras_acertadas += resposta
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '_'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('PARABENS CRLH')
        print('A palavra era:', palavra_secreta)
        break
    repeticoes += 1 
print(f'Você teve {repeticoes} tentativas até acertar' )