def main():
    loop_for()

def loop_for():
    paises = ["Brasil", "China", "Portugal", "Egito", "Australia"]
    locais = ["America do Sul", "Asia", "Europa", "Africa", "Oceania"]
    capitais = ["Brasilia", "Pequim", "Lisboa", "Cairo", "Camberra"]    
    print(paises)
    print(locais)
    print(capitais)
    for pais, local, capital in zip(paises, locais, capitais):
        #print(f"O nome deste pais é {pais}, localizado no continente {local} e com a capital {capital}")
        if pais == "Brasil":
            print(f"O nome deste pais é {pais}, localizado no continente {local} e com a capital {capital}")
        elif pais == "China":
            print(f"O pais {pais} tem como presidente o Xi Jinping")
        if pais == "Portugal":
            print(f"O nome deste pais é {pais}, localizado no continente {local} e com a capital {capital}")
        elif pais == "Egito":
            print(f"O pais {pais} tem as famosas Piramides")

if __name__ == "__main__":
    main()