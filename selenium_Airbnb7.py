import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# SELENIUM -> indispensavel quando a web page é "reendirizada da parte do cliente" (por exemplo sites que usam React)


#Need to define these options so the driver doesn't close immediately
chrome_options = Options()
chrome_options.add_argument('window-size=600,1200')
#chrome_options.add_argument('--headless')    #para não abrir o navegador
chrome_options.add_experimental_option("detach", True)

#aceder ao website atraves do beautifull Soup
navegador = webdriver.Chrome(options = chrome_options)
navegador.get('https://www.airbnb.com')   

sleep(3)    #para aguardar que a pagina carrega ate descarregarmos o conteudo HTML
button_where = navegador.find_element(By.TAG_NAME, 'button')
ActionChains(navegador).move_to_element(button_where).click(button_where).perform()

#/homes-1-input
sleep(2) 
#input_place = navegador.find_element(By.TAG_NAME, 'input') 
input_place = navegador.find_element(By.ID, '/homes-1-input')
sleep(1)
input_place.clear()
input_place.send_keys('Punta Cana')
input_place.submit()

#ActionChains(navegador).click(input_place).send_keys("Punta Cana").perform()
#ActionChains(navegador).send_keys("Punta Cana").perform()

#converter o navegador a um object do Beautifull Soup 
# page_content = navegador.page_source          #saca o conteudo HTML da pagina
# site = BeautifulSoup(page_content, 'html.parser')     #converter esse conteudo HTMl para um objecto Beautifull Soup
# print(site.prettify())



