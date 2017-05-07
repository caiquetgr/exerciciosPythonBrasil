## http://wiki.python.org.br/ListaDeExercicios
## Caique Borges
## Exercicios de estrutura sequencial
## http://wiki.python.org.br/EstruturaSequencial

## EXERCICIO 4

def media(n1, n2, n3, n4):
    return (n1+n2+n3+n4)/4

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))

print('A media das notas eh', media(n1,n2,n3,n4))