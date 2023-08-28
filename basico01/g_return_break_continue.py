import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query

def acessar_pagina(url):
    pagina = requests.get(url)
    bs = BeautifulSoup(pagina.text, "html.parser")
    #print(bs)
    return bs

def construir_url():
    list_url = []
    links_notas_de_imprensa = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    contador = 90
    while contador >= 0:
        url_completa = links_notas_de_imprensa + str(contador)
        if contador == 0:
            url_completa = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa"
        contador = contador - 30
        list_url.append(url_completa)
    return list_url

print(construir_url())

def main():
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa"
    #pagina_web = acessar_pagina(url)
    construir_url()
    

if __name__ == "__main__":
    main()
