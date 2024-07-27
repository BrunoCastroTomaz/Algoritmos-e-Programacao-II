'''
BRUNO CASTRO TOMAZ
EXERCÍCIOS DE MATRIZES
'''

#EXERCÍCIO 7.2

def populaMatriz(n): 
    M = []
    for i in range(n):
        linha  = []
        for j in range(n):
            x = float(input("Digite o elemento " + str(i) + str(j) + " da Matriz: "))
            linha.append(x)
        M.append(linha)
    return M

def diagonalPrincipal(M,n):
    vetDP = [0]*n
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i == j:
                vetDP[i] = M[i][j]
    return vetDP

def tracoMatriz(DP):
    soma  = 0
    for i in range(len(DP)):
        soma += DP[i]
    return soma

def imprimeMatriz(M):
    for i in range(len(M)):
        print(M[i],"\n")

def elementosNulos(M):
    cont = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i != j and M[i][j] == 0:
                cont += 1
    return cont
            
def main():
    n = int(input("Digite a ordem da matriz: "))
    M = populaMatriz(n)
    imprimeMatriz(M)
    DP = diagonalPrincipal(M,n)
    print("Vetor da Diagonal Principal: ", DP)
    print("Traço da Matriz: ", tracoMatriz(DP))
    print("Elementos nulos fora da diagonal principal: ", elementosNulos(M))
main()
