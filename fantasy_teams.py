import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

navegador = webdriver.Chrome(options = chrome_options)
navegador.get('https://www.nba.com/teams')

sleep(2)

try:
    cookies_button = navegador.find_element(By.ID, 'onetrust-accept-btn-handler')
    ActionChains(navegador).move_to_element(cookies_button).click(cookies_button).perform()
except:
    print('Nem pediu a cena das cookies')

sleep(2)
equipa = navegador.find_element(By.CLASS_NAME, 'TeamFigureLink_teamFigureLink__uqnNO')
ActionChains(navegador).move_to_element(equipa).click(equipa).perform()

sleep(1)

page_content = navegador.page_source    #sacar o conteudo HTML em que o navegador se encontra de momento
site = BeautifulSoup(page_content, 'html.parser')    # converter o conteudo HTML para um object do BeautifullSoup
#print(site.prettify())        


tabela = site.find('tbody')
#print(tabela.prettify())

rows = tabela.findAll('tr')
#print(row.prettify())

player = tabela.find('a')
#print(player.get_text())

celtics = []
for row in rows:
    atributos = row.findAll('td', attrs = {'class': 'text'})


    x = []
    for atributo in atributos:
        x.append(atributo.get_text())
        
    celtics.append([x[0], x[2]])
    
print(celtics)


