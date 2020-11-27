from functools import reduce
from operator import add

valores = [30, 15, 6, 100, 25]

print(sorted(valores))
print(valores)

print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(list(reversed(valores)))
print(valores)
