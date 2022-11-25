import requests
from bs4 import BeautifulSoup
import pandas as pd

# Script to obtain products from Mercado Livre accordingly to a User search

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Produto a procurar? ')

resposta = requests.get(url_base + produto_nome)

site = BeautifulSoup(resposta.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': "andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default andes-card--animated"})
#print(produto.prettify())

lista_produtos = []

for produto in produtos:

    titulo = produto.find('h2', attrs = {'class': 'ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title'})
    #print('Titulo do Produto: ', titulo.text)

    link = produto.find('a', attrs = {'class': "ui-search-link"})
    #print('Link do Produto: ', link['href'])     #as tags 'a' tem sempre 'href' para o link

    real = produto.find('span', attrs = {'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs = {'class': 'price-tag-cents'})
    if centavos:
        #print('Preço do produto: R$', real.text + ',' + centavos.text)
        lista_produtos.append([titulo.text, real.text + ',' + centavos.text, link['href']])
    else:
        #print('Preço do produto: R$', real.text)
        lista_produtos.append([titulo.text, real.text, link['href']])
    
    print('\n\n')
    
product_description = pd.DataFrame(lista_produtos, columns=['Titulo', 'Preço (R$)', 'Link'])
print(product_description)
