import sys
import os
root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(root_dir)
from teste.coleta_article import construir_url_article

def main():
    url = 'https://www.gov.br/saude/pt-br/assuntos/noticias?b_start:int='
    construir_url_article(url, 120, 20)

if __name__ == "__main__":
    main() 