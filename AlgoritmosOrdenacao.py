'''
O código aqui desenvolvido busca comparar a eficiência dos algoritmos de ordenação BubbleSort, SelectionSort e InserctionSort
'''
import random
import time

def bubble_sort(lista,comp,trocas,tempo):
    ini = time.time()
    for i in range(len(lista)):
        for y in range(len(lista)-1):
            comp[0] += 1 
            if lista[y] > lista[y+1]:
                aux = lista[y]
                lista[y] = lista[y+1]
                lista[y+1] = aux
                trocas[0] += 1 
    fim = time.time()
    tempo[0] = fim - ini
    return lista

def selection_sort(lista,comp,trocas,tempo):
    ini = time.time()
    for i in range(len(lista)):
        min = i
        for j in range(i+1,len(lista)):
            comp[1] += 1 
            if lista[min] > lista[j]:
                min = j
        aux = lista[min]
        lista[min] = lista[i]
        lista[i] = aux
        trocas[1] += 1 
    fim = time.time()
    tempo[1] = fim - ini
    return lista

def inserction_sort(lista,comp,trocas,tempo):
    ini = time.time()
    for i in range(1,len(lista)):
        x = lista[i]
        j = i-1
        while j >= 0 and x < lista[j]:
            lista[j+1] = lista[j]
            trocas[2] += 1
            comp[2] += 1 
            j -= 1
        comp[2] += 1 
        lista[j+1] = x
    fim = time.time()
    tempo[2] = fim - ini
    return lista

def gera_lista(val,crescente,decrescente):
    vet = [0]*val
    for i in range(val):
        vet[i] = random.randint(1,100)
    if crescente == True:
        vet.sort()
    elif decrescente == True:
        vet.sort(reverse = True)
    return vet

def main():
    comp = [0]*3
    trocas = [0]*3
    tempo = [0]*3

    algori = ["BubbleSort", "SelectionSort", "InserctionSort"]
    print("1- lista crescente\n2- lista decrescente\n3 - lista aleatoria\n")

    ordem = int(input())

    valor = int(input("digite o tamanho do vetor: "))
    if ordem == 1:
        lista1 = gera_lista(valor,True,False)
    elif ordem == 2:
        lista1 = gera_lista(valor,False,True)
    else:
        lista1 = gera_lista(valor,False,False)

    lista2= [0]*valor
    lista3 = [0]*valor
    for i in range(len(lista1)):
        lista2[i] = lista1[i]
        lista3[i] = lista1[i]

    print("vetor=\n",lista1)
    
    bubble_sort(lista1,comp,trocas,tempo)
    selection_sort(lista2,comp,trocas,tempo)
    inserction_sort(lista3,comp,trocas,tempo)
    
    print("vet ordenado=\n", lista1)
    print("===================================")
    for i in range(3):
        print(algori[i], ";")
        print("COMPARAÇÕES = ", comp[i])
        print("TROCAS = ", trocas[i])
        print("TEMPO(s) = ", tempo[i])
        print("=================================")

main()
