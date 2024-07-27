'''
ALGORITMOS E PROGRAMAÇÃO 02D11
BRUNO CASTRO TOMAZ
'''

#EXERCÍCIO 4
'''
Repita o exercício anterior, agora deve ser retornado em uma String os elementos que estão em A[] mas não estão em B[], ou seja, a diferença de A – B
'''
def diferenca(A,B):
    resp = ""
    for i in range(len(A)):
        flag = False
        for j in range(len(B)):
            if (A[i] == B[j]):
                flag = True            
        if flag == False:
            resp = resp + str(A[i]) + " "
        
    return resp
def main():
    A = [0]*5
    B = [0]*4
    
    A = [7,2,5,8,4]
    B = [4,2,9,5]
    
    print(A)
    print(B)
    
    print(diferenca(A,B))
    
main()
    

