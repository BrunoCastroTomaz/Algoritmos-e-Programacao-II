'''
    Bruno Castro Tomaz
    ALGORITMOS E PROGRAMAÇÃO 2
'''
#EXERCÍCIO 1
'''
Escreva uma função geraLista() que receba como parâmetro um número inteiro n representando o tamanho de uma lista 
e devolve uma lista de n números inteiros gerados aleatoriamente. Escreva outra função somaLista() que recebe a lista de inteiros 
gerada pela função geraLista() e retorne como resposta a soma de todos os elementos da lista.
'''

import random
def geraLista(n):
    lista = []
    for i in range (n):
        lista.append(random.randint(1,100))
    return lista
def somaLista(lista):
    soma = 0
    for i in lista:
        soma+=i
    return soma
def main():
    n = int(input())
    lista = geraLista(n)
    soma = somaLista(lista)
    print(lista)
    print(soma)
main()
