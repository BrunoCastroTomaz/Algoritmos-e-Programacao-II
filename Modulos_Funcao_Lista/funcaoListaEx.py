#Escreva uma função que receba como parâmetro uma lista de inteiros e retorne como resposta a soma de todos os elementos da lista.
def soma(lst):
    soma = 0
    for i in lst:
        soma += i
    return soma
def main():
    lista = [2,5,8,10,14,33]
    print("Soma: ", soma(lista))
main()
