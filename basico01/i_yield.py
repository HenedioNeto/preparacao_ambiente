#O yield é eficiente quando precisamos trabalhar com grandes quantidades de dados
#O yield é uma palavra chave do python para criar geradores
"""
Esses geradores são formas de criar sequencias de valores de forma eficiente sem precisar armazenar
esses valores em uma memória. Esses valores são gerados via demanda, economizando uso de memória
"""

#Para utilizar o yield:

#1. Definimos uma função iteradora trocando o return por yield
#2. Ao encontrar o yield a função retornara o valor especificado pelo yield
#3. Caso chamada novamente a função retornara o valor subsequente
#4. Ao ser novamente chamada a função retornara sua execução de onde parou, permitindo que ela gere
# valores em sequencia

def num_par(maximo):
    i = 0
    while i < maximo:
        yield i
        i += 2

#A função acima retorna os numeros pares de 0 ao valor maximo pedido
#Quando chamada por um loop a função retornara um numero par a cada chamada

gerador = num_par(10)

for numero in gerador:
    print(numero)

#Esse codigo trará os numeros pares de 0 a 10, um de cada vez, sem armazena-los na memoria


