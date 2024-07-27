'''
    BRUNO CASTRO TOMAZ
    ALGORITMOS E PROGRAMAÇÃO 2 AULA DE TEORIA
    "CALCULADORA DE POLINÔMIOS"
'''
def geraPolinomio(vet):
    POLINOMIO = " "
    if vet[0] != 0:
        POLINOMIO =  str(vet[0])
    
    for i in range(1,len(vet)):
        if vet[i] != 0:
            if i==1 and vet[i]>0:
                POLINOMIO += " + " + str(vet[i]) + 'x^' + str(i) + " "
            if vet[i]>0 and i>1:
                POLINOMIO += " + " + str(vet[i]) + 'x^' + str(i) + " "
            elif vet[i]<0:
                POLINOMIO += " "+ str(vet[i]) + 'x^' + str(i) + " "
    print ("polinomio: ",POLINOMIO)

def menu():
    return ''' MENU
    a) Calcular o valor de um polinômio
    b) Calcular a soma de polinômios\n
    '''

def CalculaValor(x,vet):
    Polinomio = 0
    for i in range(0,len(vet)):
        Polinomio += (vet[i] * (x**i))
    return Polinomio

def CalculaSoma(vet,vet_2):
    Soma = 0
    for i in range(len(vet)):
        Soma += ('x^' + str(i)) + str(vet[i] + vet_2[i])
    return Soma

def main():
    grau = int(input("grau do polinomio: "))
    grau += 1
    vet = [0]*grau
    for i in range((len(vet)-1), -1, -1):
        vet[i] = int(input("digite o " + str(i) + " numero: "))
    geraPolinomio(vet)
    flag = True
    while flag:
        print(menu())
        opcao = str(input("Escolha uma opção do menu: "))
        if opcao == "a":
            x = int(input("Insira um valor para x: "))
            print(CalculaValor(x,vet))
        elif opcao == "b":
            grau = int(input("grau do polinomio: "))
            grau += 1
            vet_2 = [0]*grau
            for i in range((len(vet_2)-1), -1, -1):
                vet_2[i] = int(input("digite o " + str(i) + " numero: "))
            geraPolinomio(vet_2)
            print(CalculaSoma(vet,vet_2))
        else:
            flag = False        
    
main()
