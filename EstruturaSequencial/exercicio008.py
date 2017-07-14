## http://wiki.python.org.br/ListaDeExercicios
## Caique Borges
## Exercicios de estrutura sequencial
## http://wiki.python.org.br/EstruturaSequencial

## EXERCICIO 8 - Faça um Programa que pergunte quanto você ganha por hora e o número
# de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganhoHora = float(input('Quanto voce ganha por hora? R$'))
horasTrabalhadas = float(input('Quantas horas trabalhou no mês? '))

print('O seu salario este mes eh de R$', round(ganhoHora * horasTrabalhadas, 2))