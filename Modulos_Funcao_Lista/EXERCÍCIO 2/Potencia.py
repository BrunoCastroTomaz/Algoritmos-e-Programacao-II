# BRUNO CASTRO TOMAZ
# ALGORITMOS E PROGRAMAÇÃO 2
# EXERCÍCIO 2:
'''
Imagine agora que o Python não possui o operador de potência (**), sabemos que a potência pode ser definida através de multiplicações sucessivas:
x^y = x * x ...* x ou seja x multiplicado y vezes. Para x =4 e y = 5 teremos 4*4*4*4*4, ou seja, 4 multiplicado 5 vezes. 

Escreva a função  def potencia(x,y): que tem como entrada x e y e calcule a potência de xy.
'''

def potencia(x,y):
    m = 1
    while y>0:
        m = m * x
        y = y - 1
    return m
def main ():
    x = int(input())
    y = int(input())
    print(potencia(x,y))
main()
