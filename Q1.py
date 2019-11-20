#Nome: Yuri Pereira Dantas
#Questao 1 da P2 de Comp1 / Professor Juliano
#versao: do jeito exato que escrevi na minha prova

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
    if condicao[4] == \ : #Aqui esqueci de botar a contrabarra entre aspas
        condicao1 = condicao[0]
        condicao2 = condicao[1]
        condicao3 = condicao[2]
        condicao = condicao1 + condicao2 + condicao3
        booleana = TRUE #Aqui esqueci que so a primeira letra e maiuscula do True
        if condicao == 'SIM':
            return booleana
        elif condicao == 'NAO':
            booleana = FALSE #Cometi o mesmo erro aqui sobre somente a primeira letra ser maiuscula
            return booleana

#Questao 1c)

def separador(lista):
    listanova = [] 
    i = 0
    tamanho = len(lista)
    for cont in range (tamanho):
        if lista[cont] == ':':
            while i < cont:
                listanova[i] = lista[i]
                i = i + 1
            i = i +1
    return listanova

def arqlista(fd):
    lista = fd.readlines()
    return lista

def main():
    fd = fd.open('cadastro'.txt, 'r')
    list = []
    list = arqlista(fd)
    list = separador
