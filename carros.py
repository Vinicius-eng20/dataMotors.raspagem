from requests import get
import json
from time import sleep
from datetime import date

api = 'https://www.webmotors.com.br/api/search/car?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
    'Referer': 'https://www.webmotors.com.br/',
    'Accept': 'application/json, text/plain, */*',
}
lista_carros = []

def json_carro(objeto):
    return {
        'Marca': objeto['Specification']['Make']['Value'],
        'Modelo': objeto['Specification']['Model']['Value'],
        'Versão': objeto['Specification']['Version']['Value'],
        "Tipo": objeto['ListingType'],
        'Preço (R$)': str(objeto['Prices']['Price']).replace('.',','),
        'Cor': objeto['Specification']['Color']['Primary'],
        'Transmissão': objeto['Specification']['Transmission'],
        'Numero de Portas': objeto['Specification']['NumberPorts'],
        'Quilometragem': str(objeto['Specification']['Odometer']).replace('.', ','),
        'Cidade': objeto['Seller']['City'],
        'Estado': objeto['Seller']['State'],
        'AnoFab': objeto['Specification']['YearFabrication'],
        'AnoModelo': int(objeto['Specification']['YearModel']),
        #'Vendedor': objeto['Seller']['FantasyName'],
        'Data': date.today().strftime("%d/%m/%Y")
    }

class Carros:
    def getCarsInStock(self):
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
        response = get(api, headers=headers, params=data)
        response.raise_for_status()
        qtde_items = json.loads(response.text)
        qtde_produtos = qtde_items['Count']
        print(qtde_produtos)

        for j in range(1, 20):
            data = {
                #'url': 'https://www.webmotors.com.br/ofertas/feiroes/megafeirao/carros/estoque?feirao=Mega Feirão',
                #'feirao': 'Mega Feirão',
                'url': 'https://www.webmotors.com.br/carros/estoque?lkid=1022',
                'actualPage': j,
                'displayPerPage': 24,
                'order': 1,
                'showMenu': True,
                'showCount': True,
                'showBreadCrumb': True,
                'testAB': False,
                'returnUrl': False
            }
            response = get(api, headers=headers, params=data)

            print(response)
            print(f"Page {j}")

            if response.status_code != 200:
                print("Próximo...")
                continue

            dados = json.loads(response.text)

            for i in range(0, 24):
                produto = dados['SearchResults'][i]
                lista_carros.append(json_carro(produto))

            sleep(.5)

        return lista_carros





