'''
    Bruno Castro Tomaz
    ALGORITMOS E PROGRAMAÇÃO 2
'''
#EXERCÍCIO 2
'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando 
for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

a) Mostre a quantidade de valores que foram lidos;
b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d) Calcule e mostre a soma dos valores;
e) Calcule e mostre a média dos valores;
f) Calcule e mostre a quantidade de valores acima da média calculada;
g) Calcule e mostre a quantidade de valores abaixo de sete;
h) Encerre o programa com uma mensagem;

'''
import random
def quantidade(notas):
    return len(notas)

def ordemInversa(notas):
    notas.reverse()
    i = 0
    c = len(notas)
    while c > i:
        print(notas[i])
        i+=1

def media(notas):
    return (sum(notas)/len(notas))

def acimaMedia(notas):
    q = 0
    i = 0
    for i in range(len(notas)):
        if notas[i] > media(notas):
            q+=1
        i+=1
    return q

def abaixoSete(notas):
    Q = 0
    i = 0
    for i in range(len(notas)):
        if notas[i] < 7:
            Q+=1
        i+=1
    return Q

def main():
    notas = []
    for i in range(100):
        notas.append(float(input()))
        if notas[i] <= -1.0:
            notas.pop()
            break
    #letra a
    print("quantidade de valores lidos: ",quantidade(notas))
    #letra b
    print("valores em ordem de digitação: ",notas)
    #letra c
    print("valores em ordem inversa:")
    ordemInversa(notas)
    #letra d
    print("Soma dos valores:",sum(notas))
    #letra e
    print("media dos valores:",media(notas))
    #letra f
    print("Quantidade de valores acima da média:",acimaMedia(notas))
    #letra g
    print("Quantidade de valores abaixo de 7:",abaixoSete(notas))
    #letra h
    print("Espero ter ajudado!Bom dia!!")

main()   
