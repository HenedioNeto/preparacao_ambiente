from func_coleta import construir_url_li

def main():
    url = 'https://www.gov.br/turismo/pt-br/assuntos/noticias?b_start:int='
    construir_url_li(url, 120, 20)

if __name__ == "__main__":
    main() 