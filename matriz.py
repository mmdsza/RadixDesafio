import numpy as np

tamanho = int(input("Tamanho da matriz: "))

#matriz = np.zeros((tamanho, tamanho), int)
def squarematrix(tamanho):
    
    #cria a matriz e preenche com zeros
    matriz = np.zeros((tamanho, tamanho), int)
    
    #preenche a diagonal com "1"
    np.fill_diagonal(matriz, 1)

    #formata e printa o resultado
    print("Matrix({}x{})\n".format(tamanho,tamanho))
    print(matriz)


squarematrix(tamanho)