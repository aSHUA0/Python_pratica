cpf = input('Digite o seu CPF sem a pontuação: ')

while True:
    #Calculo primeiro digito
    i=0
    resultado = 0
    
    while i < 9:
        algarismo = cpf[i]
        algarismo = int(algarismo)
    
        resultado += algarismo * (10 - i)
        i += 1
    
    primeiro_digito = resultado * 10
    primeiro_digito = primeiro_digito % 11

    if primeiro_digito > 9:
        primeiro_digito = 0

    #verificação primeiro digito
    primeiro_digito_str = str(primeiro_digito)

    if primeiro_digito_str != cpf[i]:
        print('CPF invalido')
        break

    #calculo segundo digito
    i=0
    resultado = 0

    while i < 10:
        algarismo = cpf[i]
        algarismo = int(algarismo)
    
        resultado += algarismo * (11 - i)
        i += 1
    
    segundo_digito = resultado * 10
    segundo_digito = segundo_digito % 11
    if segundo_digito > 9:
        segundo_digito = 0
    
    #verificação segundo digito
    segundo_digito_str = str(segundo_digito)

    if segundo_digito_str != cpf[i]:
        print('CPF invalido')
        break
    else:
        print('CPF válido')
        break