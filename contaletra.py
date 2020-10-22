#Definindo número de casos
nCasos = int(input("Número de casos: "))

#Criando listas auxiliares para armazenar as palavras e filtros.
listaPalavras = []
listaFiltros = []


#Recebendo os inputs de palavras + filtros separados por espaćos, usamos 
#a funcao .split() para separar os filtros e palavras.

for i in range(0,nCasos):
    entradaString = str(input("Palavra e letra a ser testada: "))
    palavra, filtro = entradaString.split()
    listaFiltros.append(filtro)
    listaPalavras.append(palavra)
    



#funcao para contar cada letra presente em uma palavra.
def contaLetra(palavra):
    dict = {}
    for i in palavra:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

# Uso a funcao map para me auxiliar.
# a funcao map recebe uma funcao como parametro e n parametros iteráveis
# e passa cada elemento do iterável como argumento da funćão passada no map
# nesse caso, passa cada palavra como argumento para a funcao contaLetra.
# É como um for, mas diferente.

resultado = map(contaLetra, listaPalavras)

#organizando a casa para printar
listaResultado = list(resultado)


print(listaResultado)


#checando os filtros nas palavras
for i in range(nCasos):
    checaFiltro = listaPalavras[i].count(listaFiltros[i])
    if checaFiltro == 0:
        print("Consulta inválida")
    else:
        print(listaFiltros[i]+":"+str(checaFiltro))


