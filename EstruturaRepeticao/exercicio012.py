## http://wiki.python.org.br/ListaDeExercicios
## Caique Borges
## Exercicios de estrutura de repetição
## https://wiki.python.org.br/EstruturaDeRepeticao

## EXERCICIO 12

num = int(input('Digite o número que quer ver a tabuada: '))

for i in range(1, 10+1, 1):
	print("{} x {} = {}".format(num, i, i * num))