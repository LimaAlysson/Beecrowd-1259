

#Criando 4 listas para manipular os valores
lista = []
lista_par = []
lista_impar = []
lista_ordenada = []

#Pedindo o n�mero de entradas a serem informadas
num_entradas = int(input())

#Criando um for que percorre o tamanho do n�mero de
#entradas recebido anteriormente
for i in range (num_entradas):
    #Recebendo dentro do for as entradas de acordo com o n�mero de entradas
    #informado anteriormente
    entrada = int(input())
    #Adicionando essas entradas informadas em uma lista 
    lista.append(entrada)

#Usando o m�todo sort para ordenar a lista de forma crescente
lista.sort()

#Usando um for no tamanho da lista
for j in range (len(lista)):
    #Verificando os itens da lista que s�o par
    if (lista[j] % 2 == 0):
        #Adicionando os itens pares numa lista apenas de n�meros pares
        lista_par.append(lista[j])
    else:
        #Fazendo o contrario e adicionando em outra lista apenas os n�meros impares
        lista_impar.append(lista[j])

#Atribuindo o valor da lista de n�meros �mpares � ela mesma s� que
#na ordem do maior para o menor(invertendo a lista)
lista_impar = lista_impar[::-1]
#Atribuindo os itens das listas pares e impares a uma lista final ordenada
#para o resultado final
lista_ordenada = lista_par + lista_impar

#usando um for para "printar" o resultado final, a lista ordenada.
for k in (lista_ordenada):
    print(k)
    
        
