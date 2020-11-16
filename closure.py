# Função dentro de outra função

def mult(x):
    def calcular(y):
        return x * y
    return calcular

multa = mult(2)
print(f'O dobro de 2 é {multa(2)}')