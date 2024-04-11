import pandas as pd
from carros import Carros

carros = Carros()

lista = carros.getCarsInStock()

if len(lista) != 0:
    df = pd.DataFrame(lista)
    print(df)

    df.to_csv('./dados.csv', encoding='utf-8')
else:
    print("Lista vazia. ")






