import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
import re

def acessar_pagina(url):
    pagina = requests.get(url)
    bs = BeautifulSoup(pagina.text, "html.parser")
    return bs

def construir_url():
    list_url = []
    links_notas_de_imprensa = 'https://www.gov.br/mda/pt-br/noticias?b_start:int='
    contador = 60
    while contador >= 0:
        url_completa = links_notas_de_imprensa + str(contador)
        contador = contador - 20
        list_url.append(url_completa)
    extrair_infos(list_url)

def extrair_infos(lista_urls):
    lista_de_links = lista_urls
    for link_geral in lista_de_links:
        html = acessar_pagina(link_geral)
        conteudo = html.find('ul', attrs = {'class':'noticias listagem-noticias-com-foto'})
        lista_nota_imprensa = conteudo.find_all('li')
        for nota_imprensa in lista_nota_imprensa:
            titulo = nota_imprensa.h2.text.strip()
            link = nota_imprensa.a['href'].strip()
            acesso_link = acessar_pagina(link)
            tag = acesso_link.find('p', attrs = {'property':'rnews:alternativeHeadline'})
            tag = tag.text.strip()
            atualizacao = acesso_link.find('span', attrs = {'class':'documentModified'})
            if atualizacao != None:
                atualizacao = atualizacao.text.strip()
                atualizacao = re.findall(r'(\d{2}/\d{2}/\d{4} \d{2}h\d{2})', atualizacao)
            lista_data = acesso_link.find_all('span', attrs = {'class':'documentPublished'})
            data_horario = lista_data[0].text.strip()
            data = re.findall(r'\d{2}/\d{2}/\d{4}', data_horario)
            horario = re.findall(r'\d{2}h\d{2}', data_horario)
            materia = acesso_link.find('div', attrs = {'property':'rnews:articleBody'})
            lista_paragrafo = materia.find_all('p')
            lista_texto_paragrafo = []
            for paragrafo in lista_paragrafo:
                texto_paragrafo = paragrafo.text.strip()
                lista_texto_paragrafo.append(texto_paragrafo)
            print(titulo)
            #print(link)
            #print(tag)
            #print(atualizacao)
            #print(data)
            #print(horario)
            #print(lista_texto_paragrafo)

def main():
    construir_url()

if __name__ == "__main__":
    main() 