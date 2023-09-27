import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
import re 

def acessar_pagina(url):
    pagina = requests.get(url)
    bs = BeautifulSoup(pagina.text, "html.parser")
    return bs

def construir_url(url_principal, num_contador, decremento):
    list_url = []
    links_notas_de_imprensa = url_principal
    contador = num_contador
    while contador >= 0:
        url_completa = links_notas_de_imprensa + str(contador)
        contador = contador - decremento
        list_url.append(url_completa)
    extrair_infos(list_url)

def extrair_infos(lista_urls):
    lista_de_links = lista_urls
    for link_geral in lista_de_links:
        html = acessar_pagina(link_geral)
        conteudo = html.find('div', attrs = {'id':'content-core'})
        lista_nota_imprensa = conteudo.find_all('article')
        for nota_imprensa in lista_nota_imprensa:
            titulo = nota_imprensa.h2.text.strip()
            link = nota_imprensa.a['href']           
            numero = nota_imprensa.span.text
            numero = re.findall(r'\d+', numero)
            lista_data = nota_imprensa.find_all('span', attrs = {'class':'summary-view-icon'})
            data = lista_data[0].text.strip()
            horario = lista_data[1].text.strip()
            teste = acessar_pagina(link)
            materia = teste.find('div', attrs = {'property':'rnews:articleBody'})
            lista_paragrafo = materia.find_all('p')
            lista_texto_paragrafo = []
            for paragrafo in lista_paragrafo:
                texto_paragrafo = paragrafo.text
                lista_texto_paragrafo.append(texto_paragrafo)
                print(titulo)
                print(link)
                #print(numero)
                #print(data)
                #print(horario)
                #print(lista_texto_paragrafo)
                #print('-' * 50)
            #criar_db(titulo, link, numero, data, horario, lista_texto_paragrafo) 
"""
def criar_db(titulo, link, numero, data, horario, lista_texto_paragrafo):
    db = TinyDB('db.json', indent=4, ensure_ascii = False)
    db.insert({
        'Titulo da materia': titulo,
        'Link da materia': link,
        'Numero da nota de imprensa': numero,
        'Data da materia': data,
        'Horario da materia': horario,
        'Conteudo da materia': lista_texto_paragrafo,
    })
"""
def main():
    construir_url('https://www.gov.br/turismo/pt-br/assuntos/noticias?b_start:int=', 120, 20)
    
    
    
if __name__ == "__main__":
    main()