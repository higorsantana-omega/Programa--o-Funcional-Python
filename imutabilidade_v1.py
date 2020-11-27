# from locale import setlocale, LC_ALL
from calendar import month_name, mdays
from functools import reduce

# setlocale(LC_ALL, 'pt_BR')

Lista_meses = filter(lambda x: mdays[x] == 31, range(1, 13))
nome_meses = map(lambda x: month_name[x], Lista_meses)
juntar = reduce(lambda todos, nome_mes: f'{todos}\n {nome_mes}',
                nome_meses, 'Meses com 31 dias')
print(juntar)