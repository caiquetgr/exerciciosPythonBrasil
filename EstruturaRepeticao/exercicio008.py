## http://wiki.python.org.br/ListaDeExercicios
## Caique Borges
## Exercicios de estrutura de repetição
## https://wiki.python.org.br/EstruturaDeRepeticao

## EXERCICIO 08

print('Insira 5 numeros:')
numeros = []
soma = 0

for i in range(1, 5+1):
	numero = int(input('Insira o {}º numero: '.format(i)))
	numeros.append(numero)

for i in range(0, len(numeros)):
	soma += numeros[i]

print(soma)