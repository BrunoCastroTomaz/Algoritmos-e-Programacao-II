'''
ALGORITMOS E PROGRAMAÇÃO 02D11
BRUNO CASTRO TOMAZ
'''

#EXERCÍCIO 6
'''
Escreva uma função que preencha por leitura do teclado um vetor de 10 posições e retorna a quantidade de valores diferentes que existem no vetor. 
'''
def vetor(A):
    i = 0
    c = 1
    while i < 10:
        A[i]  = int(input())
        i += 1
    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[i] != A[j+1]:
                c += 1
        break
    return c
def main():
    A = [0]*10
    print(vetor(A))    
main()
    
