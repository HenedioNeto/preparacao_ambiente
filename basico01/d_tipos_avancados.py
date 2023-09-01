"""
A lista é caracterizada pelos []
Os itens podem ser acessados por seu index
Pode ser mutável
"""

def main():
    inserir = "Brasil"
    #lista(a = "Argentina") #define um dos parametros (a) da função como Argentina 
    
def lista(a, b = "Brasil"): #define um dos parametros (b) da função como Brasil
    lista = ["Uruguai", "Paraguai", "Chile"] #criação da lista
    print(lista)
    lista.append(a) #adicionando o parametro (a) a lista
    lista.append(b) #adicionando o parametro (b) a lista
    print(lista)
    lista.append("Colombia") #adiciona Colombia a lista
    print(lista)
    print(type(lista)) #retorna o tipo da variavel lista
    print(len(lista)) #retorna o tamanho da lista (quantidades de elementos dentro dela)
    print(lista[0]) #retorna o indice 0 (primeiro elemento) da lista
    print(len(lista[0])) #retorna o tamanho do primeiro elemento (quantidade de caracteres)
    nova_lista = ["Equador"] #criação de uma segunda variavel em formato lista
    print(nova_lista)
    lista.extend(nova_lista) #adição da nova_lista na lista
    print(lista)
    lista.insert(3, "Guiana") #insere um item na lista (recebe uma posição seguida de virgula e o item)
    print(lista)
    lista.remove("Paraguai") #remove o item da lista
    print(lista)
    lista.pop() #remove o ultimo item da lista
    lista.pop(3) #remove o item pelo indice (no caso [3])
    print(lista)
    outra_lista = ['Uruguai', 'Paraguai', 'Chile', 'Guiana', 'Argentina', 'Brasil', 'Colombia', 'Equador']
    del outra_lista[4:7] #remove da lista os itens que vão do indice 4 ao 7(-1)
    print(outra_lista)
    outra_lista.clear() #remove todos os elementos da lista
    print(outra_lista)
    lista.append("Brasil")
    print(lista.count("Brasil")) #quantas vezes o item aparece na lista
    lista_copia = lista.copy() #copia a lista original
    print(lista_copia)
    lista.sort() #coloca a lista em ordem alfabetica e altera os indices
    print(lista)
    print(lista[0])
    print(sorted(lista_copia)) #ordena a lista sem alterar os indices
    print(lista_copia[0])
    lista.reverse() #inverte a ordem da lista
    print(lista)
    print(lista_copia)
    lista_copia[0] = "Paraguai" #altera o item que se encontra no indice indicado pelo item indicado
    print(lista_copia)
    print("Paraguai" in lista_copia) #retorna o boleano se o item for encontrado na lista

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
    conjunto = {"Brasil", "Argentina", "Colombia", "Equador", "Paraguai", "Uruguai", "Peru", "Chile"}
    print(conjunto)
    print(type(conjunto))
    print("Brasil" in conjunto) #boleano se há o item indicado
    conjunto.add("Venezuela") #adiciona um item
    print(conjunto)
    novo_conjunto = {"Guiana", "Suriname", "Brasil", "Guiana Francesa"}
    novo_conjunto.intersection_update(conjunto) #altera o novo_conjunto para o item que tem em comum com conjunto
    print(novo_conjunto)
    inter_conjunto = conjunto.intersection(novo_conjunto) #retorna um conjunto apenas com os elementos iguais dos conjuntos interseccionados
    print(inter_conjunto)
    conjunto.update(novo_conjunto) #adiciona o novo_conjunto ao conjunto (apenas elemento diferentes)
    print(conjunto)
    conjunto.remove("Argentina") #remove item
    print(conjunto)
    conjunto.discard("Brasil") #remove um item, caso não tenha esse item retorna none
    print(conjunto)
    print(conjunto.pop()) #remove um item e retorna o elemento (não recebe argumento)
    print(conjunto)
    conjunto_copia = conjunto.copy() #copia o conjunto
    print(conjunto_copia)
    conjunto_copia.clear() #limpa o conjunto
    print(conjunto_copia)
    print(conjunto)
    print(conjunto.difference(novo_conjunto)) #retorna os elementos que um set tem diferente do outro
    print(conjunto.isdisjoint(novo_conjunto)) #retorna um boleano (True se não houver elementos em comum entre os conjuntos)
    print(conjunto.issubset(novo_conjunto)) #retorna True se o subconjunto estiver dentro do conjunto
    print(conjunto.issuperset(novo_conjunto)) #retorna True se o conjunto for for um superconjunto de conjunto_copia
    print(conjunto.symmetric_difference(novo_conjunto)) #retorna os elementos que não estão na intersecção dos conjuntos
    print(conjunto.symmetric_difference_update(novo_conjunto)) #atualiza o conjunto com os elementos que não fazem parte da intersecção
    print(conjunto.union(novo_conjunto)) #retorna um conjunto com os elementos unicos dos conjuntos relacionados na união
    conjunto.update() #adiciona ao conjunto metodos iteraveis (aparentemente apenas um caracter)
    print(conjunto)

"""
Dicionarios são caracterizados por {}, alem das {} dicionarios também possua chave e valor
É possivel adicionar e remover itens
Os itens são acessados por suas chaves, não tem indice em dicionarios
"""

def dicionarios():
    dicionario = {
        "pais": "Brasil",
        "continente": "América",
        "capital": "Brasilia"
    }
    print(dicionario)
    print(type(dicionario))
    print(dicionario["pais"])
    print("pais" in dicionario)
    dicionario.update() #incrementa o dicionario com um outro dicionario(apenas itens diferentes)
    print(dicionario.values()) #retorna os valores do dicionario
    print(dicionario.pop("capital")) #remove e retorna o elemento com a chave fornecida
    print(dicionario)
    dicionario.setdefault("capital") #adiciona uma chave ao dicionario: com o valor none
    print(dicionario)
    print(dicionario.setdefault("pais")) #retorna o valor da chave no dicionario
    print(dicionario.popitem()) #remove e retorna o ultimo par adicionado no dicionario
    print(dicionario.keys()) #retorna as chavesdo dicionario
    print(dicionario.items()) #retorna os pares de chave e valor do dicionario como elementos de tupla
    print(dicionario.get("pais")) #retorna o valor da chave especificada
    #dicionario.fromkeys() #cria um novo dicionário a partir da sequência de elementos fornecidos
    novo_dicionario = dicionario.copy() #cria uma copia do dicionario, podendo modifica-lo sem modificar o original
    novo_dicionario.clear() #limpa o dicionario
    print(novo_dicionario)
    print(dicionario)

if __name__ == "__main__":
    main()
    #tuplas()
    #conjuntos()
    #dicionarios()