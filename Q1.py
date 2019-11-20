#Nome: Yuri Pereira Dantas
#Questao 1 da P2 de Comp1 / Professor Juliano
#versao: Corrigido

#Questao 1a)

def dict_Data(data):
    ano1 = data[0]
    ano2 = data[1]
    ano3 = data[2]
    ano4 = data[3]
    ano = ano1 + ano2 + ano3 + ano4
    ano = int(ano)
    mes1 = data[5]
    mes2 = data[6]
    mes = mes1 + mes2
    mes = int(mes)
    dia1 = data[8]
    dia2 = data[9]
    dia = dia1 + dia2
    dia = int(dia)
    datadict = {
        'day': '',
        'month': '',
        'year': ''
    }
    datadict['day'] = dia
    datadict['month'] = mes
    datadict['year'] = ano
    return datadict

#Questao 1b)

def verificarAtivo(condicao): #condicao eh string
    if condicao[4] == 'n' : 
        condicao1 = condicao[0]
        condicao2 = condicao[1]
        condicao3 = condicao[2]
        condicao = condicao1 + condicao2 + condicao3
        booleana = True 
        if condicao == 'SIM':
            return booleana
        elif condicao == 'NAO':
            booleana = False 
            return booleana

#Questao 1c)

def separador(lista):
    listanova = lista.split(':')
    return listanova

#Questao 1d)
def arqlista(fd):
    fd.seek(0)
    lista = fd.readlines()
    return lista

def main():
    clientes = []
    arquivo = open('cadastro.txt','r')

    dic_cadastro = {'CPF':'',
             'NOME':'',
             'DATA_DE_NASCIMENTO':'',
             'DATA_DO_CADASTRO':'',
             'ATIVO':''
    }
    
    linhasDoArquivo = arqlista(arquivo)

    for cont in range(len(linhasDoArquivo)):
        dic_CadastroAtual = dic_cadastro.copy()
        dadosPessoais = separador(linhasDoArquivo[cont])
        dic_CadastroAtual['CPF'] = dadosPessoais[0]
        dic_CadastroAtual['NOME'] = dadosPessoais[1]
        dic_CadastroAtual['DATA_DE_NASCIMENTO'] = dict_Data(dadosPessoais[2])
        dic_CadastroAtual['DATA_DO_CADASTRO'] = dict_Data(dadosPessoais[3])
        dic_CadastroAtual['ATIVO'] = verificarAtivo(dadosPessoais[4])
        clientes.append(dic_CadastroAtual)

    print(clientes)

    arquivo.close()

main()

