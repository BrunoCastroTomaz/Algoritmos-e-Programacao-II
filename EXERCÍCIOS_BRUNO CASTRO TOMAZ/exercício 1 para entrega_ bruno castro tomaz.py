'''
Bruno Castro Tomaz
Algoritmos e Programação 2
'''

#Exercício 1
'''
Abre o arquivo times.txt e apresenta os times em ordem alfabética
'''

FinaldoArquivo = False
vazio = ''
times = []

arquivo  = open('times.txt.txt','r')
print("Times em ordem alfabética:")

while not FinaldoArquivo:
    linha = arquivo.readline()
    if linha == vazio:
        FinaldoArquivo = True
    else:
        time = linha.rstrip()
        times.append(time)
arquivo.close()
times = sorted(times)

i = 0
while i < 6:
    print(times[i])
    i+=1

    
