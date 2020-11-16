# receber outra função como parametro

def dobro(x):
    return x * 2

def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))

if __name__ == "__main__":
    processar('dobro de 1 a 10', range(1, 11), dobro)
