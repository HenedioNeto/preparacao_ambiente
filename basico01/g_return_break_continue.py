#Return finaliza a função e retorna um valor indicado para sua chamada
#Break é utilizado em loops, quando a condição que chama o break é encontrada o loop encerra
#Continue é utilizado em loops, quando sua condição é encontrada o loop interrompe a interação atual
#e continua na próxima iteração
import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query

def acessar_pagina(url):
    pagina = requests.get(url)
    bs = BeautifulSoup(pagina.text, "html.parser")
    #print(bs)
    return bs

#TODO armazenar url em uma lista
#TODO deixar a lista acessivel para uma função "extrair_infos" (a ser criada)
#TODO acessar pagina atraves da função "acessar_pagina"
#TODO printar os nomes de todos os titulos das 3 primeiras paginas das notas de imprensa

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
#print(construir_url())

def extrair_infos():
    lista_de_links = construir_url()
    for link_geral in lista_de_links:
        html = acessar_pagina(link_geral)
        conteudo = html.find('div', attrs = {'id':'content-core'})
        lista_nota_imprensa = conteudo.find_all('article')
        for nota_imprensa in lista_nota_imprensa:
            titulo = nota_imprensa.h2.text.strip()
            link = nota_imprensa.a['href']
            numero = nota_imprensa.span.text
            lista_data = nota_imprensa.find_all('span', attrs = {'class':'summary-view-icon'})
            data = lista_data[0].text.strip()
            horario = lista_data[1].text.strip()
            print(titulo)
            print(link)
            print(numero)
            print(data)
            print(horario)
            print('###')
        #<div id="content-core">

def main():
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa"
    #pagina_web = acessar_pagina(url)
    #construir_url()
    extrair_infos()
    

if __name__ == "__main__":
    main()
