#Nome do time : ESTADO

num_times= int(input('Número de times: '))

meu_arquivo = open('times_campeonato.txt','w')

for cont in range(num_times):
    nome = input('Nome do time número ' + str(cont+1) + ': ')
    estado = input('Estado do time número ' + str(cont+1) + ': ')
    meu_arquivo.write(nome + ':'+ estado+'\n')
meu_arquivo.close()

#leitura do arquivo usando for
times_arquivo= open('times_campeonato.txt','r')
for linha in times_arquivo:
    print("Nome do time:", linha.rstrip())
times_arquivo.close()

