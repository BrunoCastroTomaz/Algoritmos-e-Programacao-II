'''
Para evitar a interrupção abrupta da execução do programa, as exceções podem ser capturadas e tratadas. Para isso, utiliza-se a estrutura try-except.

Dentro do bloco try coloca-se a sentença que podem gerar a exceção e as sentenças que dependem do sucesso da execução desta primeira sentença.

Para tratar a exceção, identificamos a exceção que será tratada (no nosso caso FileNotFoundError) logo após a palavra except e definimos um bloco com o que deverá ser executado caso a exceção ocorra.
'''

nome_arquivo = input('Nome do arquivo com os dados do time: ')

try:
    times_arquivo= open(nome_arquivo,'r')
    print('Arquivo', nome_arquivo, 'encontrado!')
    for linha in times_arquivo:
        print("Nome do time:", linha.rstrip())
    times_arquivo.close()

except FileNotFoundError:
    print('O arquivo', nome_arquivo, 'não foi encontrado!')
