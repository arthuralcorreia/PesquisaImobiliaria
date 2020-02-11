import requests
from bs4 import BeautifulSoup
import APIGoogleMaps
import re

page = requests.get('https://www.imovelweb.com.br/apartamentos-venda-sao-paulo-sp-menos-400000-reales.html')
html_soup = BeautifulSoup(page.text, 'html.parser')


ape_container = html_soup.find('div', class_ = 'posting-card super-highlighted')

Titulo = (ape_container.find('div', class_ = 'posting-heading').h2.text).lstrip().rstrip()

Endereco = (ape_container.find('div', class_ = 'posting-heading').span.text).lstrip().rstrip()

especificacoes = ape_container.find("ul", class_ = "main-features go-to-posting").text.lstrip().rstrip()

observações = ape_container.find('div', class_ = 'posting-description go-to-posting').text.lstrip().rstrip()

preco = ape_container.find("div", class_ = 'prices').text.lstrip().rstrip()

publicacoes = ape_container.find("ul", class_ = "posting-features go-to-posting").text.lstrip().rstrip()

APIGoogleMaps.CalculoDeDistanciasAtéMetro(Endereco)
print(re.sub(' +', ' ', Endereco))

# print("\n" + Titulo + "\n")
# print(Endereço + "\n")
# print(especificacoes + "\n")
# print(observações + "\n")
# print(preco + "\n")
# print(publicacoes + "\n")
