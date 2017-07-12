## http://wiki.python.org.br/ListaDeExercicios
## Caique Borges
## Exercicios de estrutura de decisao
## https://wiki.python.org.br/EstruturaDeRepeticao

## EXERCICIO 06

num1 = float(input('Insira o primero número: '))
num2 = float(input('Insira o segundo número: '))
num3 = float(input('Insira o terceiro número: '))

if(num1 > num2 and num1 > num3):
	print('O primeiro número é o maior')
elif(num2 > num1 and num2 > num3):
	print('O segundo número é o maior')
else:
	print('O terceiro número é o maior')