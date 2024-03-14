import pandas as pd
from carros import Carros

marca = 'Hyundai'
modelo = 'HB20'

carros = Carros()
lista = carros.getModelo(marca, modelo)

df = pd.DataFrame(lista)
print(df)

df.to_csv('./dados.csv', encoding='utf-8')




