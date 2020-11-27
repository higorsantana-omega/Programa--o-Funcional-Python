# Ele retornar se é verdadeiro ou falso

pessoas = [
    {'nome': 'Pedro', 'Idade': 34},
    {'nome': 'Higor', 'Idade': 14},
    {'nome': 'Joao', 'Idade': 29},
    {'nome': 'Antonio', 'Idade': 43}
]

menores = filter(lambda p: p['Idade'] < 18, pessoas)
print(list(menores))

tamanho_nome = filter(lambda t: len(t['nome']) > 5, pessoas)
print(list(tamanho_nome)) 