# Programação Funcional Python

Programação funcional é um paradigma de programação (maneira como se programa)
Se pensa no código como uma sequência de funções, e esses funções são compostas para resolver um problema.


## Funções Pura
Função é um processo que recebe alguma entrada, e produz alguma saída.
Função pura, recebe alguma entrada e retorna alguma saída com base nessa entrada. Por conta de sua independencia elas se tornam grandes candidatos para o processamento paralelo a CPU.
Elas são extremamente independentes, são faceis de mover, refatorar e reorganizar em seu código.

## Função de primeira classe
É quando se associa uma função a uma variável. São passadas como parâmetro e recebida como resultado.
```
funcs = [dobro, quadrado] * 5
for func, numero in zip(funcs, range(1, 11)):
  print(f'O {func.__name__} de {numero} é {func(numero)}')
```
