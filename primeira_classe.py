# associar uma função a uma determinada variavel

def dobro(x):
    return x * 2

def quadrado(x):
    return x ** 2

if __name__ == "__main__": 
    funcs = [dobro, quadrado] * 2
    # zip é responsavel por juntas duas variaveis a uma função
    for func, numero, in zip(funcs, range(1, 11)):
        print(f'O {func.__name__} de {numero} é {func(numero)}')