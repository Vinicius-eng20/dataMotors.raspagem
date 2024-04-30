from requests import get, post
import json
from time import sleep, time
from datetime import date
from fake_useragent import UserAgent
import concurrent.futures

ua = UserAgent()

api = 'https://www.webmotors.com.br/api/search/car?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
    #'User-Agent': ua.random,
    'Referer': 'https://www.webmotors.com.br/',
    'Accept': 'application/json, text/plain, */*',
}
lista_carros = []

def json_carro(objeto):
    return {
        'marca': objeto['Specification']['Make']['Value'],
        'modelo': objeto['Specification']['Model']['Value'],
        'versao': objeto['Specification']['Version']['Value'],
        "tipo": objeto['ListingType'],
        'preco': objeto['Prices']['Price'],
        'cor': objeto['Specification']['Color']['Primary'],
        'transmissao': objeto['Specification']['Transmission'],
        'numPortas': objeto['Specification']['NumberPorts'],
        'carroceria': objeto['Specification']['BodyType'],
        'blindado': objeto['Specification']['Armored'],
        'quilometragem': objeto['Specification']['Odometer'],
        'cidade': objeto['Seller']['City'],
        'estado': objeto['Seller']['State'],
        'anoFab': int(objeto['Specification']['YearFabrication']),
        'anoModelo': int(objeto['Specification']['YearModel']),
        #'Vendedor': objeto['Seller']['FantasyName'],
        'data': date.today().strftime("%d/%m/%Y")
    }

def insert_API(url, json):
    response = post(url, json=json)
    return response

data = {
    #'url': 'https://www.webmotors.com.br/ofertas/feiroes/megafeirao/carros/estoque?feirao=Mega Feirão',
    #'feirao': 'Mega Feirão',
    'url': 'https://www.webmotors.com.br/carros/estoque?lkid=1022',
    'actualPage': 1,
    'displayPerPage': 24,
    'order': 1,
    'showMenu': True,
    'showCount': True,
    'showBreadCrumb': True,
    'testAB': False,
    'returnUrl': False
}

class Carros:
    def getCarsInStock(self):
        
        response = get(api, headers=headers, params=data)
        response.raise_for_status()
        qtde_items = json.loads(response.text)
        qtde_produtos = qtde_items['Count']
        print(qtde_produtos)

        def paginacao(page):
            data['actualPage'] = page
            response = get(api, headers=headers, params=data)

            print(f"Page {page}: {response}")

            if response.status_code != 200:
                print("Próximo...")
                sleep(1)
                return

            dados = json.loads(response.text)
            carros = []
            for i in range(0, 24):
                produto = dados['SearchResults'][i]
                lista_carros.append(json_carro(produto))
                insert_API("http://localhost:8080/carros", json=json_carro(produto))
                carros.append(json_carro(produto))
            
            sleep(1)

            return carros
            
        # Número total de páginas
        total_pages = 300

        # Número máximo de threads simultâneas
        max_workers = 3

        # Lista para armazenar os resultados da raspagem
        results = []

        # Função para processar as páginas em paralelo
        def process_pages():
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                # Mapeia a função scrape_page para cada página
                future_to_page = {executor.submit(paginacao, page): page for page in range(1, total_pages + 1)}
                # Coleta os resultados
                for future in concurrent.futures.as_completed(future_to_page):
                    page = future_to_page[future]
                    try:
                        result = future.result()
                        results.append(result)
                        sleep(.5)
                    except Exception as e:
                        print(f"Exceção ao processar página {page}: {e}")

        # Inicia o processamento das páginas
        start_time = time()
        process_pages()
        end_time = time()

        # Imprime os resultados
        print(f"Raspagem concluída em {end_time - start_time:.2f} segundos.")
        print(f"Total de registros coletados: {len(results)}")
        
        # for j in range(1, 50):
        #     lista_carros.append(paginacao(j))

        # return lista_carros





