import requests
from bs4 import BeautifulSoup
import pandas as pd


resposta = requests.get(url='https://www.fantasypros.com/nba/rankings/overall.php')

content = resposta.content
#print(content)

site = BeautifulSoup(content, 'html.parser')
#print(site.prettify())


tabela = site.find('div', attrs = {'class': 'mobile-table'})
#print(tabela.prettify())


jogadores = tabela.findAll('td', attrs={'class':'player-label'})
#print(jogadores)

fantasy = []

for jogador in jogadores:
    
    nome = jogador.text.split('(')
    x = ''.join(nome[1])
    if x[:2] == 'FA':
        break
    player = nome[0]
    team = nome[1][:3]
    y = x.split('-')
    w = ''.join(y[1])
    z = w.split(')')
    position = z[0]
    fantasy.append([player, team, position])
    
#print(fantasy)

fant = pd.DataFrame(fantasy, columns=['Player', 'Team', 'Position'])
print(fant)



#rank = tabela.find('td')
#print(rank.text)
