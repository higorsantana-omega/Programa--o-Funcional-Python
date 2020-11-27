from functools import reduce

# Reduce retorna uma lista ou um dicionario com base no seu acumulador

pessoas = [
    {'nome': 'Pedro', 'Idade': 34},
    {'nome': 'Higor', 'Idade': 14},
    {'nome': 'Joao', 'Idade': 29},
    {'nome': 'Antonio', 'Idade': 43}
]

# epx = reduce(lambda acumulador, p: acumulador + p[], lista, inicio_acumulador)
soma = reduce(lambda idades, p: idades + p['Idade'], pessoas, 0)
print(soma)