## http://wiki.python.org.br/ListaDeExercicios
## Caique Borges
## Exercicios de estrutura sequencial
## http://wiki.python.org.br/EstruturaSequencial

## EXERCICIO 9 - Faça um Programa que peça a temperatura em graus Farenheit,
#  transforme e mostre a temperatura em graus Celsius.
#C = (5 * (F-32) / 9).

f = float(input('Qual a temperatura em Farenheit? '))
c = (5 * (f-32) / 9)

print(f, '°K -> ', c, '°C', sep="")