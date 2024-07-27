'''
ALGORITMOS E PROGRAMAÇÃO 02D11
BRUNO CASTRO TOMAZ
'''

#EXERCÍCIO 5
'''
Escreva uma função que recebe dois vetores inteiros A[] e B[], em seguida, a sua função efetua a UNIÃO entre os vetores, ou seja, os elementos do vetor A mais aos elementos do vetor B, desde que os elementos de B não estejam presentes no vetor A, ao final sua função retorna uma String com a resposta. Os vetores dados não possuem valores duplicados e não estão ordenados.
'''
def uniao(A,B):
    resp = ""
    U = []
    uniaoTemporaria = A + B
    for i in uniaoTemporaria:
        if i not in U:
            resp = resp + str(i) + " "
            U.append(i)
    return resp
def main():
    A = [0]*5
    B = [0]*4
    
    A = [7,2,5,8,4]
    B = [4,2,9,5]

    #A = [0]*3
    #B = [0]*3
    
    #A = [3,9,11]
    #B = [2,6,1]
    
    print(A)
    print(B)
    
    print(uniao(A,B))
    
main()
    
