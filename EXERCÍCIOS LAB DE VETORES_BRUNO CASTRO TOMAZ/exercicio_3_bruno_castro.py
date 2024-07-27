'''
ALGORITMOS E PROGRAMAÇÃO 02D11
BRUNO CASTRO TOMAZ
'''

#EXERCÍCIO 3
'''
Escreva uma função que recebe dois vetores inteiros A[] e B[], em seguida, a sua função efetua a INTERSECÇÃO entre os vetores, ou seja, os elementos em comum entre os dois vetores, ao final sua função retorna uma String com a resposta. Os vetores dados não possuem valores duplicados e não estão ordenados.
'''
def intersec(A,B):
    resp = ""
    for i in range(len(A)):
        flag = False
        for j in range(len(B)):
            if (A[i] == B[j]):
                flag = True            
        if flag == True:
            resp = resp + str(A[i]) + " "
        
    return resp
def main():
    A = [0]*5
    B = [0]*4
    
    A = [7,2,5,8,4]
    B = [4,2,9,5]
    
    print(A)
    print(B)
    
    print(intersec(A,B))
    
main()
    

