'''
Bruno Castro Tomaz
Algoritmos e Programação 2

Exercício de Laboratório: "Leitura de Arquivo"
'''
#Tarefa das notas dos alunos

def Nomes():
    arquivo_1 = open('classe.txt.txt','r')
    i = 0
    global lista_de_nomes#lista global para ser aproveitada em outras funções
    global numeros_dos_alunos#lista global para ser aproveitada em outras funções
    lista_de_nomes = []
    numeros_dos_Alunos = []
    for i in range(4):
        linha_1 = arquivo_1.readline().rstrip()
        numero_do_aluno = linha_1.split(' ')#isola o número dos alunos
        numeros_dos_Alunos.append(numero_do_aluno[0])#salva O NUMERO dos alunos em uma lista separada
        lista_de_nomes.append(numero_do_aluno[1].upper())#salva O NOME dos alunos em uma lista separada
        i+=1
    arquivo_1.close()
    return lista_de_nomes
    return numeros_dos_Alunos
    
def Notas():
    arquivo_2 = open('notas.txt.txt','r')
    j = 0
    global lista_de_notas#lista global para ser aproveitada em outras funções
    lista_de_notas =[]
    for i in range(4):
        linha_2 = arquivo_2.readline().rstrip()
        numero_do_aluno = linha_2.split(' ')#SEPARA o NÚMERO dos alunos de suas respectivas NOTAS
        notas = numero_do_aluno[1].split(':')#SEPARA AS 4 NOTAS DE CADA UM DOS 4 ALUNOS 
        lista_de_notas.append(notas)
        j+=1
    arquivo_2.close()
    return lista_de_notas

#Como a entrada pode ser fornecida tanto pelo número quanto pelo nome, deve-se conferir a entrada: 
def ConfereNumero(entrada):
    if entrada == '1':
        return lista_de_nomes[0]
    elif entrada == '2':
        return lista_de_nomes[1]
    elif entrada == '3':
        return lista_de_nomes[2]
    elif entrada == '4':
        return lista_de_nomes[3]
    else:
        return ''
def main():
    entrada = str(input("Por favor insira o nome ou número do aluno desejado: ")).upper()
    Nomes()#chama a função nomes para obter a lista de nomes salvos no arquivo 'classe.txt'
    escolha = ConfereNumero(entrada)#verifica se a entrada foi dada em NÚMEROS ou NOMES
    if escolha != '':
        entrada = escolha #atribui o valor da vaiável 'escolha' na variável 'entrada', apenas para facilitar as próximas etapas do código
        print("Nome do aluno:",entrada)
    else:
        
        print("Nome do aluno:",entrada)
    Notas()#chama a função notas para obter a lista de notas salvas no arquivo 'notas.txt'
    print("Notas deste aluno:")
    j = 0
    for j in range(4):
        if lista_de_nomes[j] == entrada:#verifica em que posição da lista de nomes está o valor fornecido como 'entrada'
            print(lista_de_notas[j])#verifica a mesma posição, AGORA NA LISTA DE NOTAS, e imprime a sequência de notas do aluno
        j+=1
    print("Espero ter ajudado!")
main()

