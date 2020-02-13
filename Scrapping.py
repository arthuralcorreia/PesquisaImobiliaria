import requests
from bs4 import BeautifulSoup
import APIGoogleMaps
import re
import csv

i = 1
M = 1
csv_file = open('ResultadosDaPesquisa.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Título','Link', 'Endereço', 'Especificações', 'Observações', 'Preço', 'Metrô mais próximo', 'Metrõ mais Rapido', 'Distancia', 'Duração'])

for j in range(1000):

    page = requests.get('https://www.imovelweb.com.br/apartamentos-venda-sao-paulo-sp-menos-400000-reales-pagina-'+ str(j) +'.html')
    html_soup = BeautifulSoup(page.text, 'html.parser')

    

    for ape_container in html_soup.find_all('div', class_ = 'posting-card super-highlighted'):


        Titulo = (ape_container.find('div', class_ = 'posting-heading').h2.text).lstrip().rstrip()
        url = (ape_container.find('a').get('href'))
        Endereco = (ape_container.find('div', class_ = 'posting-heading').span.text).lstrip().rstrip().strip()
        especificacoes = ape_container.find("ul", class_ = "main-features go-to-posting").text.lstrip().rstrip()
        observações = ape_container.find('div', class_ = 'posting-description go-to-posting').text.lstrip().rstrip()
        preco = ape_container.find("div", class_ = 'prices').text.lstrip().rstrip()
        publicacoes = ape_container.find("ul", class_ = "posting-features go-to-posting").text.lstrip().rstrip()
        Endereco_Limpo = re.sub(r'(\s+|\n)', ' ', Endereco)
        Especificacoes_limpas = re.sub(r'(\s+|\n)', ' ', especificacoes)
        APIGoogleMaps.CalculoDeDistanciasAtéMetro(Endereco_Limpo)
        MetroMaisProxímo = APIGoogleMaps.MetroMaisProximo
        MetroMaisRapido = APIGoogleMaps.MetroMaisRapido 
        DistanciaDoMetro = APIGoogleMaps.DistanciaMetro
        RapidezaoMetro = APIGoogleMaps.MetroRapido
        
        csv_writer.writerow([Titulo, url, Endereco_Limpo, Especificacoes_limpas, observações, preco, MetroMaisProxímo, MetroMaisRapido, DistanciaDoMetro, RapidezaoMetro])
        
        print("\n")
        print("***********")
        # print(Titulo + "\n" + url  + "\n" +  Endereco_Limpo  + "\n" + Especificacoes_limpas + "\n" +  observações + "\n" +  preco + "\n" +  MetroMaisProxímo + "\n" +  MetroMaisRapido + "\n" +  DistanciaDoMetro + "\n" +  RapidezaoMetro)             
        print("*************")
        print(str(i) + " pesquisas concluidas")
        print("_____________")
        print("😎")
    
        i = i + 1
        
        
        # print(Endereco_Limpo)
        # print('***********************')
        # print(MetroMaisProxímo)
        # print(MetroMaisRapido)
        # print('_________________________')
