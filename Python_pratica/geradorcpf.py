import random

cpf =''
for i  in range(9):
    cpf += str(random.randint(0,9))

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

primeiro_digito_str = str(primeiro_digito)
cpf = cpf + primeiro_digito_str
#calculo segundo digito
i=0
resultado = 0

while i < 10:
    algarismo = cpf[i]
    algarismo = int(algarismo)

    resultado += algarismo * (11 - i)
    i+=1
    
segundo_digito = resultado * 10
segundo_digito = segundo_digito % 11
if segundo_digito > 9:
   segundo_digito = 0

segundo_digito_str = str(segundo_digito)
cpf = cpf + segundo_digito_str
print(cpf)