## http://wiki.python.org.br/ListaDeExercicios
## Caique Borges
## Exercicios de estrutura de decisao
## https://wiki.python.org.br/EstruturaDeRepeticao

## EXERCICIO 04

letra = input('Digite uma letra: ').lower()

vogais = ['a','e','i','o','u']

if( letra in vogais ):
	print('Letra {} é uma vogal!'.format(letra))
else:
	print('Letra {} é uma consoante!'.format(letra))