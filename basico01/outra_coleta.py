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
    links_notas_de_imprensa = 'https://www.gov.br/turismo/pt-br/assuntos/noticias?b_start:int='
    contador = 120
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
            teste = acessar_pagina(link)
            tag = teste.find('p', attrs = {'property':'rnews:alternativeHeadline'})
            tag = tag.text.strip()
            print(tag)
            categoria = teste.find('div', attrs = {'class':'contenttree-widget relationchoice-field'})
            categoria = categoria.text.strip()
            print(categoria)
            atualizacao = teste.find('span', attrs = {'class':'documentModified'})
            if atualizacao != None:
                atualizacao = atualizacao.text.strip()
                atualizacao = re.findall(r'(\d{2}/\d{2}/\d{4} \d{2}h\d{2})', atualizacao)
                print(atualizacao)
            lista_data = teste.find_all('span', attrs = {'class':'value'})
            data_horario = lista_data[0].text.strip()
            data = re.findall(r'\d{2}/\d{2}/\d{4}', data_horario)
            horario = re.findall(r'\d{2}h\d{2}', data_horario)
            materia = teste.find('div', attrs = {'property':'rnews:articleBody'})
            lista_paragrafo = materia.find_all('p')
            lista_texto_paragrafo = []
            for paragrafo in lista_paragrafo:
                texto_paragrafo = paragrafo.text.strip()
                lista_texto_paragrafo.append(texto_paragrafo)
            print(titulo)
            print(link)
            print(data)
            print(horario)
            print(lista_texto_paragrafo)
            print('-' * 50)
        
def main():
    construir_url()
    
if __name__ == "__main__":
    main()