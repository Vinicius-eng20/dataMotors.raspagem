import pandas as pd
from carros import Carros
# from db import connect_postgres

# marca = 'Hyundai'
# modelo = 'HB20'

carros = Carros()
# lista = carros.getModelo(marca, modelo)
lista = carros.getMegaFeirao()

if len(lista) != 0:
    df = pd.DataFrame(lista)
    print(df)

    # connect_postgres(lista)

    df.to_csv('./dados.csv', encoding='utf-8')
else:
    print("Lista vazia. ")






