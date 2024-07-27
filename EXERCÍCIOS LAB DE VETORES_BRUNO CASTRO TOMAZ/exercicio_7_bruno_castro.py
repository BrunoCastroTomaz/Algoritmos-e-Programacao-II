'''
ALGORITMOS E PROGRAMAÇÃO 02D11
BRUNO CASTRO TOMAZ
'''

#EXERCÍCIO 7
'''
Escreva uma função que recebe um vetor contendo 5 números inteiros e um valor x. A função deverá devolver a posição em que o valor x (lido do teclado) está no vetor. Caso o valor x não seja encontrado, a função deve retornar o valor -1 
'''
def procuraX(V):
    i = 0
    while i < 6:
        V[i]  = int(input("Insira numeros inteiros: "))
        i += 1
    x = int(input("digite um valor x:"))
    aux = 0
    for i in range(len(V)):
        if V[i] == x:
            print("o valor x está na posição", i, "do vetor")
            aux += 1
    if aux == 0:
        print(-1)
def main():
    V = [0]*6
    procuraX(V)
main()
    
