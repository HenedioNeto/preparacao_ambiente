"""
A lista é caracterizada pelos []
Os itens podem ser acessados por seu index
Pode ser mutável
"""

def main():
    inserir = "Brasil"
    #lista(a = "Argentina") #define um dos parametros (a) da função como Argentina 
    
def lista(a, b = "Brasil"): #define um dos parametros (b) da função como Brasil
    """Função para estudo de metodo de listas"""
    lista = ["Uruguai", "Paraguai", "Chile"] #criação da lista
    print(type(lista)) #retorna o tipo da variavel lista
    print(len(lista)) #retorna o tamanho da lista (quantidades de elementos dentro dela)

    """Metodos de adição e criação de listas"""
    lista.append(a) #adicionando o parametro (a) a lista
    lista.append(b) #adicionando o parametro (b) a lista
    lista.append("Colombia") #adiciona Colombia a lista
    nova_lista = ["Equador"] #criação de uma segunda variavel em formato lista
    lista.extend(nova_lista) #adição da nova_lista na lista
    lista.insert(3, "Guiana") #insere um item na lista (recebe uma posição seguida de virgula e o item)
    lista[0] = "Paraguai" #altera o item que se encontra no indice indicado pelo item indicado

    """Métodos de busca em listas"""
    print(lista[0]) #retorna o indice 0 (primeiro elemento) da lista
    print(len(lista[0])) #retorna o tamanho do primeiro elemento (quantidade de caracteres)
    print(lista.count("Brasil")) #quantas vezes o item aparece na lista
    print("Paraguai" in lista) #retorna um boleano sobre a presença do item na lista
    lista_copia = lista.copy() #copia a lista original

    """Métodos de remoção em listas"""
    lista.remove("Paraguai") #remove o item da lista
    lista.pop() #remove o ultimo item da lista
    lista.pop(3) #remove o item pelo indice (no caso [3])
    outra_lista = ['Uruguai', 'Paraguai', 'Chile', 'Guiana', 'Argentina', 'Brasil', 'Colombia', 'Equador']
    del outra_lista[4:7] #remove da lista os itens que vão do indice 4 ao 7(-1)
    outra_lista.clear() #remove todos os elementos da lista

    """Métodos de ordenação em listas"""
    lista.sort() #coloca a lista em ordem alfabetica e altera os indices
    print(sorted(lista_copia)) #ordena a lista sem alterar os indices
    lista.reverse() #inverte a ordem da lista

"""
Tuplas são caracterizadas por () com um item dentro SEGUIDO POR VIRGULA (,)
É possivel acessar itens por index
Não podem ser mutaveis, não é possivel adicionar ou excluir item, nem reordena-los
"""

def tuplas():
    """Função para estudo de metodo de tuplas"""
    tupla = ("Paraguai", "Brasil", "Equador", "Colombia", "Argentina", "Brasil")
    print(tupla)
    print(type(tupla)) #tipo da variavel
    print(tupla[0]) #indice 0 na variavel
    print("Paraguai" in tupla) #boleano do item na tupla
    print(tupla.count("Brasil")) #numero de vezes que o item se encontra na tupla
    print(tupla.index("Brasil")) #indice do item (primeira vez que ele aparece na tupla)
"""
O conjunto é caracterizado por {}
Armazena dados mutaveis, podendo adicionar e remover
Não pode ser acessado por indice e nem ordenados
A ordem dos itens alteram no print()
"""

def conjuntos():
    """Função para estudo de metodo de conjuntos"""
    conjunto = {"Brasil", "Argentina", "Colombia", "Equador", "Paraguai", "Uruguai", "Peru", "Chile"}
    print(conjunto)
    print(type(conjunto))

    """Métodos de adição e criação em conjuntos"""
    conjunto.add("Venezuela") #adiciona um item
    novo_conjunto = {"Guiana", "Suriname", "Brasil", "Guiana Francesa"}
    conjunto_copia = conjunto.copy() #copia o conjunto
    conjunto.update(novo_conjunto) #adiciona o novo_conjunto ao conjunto (apenas elemento diferentes)
    novo_conjunto.intersection_update(conjunto) #altera o novo_conjunto para o item que tem em comum com conjunto
    inter_conjunto = conjunto.intersection(novo_conjunto) #retorna um conjunto apenas com os elementos iguais dos conjuntos interseccionados
    print(conjunto.symmetric_difference_update(novo_conjunto)) #atualiza o conjunto com os elementos que não fazem parte da intersecção
    print(conjunto.union(novo_conjunto)) #retorna um conjunto com os elementos unicos dos conjuntos relacionados na união
    conjunto.update() #adiciona ao conjunto metodos iteraveis (aparentemente apenas um caracter)

    """Métodos de busca em conjuntos"""
    print("Brasil" in conjunto) #boleano se há o item indicado
    print(conjunto.isdisjoint(novo_conjunto)) #retorna um boleano (True se não houver elementos em comum entre os conjuntos)
    print(conjunto.difference(novo_conjunto)) #retorna os elementos que um set tem diferente do outro
    print(conjunto.issubset(novo_conjunto)) #retorna True se o subconjunto estiver dentro do conjunto
    print(conjunto.issuperset(novo_conjunto)) #retorna True se o conjunto for for um superconjunto de conjunto_copia
    print(conjunto.symmetric_difference(novo_conjunto)) #retorna os elementos que não estão na intersecção dos conjuntos

    """Métodos de remoção em conjuntos"""
    conjunto.remove("Argentina") #remove item
    conjunto.discard("Brasil") #remove um item, caso não tenha esse item retorna none
    print(conjunto.pop()) #remove um item e retorna o elemento (não recebe argumento)    
    conjunto_copia.clear() #limpa o conjunto
    

"""
Dicionarios são caracterizados por {}, alem das {} dicionarios também possua chave e valor
É possivel adicionar e remover itens
Os itens são acessados por suas chaves, não tem indice em dicionarios
"""

def dicionarios():
    """Função para estudo de metodo de dicionarios"""
    dicionario = {
        "pais": "Brasil",
        "continente": "América",
        "capital": "Brasilia"
    }
    print(dicionario)
    print(type(dicionario))

"""Métodos de adição e criação em dicionarios"""
    dicionario.update() #incrementa o dicionario com um outro dicionario(apenas itens diferentes)
    dicionario.setdefault("capital") #adiciona uma chave ao dicionario: com o valor none
    #dicionario.fromkeys() #cria um novo dicionário a partir da sequência de elementos fornecidos
    novo_dicionario = dicionario.copy() #cria uma copia do dicionario, podendo modifica-lo sem modificar o original

"""Métodos de busca em dicionario"""
    print(dicionario["pais"])
    print("pais" in dicionario)
    print(dicionario.values()) #retorna os valores do dicionario
    print(dicionario.setdefault("pais")) #retorna o valor da chave no dicionario
    print(dicionario.keys()) #retorna as chaves do dicionario
    print(dicionario.items()) #retorna os pares de chave e valor do dicionario como elementos de tupla
    print(dicionario.get("pais")) #retorna o valor da chave especificada

"""Métodos de remoção em dicionarios"""
    print(dicionario.pop("capital")) #remove e retorna o elemento com a chave fornecida
    print(dicionario.popitem()) #remove e retorna o ultimo par adicionado no dicionario
    novo_dicionario.clear() #limpa o dicionario

if __name__ == "__main__":
    main()
    #tuplas()
    #conjuntos()
    #dicionarios()