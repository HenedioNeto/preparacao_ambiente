import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query

def construir_url():
    links_notas_de_imprensa = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    contador = 90
    while contador >= 0:
        url_completa = links_notas_de_imprensa + str(contador)
        contador = contador - 30
        print(url_completa)

def url_teste():
    contador = 0
    while contador <= 90:
        link_teste = f"https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int={contador}"
        contador += 30
        print(link_teste)

def main():
    #construir_url()
    url_teste()

if __name__ == "__main__":
    main()