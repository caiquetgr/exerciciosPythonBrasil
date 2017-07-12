## http://wiki.python.org.br/ListaDeExercicios
## Caique Borges
## Exercicios de estrutura de decisao
## https://wiki.python.org.br/EstruturaDeRepeticao

## EXERCICIO 01

num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))

if(num1 > num2):
	print("O maior número é o primeiro! {} > {} ".format(num1, num2))
else:
	print("O maior número é o segundo! {} > {}".format(num2, num1))