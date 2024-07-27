# Autores:
# BRUNO CASTRO TOMAZ 
# CAUE MACEDO DE SOUZA

'''
SIMULADOR DE MEGA-SENA EM PYTHON
'''
import random

def geraApostas():
    aposta = [0]*6
    for i in range(len(aposta)):
        aposta[i] = random.randint(1,60)
    i = 0
    for j in range(len(aposta)-1):
        flag = False
        if aposta[i] == aposta[j+1]:
            flag = True
        if flag == True:
            aposta[j+1] = random.randint(1,60)
    return aposta

def registraApostas(arq):
    n = 0
    auxiliar = []
    while n < 100000:
        apostador = geraApostas()
        for i in range(len(apostador)):
            arq.write(str(apostador[i]) + " ")
        arq.write("\n")
        auxiliar.append(apostador)
        n+=1
    return auxiliar

def geraResultado(auxiliar):
    sorteio = random.randint(0,9)
    global Resultado
    Resultado = auxiliar[sorteio]
    return Resultado

def sena(Sena):
    return Sena+1
def quina(Quina):
    return Quina+1
def quadra(Quadra):
    return Quadra+1

def SorteGrande(result,auxiliar,auxiliar_2):
    global Sena
    global Quina
    global Quadra
    Sena = 0
    Quina = 0
    Quadra = 0
    Conta_Acertos = 0
    for j in range(len(auxiliar_2)):
        for k in range(len(result)):
            if  auxiliar_2[j]  == result[k] :
                Conta_Acertos += 1
    if Conta_Acertos == 6:
        Sena = sena(Sena)
    elif Conta_Acertos == 5:
        Quina = quina(Quina)
    elif Conta_Acertos == 4:
        Quadra = quadra(Quadra)
        
def sortudos(auxiliar):
    global auxiliar_2
    for i in range(len(auxiliar)):
        auxiliar_2  = auxiliar[i]
        SorteGrande(result,auxiliar,auxiliar_2)
    print("S = ",Sena)
    print("QI = ",Quina)
    print("Qa = ", Quadra)   

def geraRelatorio(premio,result):
    divisao6 = 0
    divisao5 = 0
    divisao4 = 0    
    result5 = str(Resultado[1]) + " " + str(Resultado[2]) + " " + str(Resultado[3]) + " " + str(Resultado[4]) + " " + str(Resultado[5])
    result4 = str(Resultado[2]) + " " + str(Resultado[3]) + " " + str(Resultado[4]) + " " + str(Resultado[5])
    if Sena != 0:
        premio6 = (62*premio)/100
        divisao6 = premio6/Sena
        premio5 = (19*premio)/100
        premio4 = (19*premio)/100
    elif Quina != 0:
        premio6 = 0
        premio5 = premio/2
        premio4 = premio/2
        divisao5 = premio5/Quina
        divisao4 = premio4/Quadra
    elif Quadra != 0:
        premio6 = 0
        premio5 = 0
        premio4 = premio
    else:
        premio6 = 0
        premio5 = 0
        premio4 = 0
    relatorio = open('arquivo_de_saida.txt', 'w')
    relatorio.write("CONCURSO MEGA SENA DA VIRADA\n" + "PRÊMIO: " + str(premio) + "\n")
    relatorio.write("NÚMEROS SORTEADOS\n" + str(result) + "\n" + "GANHADORES\n")
    relatorio.write("FAIXA | NÚMEROS SORTEADOS | GANHADORES | PREMIO | DIVISAO\n")
    relatorio.write("SENA | " + str(result) + "| " + str(Sena) + " | " + str(premio6) + " | " + str(divisao6) + "\n")
    relatorio.write("QUINA | " + str(result5) + "| " + str(Quina) + " | " + str(premio5) + " | " + str(divisao5) + "\n")
    relatorio.write("QUADRA | " + str(result4) + "| " + str(Quadra) + " | " + str(premio4) + " | " + str(divisao4) + "\n")
    if Sena == 0 and Quina == 0 and Quadra == 0:
        relatorio.write("PRÊMIO ACUMULADO!!")
    else:
        relatorio.write("NÃO ACUMULADO!!")

def main():
    global result
    premio = int(input("Insira o valor do prêmio da mega-sena: "))
    arq = open('Apostas.txt','w')
    auxiliar = registraApostas(arq)
    result = geraResultado(auxiliar)
    for i in range(len(auxiliar)):
        print(auxiliar[i],"\n")
    print("resultado:", result)
    arq = open('Apostas.txt','r')
    print(SorteGrande(result,auxiliar,auxiliar_2))
    ganhadores = sortudos(auxiliar)
    arq.close()
    geraRelatorio(premio,result)
    
main()
