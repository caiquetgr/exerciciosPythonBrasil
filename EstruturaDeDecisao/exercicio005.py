## http://wiki.python.org.br/ListaDeExercicios
## Caique Borges
## Exercicios de estrutura de decisao
## https://wiki.python.org.br/EstruturaDeRepeticao

## EXERCICIO 05

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota:'))

media = (nota1 + nota2) / 2

if(media >= 7 and media < 10):
	print('Aprovado')
elif(media < 7):
	print('Reprovado')
else:
	print('Aprovado com distinção')