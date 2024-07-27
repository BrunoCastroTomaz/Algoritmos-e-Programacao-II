'''
BRUNO CASTRO TOMAZ
EXERCÍCIOS DE MATRIZES
'''

#EXERCÍCIO 7.3

def populaMatriz(n): 
    M = []
    for i in range(n):
        linha  = []
        for j in range(n):
            x = int(input("Digite o elemento " + str(i) + str(j) + " da Matriz: "))
            linha.append(x)
        M.append(linha)
    return M

def imprimeMatriz(M):
    for i in range(len(M)):
        print(M[i],"\n")

def verificaMatriz(M):
    cont = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i > j and M[i][j] == 0:
                cont += 1
    if cont == 0:
        return "A matriz não é triangular superior"
    return "A matriz é triangular superior"
            
def main():
    n = int(input("Digite a ordem da matriz: "))
    M = populaMatriz(n)
    imprimeMatriz(M)
    print("Dimensão da matriz: ", n , "x" , n)
    print(verificaMatriz(M))
main()

