import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyBZFny6JOecPZm0BLk63zeCPnfnApdbxSw')

origem = pd.read_excel('sao-paulo-metro/Book7.xlsx')

ArraydeDuração = []
ArraydeNomes = []
ArraydeDistancia = []

def CalculoDeDistanciasAtéMetro(Origem):
    for index, l_origem in origem.iterrows():
        consulta = gmaps.distance_matrix('Metro' + l_origem['name'] + ', São Paulo', Origem)
        Distancia = consulta['rows'][0]['elements'][0]['distance']['value']
        Duracao = consulta['rows'][0]['elements'][0]['duration']['value']
        ArraydeDistancia.append(Distancia)
        ArraydeDuração.append(Duracao)
        ArraydeNomes.append(l_origem['name'])

    MenorDistancia = ArraydeDistancia.index(min(ArraydeDistancia))
    menorDuração = ArraydeDuração.index(min(ArraydeDuração))

    print(ArraydeNomes[menorDuração])
    print(ArraydeNomes[MenorDistancia])






    # print(Duracao)
    # print(Distancia)
    # print('Metro ' + l_origem['name'] + ': \n    Duração: ' + Duracao + '\n    Distancia: ' + Distancia)

