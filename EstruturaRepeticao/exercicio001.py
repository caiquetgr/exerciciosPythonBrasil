## http://wiki.python.org.br/ListaDeExercicios
## Caique Borges
## Exercicios de estrutura de repetição
## https://wiki.python.org.br/EstruturaDeRepeticao

## EXERCICIO 01

invalido = True

while(invalido):
	nota = int(input('Insira uma nota entre zero e dez: '))
	
	if (nota >= 1 and nota <= 10):
		print('Obrigado pela sua opinião')
		invalido = False