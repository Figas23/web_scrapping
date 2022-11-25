import requests
from bs4 import BeautifulSoup
import pandas as pd

resposta = requests.get(url = 'https://www.nba.com/news/nba-fantasy-top-150-rankings-2022-23-part-3')

content = resposta.content
#print(content)

site = BeautifulSoup(content, 'html.parser')
#print(site.prettify())



noticia = site.find('ol')
#print(noticia.prettify())

jogadores = noticia.findAll('li')
#print(jogadores)

fantasy = []

for jogador in jogadores:
    
    #print(jogador.text)
    x = jogador.text.split(':')
    descricao = x[-1]
    y = ''.join(x[0])
    z = y.split(',')
    player = z[0]
    team = z[1]
    
    fantasy.append([team, player, descricao])
    
    
fant = pd.DataFrame(fantasy, columns=['Team', 'Player', 'Description'])
print(fant)
    

