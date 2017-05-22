## http://wiki.python.org.br/ListaDeExercicios
## Caique Borges
## Exercicios de estrutura sequencial
## http://wiki.python.org.br/EstruturaSequencial

## EXERCICIO 10 - Faça um Programa que peça a temperatura em graus Celsius,
#  transforme e mostre em graus Farenheit.

c = float(input('Insira os graus em celsius: '))
f = c * 1.8 + 32

print(c, '°C -> ', f, '°F', sep="")