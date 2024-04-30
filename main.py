# import pandas as pd
from carros import Carros

carros = Carros()

lista = carros.getCarsInStock()
print("Raspagem concluída.")


# if len(lista) != 0:
#     # df = pd.DataFrame(lista)
#     # print(df)
#     print("Preparando para enviar dados...")
#     # df.to_csv('./dados.csv', encoding='utf-8')
#     for item in lista:
#         response = post(url="http://localhost:8080/carros", json=item)
#         print(response)
# else:
#     print("Lista vazia. ")






