## http://wiki.python.org.br/ListaDeExercicios
## Caique Borges
## Exercicios de estrutura sequencial
## http://wiki.python.org.br/EstruturaSequencial

## EXERCICIO 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("Qual o raio do circulo? "))
area = math.pi * (raio ** 2)

print('A area do circulo eh', round(area, 2))