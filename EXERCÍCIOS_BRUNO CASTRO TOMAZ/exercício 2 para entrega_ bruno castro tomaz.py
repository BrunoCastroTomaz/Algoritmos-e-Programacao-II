'''
Bruno Castro Tomaz
Algoritmos e Programação 2

'''

#Exercício 2
'''
Constrói uma tabela de jogos únicos entre os times
'''

FinaldoArquivo = False
vazio = ''
times = []

arquivo  = open('times.txt.txt','r')

while not FinaldoArquivo:
    linha = arquivo.readline()
    if linha == vazio:
        FinaldoArquivo = True
    else:
        time = linha.rstrip()
        times.append(time)
arquivo.close()
print("Jogos (Turno Único):\n")

i = 0
j = 0
for i in range(6):
    for j in range(6):
        if i < j:
            print(times[i],"X",times[j])
        else:
            continue
    j+=1
i+=1
