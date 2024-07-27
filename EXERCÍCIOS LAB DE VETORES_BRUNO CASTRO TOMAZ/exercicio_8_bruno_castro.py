'''
ALGORITMOS E PROGRAMAÇÃO 02D11
BRUNO CASTRO TOMAZ
'''

#EXERCÍCIO 8
'''
Escreva uma função que receba dois vetores de 3 posições, que representam forças sobre um ponto no espaço 3D e retorna o valor da força resultante. 
Dica: força resultante é obtida pela soma dos valores das coordenadas correspondentes nos dois vetores: (x1 + x2), (y1 + y2), (z1 + z2)

Exemplo:
Vet1 = {x1, y1, z1}
Vet2 ={x2, y2, z2}
'''

def forcaResultante(V1,V2):
    i = 0
    while i < 3:
        V1[i] = int(input())
        V2[i] = int(input())
        i += 1
    Fr = 0
    for i in range(len(V1)):
            Fr += V1[i] + V2[i]
    return Fr
def main():
    V1 = [0]*3
    V2 = [0]*3
    print(forcaResultante(V1,V2))
main()
    
