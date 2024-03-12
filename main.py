from requests import get
import json

marca = 'Porsche'

url = 'https://www.webmotors.com.br/api/search/car?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
}

for i in range(0, 11):
    data = {
        #'url': 'https://www.webmotors.com.br/ofertas/feiroes/megafeirao/carros/estoque?feirao=Mega Feirão',
        #'feirao': 'Mega Feirão',
        'url': f'https://www.webmotors.com.br/carros/estoque/{marca.lower()}?estadocidade=estoque&marca1={marca.upper()}&autocomplete={marca.lower()}&autocompleteTerm={marca.upper()}&lkid=1704',
        'actualPage': i,
        'displayPerPage': 24,
        'order': 1,
        'showMenu': True,
        'showCount': True,
        'showBreadCrumb': True,
        'testAB': False,
        'returnUrl': False
    }

    response = get(url, headers=headers, params=data)

    dados = json.loads(response.text)

    for j in range(0, 24):
        produto = dados['SearchResults'][j]
        titulo = produto['Specification']['Title']
        preco = produto['Prices']['Price']
        print(f"{i+1}. {titulo}: R$ {preco:.2f}")


