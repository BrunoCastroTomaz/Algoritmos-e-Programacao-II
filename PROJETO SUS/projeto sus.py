'''
                         PROJETO 1 - SUS COVID-19

            Bruno Castro Tomaz
            Professora Ana Grasielle Dionísio Corrêa
'''

def geraListas(geral):
    global sintomas
    global profissionalSaude
    global estadoTeste
    global tipoTeste
    global resultadoTeste
    global sexo
    global estado
    global municipio
    global idade
    sintomas = []
    profissionalSaude = []
    estadoTeste = []
    tipoTeste = []
    resultadoTeste = []
    sexo = []
    estado = []
    municipio = []
    idade = []
    for i in range(1,len(geral)):
        dados = []
        dados = geral[i].split(';')
        sintomas.append(dados[0])
        profissionalSaude.append(dados[1])
        estadoTeste.append(dados[2])
        tipoTeste.append(dados[3])
        resultadoTeste.append(dados[4])
        sexo.append(dados[5])
        estado.append(dados[6])
        municipio.append(dados[7])
        idade.append(dados[8])
        i += 1
def ContaGenero():
    qtde_Homens = 0
    qtde_Mulheres = 0
    geraListas(geral)
    for i in range(len(sexo)):
        if sexo[i] == "Masculino":
            qtde_Homens += 1
        elif sexo[i] == "Feminino":
            qtde_Mulheres += 1
    meninos = (qtde_Homens/len(sexo))
    meninas = (qtde_Mulheres/len(sexo))
    print("2) Quantidade de pessoas do sexo masculino: ", qtde_Homens, "(",end = '')
    print(f"{meninos:.2%})")
    print("3) Quantidade de pessoas do sexo feminino: ", qtde_Mulheres, "(",end = '')
    print(f"{meninas:.2%})")
def Positivo():
    qtde_positivo = 0
    qtde_homem_positivo = 0
    qtde_mulher_positivo = 0
    for i in range(len(resultadoTeste)):
        if (resultadoTeste[i] == "Positivo"):
            qtde_positivo += 1
            if (sexo[i] == "Masculino"):
                qtde_homem_positivo += 1
            elif (sexo[i] == "Feminino"):
                qtde_mulher_positivo += 1
    Garoto = (qtde_homem_positivo/qtde_positivo)
    Garota = (qtde_mulher_positivo/qtde_positivo)
    print("4) Quantidade de pessoas que testaram positivo: ", qtde_positivo)
    print("5) Quantidade de homens que testaram positivo: ", qtde_homem_positivo, "(",end = '')
    print(f"{Garoto:.2%})")
    print("6) Quantidade de mulheres que testaram positivo: ", qtde_mulher_positivo, "(",end = '')
    print(f"{Garota:.2%})")
def TipoTeste():
    qtde_RT = 0
    qtde_TesteRapido = 0
    for i in range(len(tipoTeste)):
        if tipoTeste[i] == "RT-PCR":
            qtde_RT += 1
        elif tipoTeste[i] == "TESTE RÁPIDO - ANTICORPO":
            qtde_TesteRapido += 1
    Pessoa1 = (qtde_RT/len(tipoTeste))
    Pessoa2 = (qtde_TesteRapido/len(tipoTeste))
    print("7) Quantidade de pessoas que fizeram o teste do tipo “RT-PCR”: ", qtde_RT,"(",end='')
    print(f"{Pessoa1:.2%})")
    print("8) Quantidade de pessoas que fizeram o teste do tipo “teste rápido - anticorpo”: ", qtde_TesteRapido,"(",end='')
    print(f"{Pessoa2:.2%})")
def Sintomas():
    assint = 0
    febre = 0
    cabeca = 0
    garganta = 0
    for i in range(len(sintomas)):
        if sintomas[i] == "Assintomático":
            assint += 1
        elif sintomas[i] == "Febre":
            febre += 1
        elif sintomas[i] == "Dor de Cabeça":
            cabeca += 1
        elif sintomas[i] == "Dor de Garganta":
            garganta += 1
    PessoaA = (assint/len(sintomas))
    PessoaB = (febre/len(sintomas))
    PessoaC = (cabeca/len(sintomas))
    PessoaD = (garganta/len(sintomas))
    print("9) Quantidade de pessoas assintomáticas: ", assint,"(",end='')
    print(f"{PessoaA:.2%})")
    print("10) Quantidade de pessoas que relataram ter sentido febre: ", febre,"(",end='')
    print(f"{PessoaB:.2%})")
    print("11) Quantidade de pessoas que relataram ter sentido dor de cabeça: ", cabeca,"(",end='')
    print(f"{PessoaC:.2%})")
    print("12) Quantidade de pessoas que relataram ter sentido dor de garganta: ", garganta,"(",end='')
    print(f"{PessoaD:.2%})")
def Sintomatico():
    mulherAssint = 0
    pessoaSint = 0
    for i in range(len(idade)):
        if (int(idade[i]) > 50) and (sexo[i] == "Feminino") and (sintomas[i] == "Assintomático"):
            mulherAssint += 1
        elif (sintomas[i] != "Assintomático") and (int(idade[i]) < 20):
            pessoaSint += 1
    porcent = (mulherAssint/len(idade))
    Menorde20 = (pessoaSint/len(sintomas))
    print("13) e 14) Quantidade de mulheres, acima de 50 anos, assintomáticas: ", mulherAssint, "(",end = '')
    print(f"{porcent:.2%})")
    print("15) Quantidade de pessoas com menos de 20 anos sintomáticos: ", pessoaSint, "(",end = '')
    print(f"{Menorde20:.2%})")
def SintomasEmSP():
    SintSP = 0
    mulherDracena= 0
    Maisque50Bauru = 0
    for i in range(len(sintomas)):
        if (sintomas[i] != "Assintomático") and (municipio[i] == "São Paulo"):
            SintSP += 1
        elif (sintomas[i] != "Assintomático") and (municipio[i] == "Dracena") and (sexo[i] == "Feminino"):
                mulherDracena += 1
        elif (sintomas[i] != "Assintomático") and (municipio[i] == "Bauru") and (sexo[i] == "Masculino") and (int(idade[i]) > 50):
                Maisque50Bauru += 1
    pessoaSP = (SintSP/len(sintomas))
    pessoaDracena = (mulherDracena/len(sintomas))
    HomemBauru = (Maisque50Bauru/len(sexo))        
    print("16) Quantidade de sintomáticos na cidade de São Paulo: ", SintSP, "(",end = '')
    print(f"{pessoaSP:.2%})")
    print("17) Quantidade de mulheres sintomáticas na cidade de Dracena: ", mulherDracena, "(",end = '')
    print(f"{pessoaDracena:.2%})")
    print("18) Quantidade de homens, maiores de 50 anos, sintomáticos na cidade de Bauru: ", Maisque50Bauru, "(",end = '')
    print(f"{HomemBauru:.2%})")
def main():
    finalDoArquivo = False
    stringVazia = ''
    print('1) Quantidade de pessoas que fizeram o teste:', end =' ')    
    global geral
    geral = []
    arquivo = open('SUS-covid19.txt.txt', 'r', encoding="utf=8", errors = 'ignore')
    linha = arquivo.readline()
    while not finalDoArquivo:
        linha = arquivo.readline()
        if linha == stringVazia:
            finalDoArquivo = True
        else:
            pessoa = linha.rstrip()
            geral.append(pessoa)
    arquivo.close()
    print(len(geral))
    geraListas(geral)
    ContaGenero()
    Positivo()
    TipoTeste()
    Sintomas()
    Sintomatico()
    SintomasEmSP()
main()
