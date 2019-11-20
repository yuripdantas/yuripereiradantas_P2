#Nome: Yuri Pereira Dantas
#Questao 2 da P2 de Comp1 / Professor Juliano
#versao: do jeito exato que escrevi na minha prova

def calculaDet(matrix):
    return(matrix[0][0]*matrix[1][1]) - (matrix[1][0]*matrix[0][1])

def inverterMatriz (matrix):
    determinante = calculaDet(matrix)
    if determinante != 0:
        matrix[0][0], matrix[1][1] = changeValues(matrix[0][0], matrix[1][1])
        matrix[0][1] = - matrix[0][1]
        matrix[1][0] = - matrix[1][0]
        for n in range (len(matrix)):
            for m in range (len(matrix[0])):
                matrix[n][m] = matrix[n][m]/determinante
        return matrix
    else:
        return None

def changeValues(a, b):
    a = a + b
    b = a - b
    a = a-b
    return a, b

def imprimeMatriz(matrix, nlinhas, ncolunas):
    for linhas in range (nlinhas):
        for colunas in range (ncolunas):
            print(matrix[linhas][coluna], end = '\t')
        print()

def main():
    tamanho = 2
    matriz[0] * tamanho
    for i in range (tamanho):
        matriz[i] = [0] * tamanho
    print('Digite o indice A da matriz')
    matriz[0][0] = int(input()) 
    print('Digite o indice B da matriz')
    matriz[0][1] = int(input())
    print('Digite o indice C da matriz')
    matriz[1][0] = int(input())
    print('Digite o indice D da matriz')
    matri[1][1] = int(input())
    imprimeMatriz(matriz, tamanho, tamanho)
    print('Agora vamos inverter sua matriz')
    matriz = inverterMatriz(matriz)
    if matriz is None:
        print('O determinante da matriz que voce inseriu deu 0')
    else:
        print('Sua matriz invertida')
        imprimeMatriz(matriz, tamanho, tamanho)

main()
























                  
