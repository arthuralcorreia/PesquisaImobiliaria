import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='')

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
    def values():
        global IndexMenorDistancia
        IndexMenorDistancia = ArraydeDistancia.index(min(ArraydeDistancia))
        global IndexArraymenorDuração
        IndexArraymenorDuração = ArraydeDuração.index(min(ArraydeDuração))
        global MetroMaisProximo
        MetroMaisProximo = ArraydeNomes[IndexArraymenorDuração]
        global MetroMaisRapido
        MetroMaisRapido = ArraydeNomes[IndexMenorDistancia]
        global DistanciaMetro
        DistanciaMetro = ArraydeDistancia[IndexMenorDistancia]
        global MetroRapido
        MetroRapido = ArraydeDistancia[IndexArraymenorDuração]
        
    values()
        
    ArraydeDuração.clear()
    ArraydeNomes.clear()
    ArraydeDistancia.clear()
    





    # print(Duracao)
    # print(Distancia)
    # print('Metro ' + l_origem['name'] + ': \n    Duração: ' + Duracao + '\n    Distancia: ' + Distancia)

