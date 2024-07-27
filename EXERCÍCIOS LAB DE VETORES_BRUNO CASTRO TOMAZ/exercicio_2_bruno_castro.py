'''
ALGORITMOS E PROGRAMAÇÃO 02D11
BRUNO CASTRO TOMAZ
'''

#EXERCÍCIO 2
'''
Escreva uma função que recebe um vetor de número inteiros, e verifica se os elementos do vetor estão em ordem crescente, função retorna True caso os elementos estejam em ordem crescente e False caso contrário
'''
import random
def geraVetor(tamanho):
    V = [0]*tamanho
    for i in range(len(V)):
        V[i] = random.randint(1,80)
    return V
def verificaOrdem(Vetor):
    for i in range(len(Vetor)-1):
        if Vetor[i] > Vetor[i+1]:
            return False
    return True
def main():
    tamanho = int(input("digite o tamanho do vetor:"))
    Vetor = geraVetor(tamanho)
    print(Vetor)
    print(verificaOrdem(Vetor))
main()
    

