from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('window-size = 800, 1600')


navegador = webdriver.Chrome(options = chrome_options)
navegador.get('https://www.rapidtables.com/convert/temperature/celsius-to-kelvin.html')

navegador.implicitly_wait(5)


try:
    cookies_button = navegador.find_element(By.ID, 'pgdg-continue')
    navegador.implicitly_wait(10)
    ActionChains(navegador).move_to_element(cookies_button).click(cookies_button).perform()
    
    not_robbot_button = navegador.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border')
    navegador.implicitly_wait(10)
    ActionChains(navegador).move_to_element(not_robbot_button).click(not_robbot_button).perform()
    
    not_robbot_submit = navegador.find_element(By.ID, 'captcha-submit')
    navegador.implicitly_wait(10)
    ActionChains(navegador).move_to_element(not_robbot_submit).click(not_robbot_submit).perform()
except:
    print('Nem apareceu a cena das cookies ...')
    
# ESTE SITE TEM A CENA PARA IMPEDIR QUE ROBOTS ACEDAM, PORTANTO NÃO CONSIGO ENTRAR