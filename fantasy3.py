import requests
from bs4 import BeautifulSoup
import pandas as pd


resposta = requests.get(url='https://www.rotowire.com/basketball/article/fantasy-basketball-rankings-jokic-curry-lead-top-150-for-2022-23-nba-season-65209')

content = resposta.content   #saca o conteudo html da pagina em que fizemos o request

site = BeautifulSoup(content, 'html.parser')     #converter o conteudo HTML num object do BeautifullSoup



jogadores = site.findAll('li')

fantasy = []

for jogador in jogadores:
    
    tudo = jogador.text
    tudo = tudo.split(',')
    if len(tudo) != 3:
        continue
    player = tudo[0]
    position = tudo[1]
    team = tudo[2]
    
    
    fantasy.append([player, position, team])
    
    

fant = pd.DataFrame(fantasy, columns=['Player', 'Position', 'Team'])
print(fant)
    