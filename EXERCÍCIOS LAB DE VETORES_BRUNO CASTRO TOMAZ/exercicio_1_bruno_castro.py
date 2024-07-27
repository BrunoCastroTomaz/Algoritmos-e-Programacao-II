'''
ALGORITMOS E PROGRAMAÇÃO 02D11
BRUNO CASTRO TOMAZ
'''

#EXERCÍCIO 1
'''
Escreva uma função que recebe um vetor e retorna o vetor invertido, para o vetor abaixo:
V = [ 4, 9, 10, 8, 6] o vetor V invertido é 
igual a [6, 8, 10, 9, 4] 
Resolva essa questão sem utilizar o método reverse() para listas e sem usar um vetor auxiliar v2.
'''
def geraVetor(tamanho):
    V = [0]*tamanho
    for i in range(len(V)):
        V[i] = int(input("Digite um valor:"))
    return V

def Inverte(Vetor):
    j = len(Vetor)-1
    auxiliar = 0
    for i in range(len(Vetor)//2):
        auxiliar = Vetor[i]
        Vetor[i] = Vetor[j]
        Vetor[j] = auxiliar
        i+=1
        j-=1
    return Vetor
def main():
    tamanho = int(input("Digite o tamanho do vetor: "))
    Vetor = geraVetor(tamanho)
    print("O vetor original: ",Vetor)
    Vetor_invertido = Inverte(Vetor)
    print("O vetor invertido: ",Vetor_invertido)
main()
