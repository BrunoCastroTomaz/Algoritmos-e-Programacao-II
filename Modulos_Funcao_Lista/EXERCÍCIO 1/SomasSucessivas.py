# BRUNO CASTRO TOMAZ
# ALGORITMOS E PROGRAMAÇÃO 2
# EXERCÍCIO 1:
'''
Imagine que o Python não possui mais o operador de multiplicação (*), por sorte os matemáticos definiram que a multiplicação pode ser definida
através de somas sucessivas: a*b = a + a ...+ a ou seja a somado b vezes. Para a =4 e b = 5 teremos 4+4+4+4+4, ou seja, 4 somado 5 vezes.
Escreva a função def mult(a, b): que tem como entrada a e b, a função calcula e devolve a multiplicação de a*b utilizando a regra acima.
'''

def mult (a,b):
    m = 0
    while b > 0:
        m = m + a
        b = b - 1
    return m
def main ():
    a = int(input())
    b = int(input())
    print(mult(a,b))
main()
