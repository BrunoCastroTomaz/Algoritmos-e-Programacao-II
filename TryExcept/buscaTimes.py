'''
O arquivo times_sp.txt deve conter somente os nomes dos times do estado de São Paulo.
'''
times_arquivo = open('times_campeonato.txt', 'r')
times_sp_arquivo = open('times_sp.txt', 'w')
for linha in times_arquivo:
    registro_time = linha.rstrip()
    info_time = registro_time.split(':')
    nome = info_time[0]
    estado = info_time[1]
    if estado == 'SP':
        times_sp_arquivo.write(nome + '\n')
        
times_arquivo.close()
times_sp_arquivo.close()
