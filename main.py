import pandas as pd
from carros import Carros

# marca = 'Audi'
# modelo = 'A6'

carros = Carros()
# lista = carros.getModelo(marca, modelo)
lista = carros.getMegaFeirao()

if len(lista) != 0:
    df = pd.DataFrame(lista)
    print(df)

    df.to_csv('./dados.csv', encoding='utf-8')
else:
    print("Lista vazia.")




