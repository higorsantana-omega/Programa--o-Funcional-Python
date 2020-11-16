# Lambda é uma função anônima
# Exemplos

# Pura
mult = lambda x: x * 2
print(mult(10))

# Com map
compras = (
    {'Qtd': 2, 'Preço': 1.99},
    {'Qtd': 5, 'Preço': 3.99}
)

total = tuple(map(lambda compra: compra['Qtd'] * compra['Preço'], compras))

print('Preço totais', list(total))
print('Total: ', sum(total))