def main():
    inserir = "Brasil"
    #lista(a = "Argentina")
    
def lista(a, b = "Brasil"):
    lista = []
    print(b)
    print(lista)
    lista.append(a)
    lista.append(b)
    print(type(lista))
    print(lista)
    print(len(lista))
    print(len(lista[0]))
    print(lista[0])
    print(lista[1])
    lista.append("Uruguai")
    print(lista)

def conjuntos():
    conjunto = {"Brasil", "Argentina"}
    print(conjunto)
    print(type(conjunto))

def dicionarios():
    dicionario = {
        "pais": "Brasil",
        "continente": "América",
    }
    print(dicionario)
    print(type(dicionario))
    print(dicionario["pais"])
    print("pais" in dicionario)

if __name__ == "__main__":
    main()
    #conjuntos()
    dicionarios()