# BRUNO CASTRO TOMAZ
# ALGORITMOS E PROGRAMAÇÃO 2
# EXERCÍCIO 3:
'''
Considere o problema de encontrar todos números primos existentes entre N1 e N2 (inclusive), em que N1 e N2 são números naturais lidos.
Para resolver o problema escreva a função def ehPrimo(n), que verifica se um número é primo, com a função pronta escreva um programa que
utiliza a função ehPrimo() para resolver o problema descrito acima. 
'''
def ehPrimo(n):
    mult = 0
    for count in range (N1,n):
        if n % count == 0:
            print ("Múltiplo de ", count)
            mult +=1
    if mult == 0:
        print("É primo")
    else:
        print("Tem", mult, " múltiplos acima de 2 e abaixo de", n)
def main ():
    global N1
    global N2
    N1 = int(input())
    N2 = int(input())
    ehPrimo(N2)
main()
