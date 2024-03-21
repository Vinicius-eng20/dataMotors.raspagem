from requests import get
import json, math
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
        'Preço (R$)': (objeto['Prices']['Price']) / 10,
        'Cor': objeto['Specification']['Color']['Primary'],
        'Transmissão': objeto['Specification']['Transmission'],
        'Numero de Portas': objeto['Specification']['NumberPorts'],
        'Quilometragem': (objeto['Specification']['Odometer']) / 10,
        'Cidade': objeto['Seller']['City'],
        'Estado': objeto['Seller']['State'],
        'AnoFab': objeto['Specification']['YearFabrication'],
        'AnoModelo': int(objeto['Specification']['YearModel']),
        #'Vendedor': objeto['Seller']['FantasyName'],
        'Data': date.today().strftime("%d/%m/%Y")
    }

class Carros:
    def getMegaFeirao(self):
        data = {
            #'url': 'https://www.webmotors.com.br/ofertas/feiroes/megafeirao/carros/estoque?feirao=Mega Feirão',
            #'feirao': 'Mega Feirão',
            'url': 'https://www.webmotors.com.br/carros/estoque',
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
                'url': 'https://www.webmotors.com.br/ofertas/feiroes/megafeirao/carros/estoque?feirao=Mega Feirão',
                'feirao': 'Mega Feirão',
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

            dados = json.loads(response.text)

            print(f"Page {j}")

            for i in range(0, 24):
                produto = dados['SearchResults'][i]
                lista_carros.append(json_carro(produto))

        return lista_carros
    
    def getMarca(self, marca):
        if marca == '': 
            return [] 

        data = {
            'url': f'https://www.webmotors.com.br/carros/estoque/{marca.lower()}?estadocidade=estoque&marca1={marca.upper()}&autocomplete={marca.lower()}&autocompleteTerm={marca.upper()}&lkid=1704',
            #'url': f'https://www.webmotors.com.br/api/search/car?actualPage=1&brand={marca}',
            'actualPage': 1,
            'displayPerPage': 24,
            'order': 1,
            'showMenu': True,
            'showCount': True,
            'showBreadCrumb': True,
            'testAB': False,
            'returnUrl': False
        }
        try:
            response = get(api, headers=headers, params=data)
            response.raise_for_status()
            qtde_items = json.loads(response.text)
            qtde_produtos = qtde_items['Count']
            print(qtde_produtos)

            for j in range(1, 20):
                data = {
                    'url': f'https://www.webmotors.com.br/carros/estoque/{marca.lower()}?estadocidade=estoque&marca1={marca.upper()}&autocomplete={marca.lower()}&autocompleteTerm={marca.upper()}&lkid=1704',
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

                dados = json.loads(response.text)

                print(f"Page {j}")

                for i in range(0, 24):
                    produto = dados['SearchResults'][i]
                    lista_carros.append(json_carro(produto))

            return lista_carros
        except Exception as e:
            print(f"Erro: {e}")

    def getModelo(self, marca, modelo):
        if marca == '' or modelo == '':
            return []
        
        data = {
            'url': f'https://www.webmotors.com.br/carros/estoque/{marca.lower()}/{modelo.lower()}?lkid=1022&estadocidade=estoque&marca1={marca.upper()}&modelo1={modelo.upper()}&autocomplete={marca.lower()}%20{modelo.lower()}&autocompleteTerm={marca.upper()}%20{modelo.upper()}',
            'actualPage': 1,
            'displayPerPage': 24,
            'order': 1,
            'showMenu': True,
            'showCount': True,
            'showBreadCrumb': True,
            'testAB': False,
            'returnUrl': False
        }
        try:
            response = get(api, headers=headers, params=data)
            response.raise_for_status()
            qtde_items = json.loads(response.text)
            qtde_produtos = qtde_items['Count']
            print(qtde_produtos)

            #for j in range(1, math.ceil(qtde_produtos/24)):
            for j in range(1, 20):
                data = {
                    'url': f'https://www.webmotors.com.br/carros/estoque/{marca.lower()}/{modelo.lower()}?lkid=1022&estadocidade=estoque&marca1={marca.upper()}&modelo1={modelo.upper()}&autocomplete={marca.lower()}%20{modelo.lower()}&autocompleteTerm={marca.upper()}%20{modelo.upper()}',
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

                dados = json.loads(response.text)

                print(f"Page {j}")

                for i in range(0, 24):
                    produto = dados['SearchResults'][i]
                    lista_carros.append(json_carro(produto))

            return lista_carros

        except Exception as e:
            print(f'Erro: {e}')





