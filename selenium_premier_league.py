from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
from selenium.webdriver.support.ui import Select

website = 'https://www.adamchoi.co.uk/overs/detailed'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

navegador = webdriver.Chrome(options = chrome_options)
navegador.get(website)

sleep(5)

try:
    cookies_button = navegador.find_element(By.CLASS_NAME, 'cc_btn_accept_all')
    cookies_button.click()
except:
    print('Não apareceu Cookies Button')

#Carregar no botão para selecionar All Matches
#XPATH: //tagName[@AttributeName='Value']
all_matches_button = navegador.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

sleep(1)

#Selecionar um Pais diferente
dropdown = Select(navegador.find_element(By.ID, "country"))
dropdown.select_by_visible_text('Portugal')

sleep(1)

#Extract data from table
rows = navegador.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
result = []
away_team = []

for match in rows:
    date.append(match.find_element(By.XPATH, './td[1]').text)    # . quer dizer que vamos procurar por XPATH a partir da localização atual: neste caso match
    home_team.append(match.find_element(By.XPATH, './td[2]').text) 
    result.append(match.find_element(By.XPATH, './td[3]').text)     # No Selenium o index começa em 1
    away_team.append(match.find_element(By.XPATH, './td[4]').text)  
    
df = pd.DataFrame({'Date':date, 'Home_team':home_team, 'Result':result, 'Away_team':away_team})

df.to_csv('football_data.csv', index=False)
