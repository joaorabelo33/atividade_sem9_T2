

def contador_s(resposta):
    contador = 0
    resposta = str(resposta).lower()
    if(resposta == 's'):
        contador+=1
    return contador

def crime(contador):
    status = ''
    if(contador < 2):
        status = 'Inocente'
    elif(contador == 2):
        status = 'Suspeito'
    elif(contador == 3 or contador == 4):
        status = 'Cúmplice'
    elif(contador == 5):
        status = 'Assassino'
    else:
        raise ValueError('Entrada inválida')   

    return status    



contador = 0
resposta = input().strip()
contador += contador_s(resposta)
resposta = input().strip()
contador += contador_s(resposta)
resposta = input().strip()
contador += contador_s(resposta)
resposta = input().strip()
contador += contador_s(resposta)
resposta = input().strip()
contador += contador_s(resposta)
resultado = crime(contador)
print(f'{resultado}')
    
