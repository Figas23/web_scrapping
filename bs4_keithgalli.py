import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


# LOAD THE WEBPAGE

base_url = 'https://keithgalli.github.io/web-scraping/'
resposta = requests.get(base_url + 'webpage.html')     #fazer a requesição a um dado URL
content = resposta.content               #get the HTML content
site = BeautifulSoup(content, 'html.parser')



####################################################################################################################################
######################### TASK1: GRAB ALL THE SOCIAL LINKS FROM THW WEBPAGE IN 3 DIFFERENT WAYS ######################################

        ###################### 1st WAY
# result = []
# socials = site.find('ul', attrs = {'class': 'socials'})
# links = socials.find_all('a')
# for link in links:
#     result.append(link['href'])
# print(result)


        ####################### 2nd WAY
        
# links = site.select('ul.socials a')
# actual_links = [link['href'] for link in links]
# print(actual_links)


        ###################### 3rd WAY
        
# links = site.select('li.social')
# result = []
# for link in links:
#     actual_link = link.find('a') 
#     actual_link = actual_link['href']
#     social_net = link.find('b')
#     result.append([social_net.get_text()[:-1], actual_link])
# print(result)
    
 ###################################################################################################################################
 ###################################################################################################################################
 
 
 
 ####################################################################################################################################
########################################## TASK2: Scrape the table in the webpage ###################################################
 
# table = site.select('table', attrs = {'class': 'hockey-stats'})[0]    #[0] pq qnd uso o select vem em formato de lista
# #table = site.select('table.hockey-stats')[0]           #mesma merda que em cima

# #fazer o scrapping da tabela para uma pandas dataframe
# result = []
# columns = table.find('thead').find_all('th')
# column_names = [column.string for column in columns]

# rows = table.find('tbody').find_all('tr')
# for tr in rows:
#     td = tr.find_all('td')
#     row = [str(tr.get_text()).strip() for tr in td]
#     result.append(row)
    
# df = pd.DataFrame(result, columns=column_names)
# df = df.loc[df['Team'] != 'Did not play']

# print(df)
        
#################################################################################################################################
#################################################################################################################################


 
###################################################################################################################################
####################################### TASK3: Grab all fun facts that have word 'is'##############################################


# frases_is = []
# fun_facts = site.find('ul', attrs = {'class': 'fun-facts'})
# phrases = fun_facts.find_all('li')

# real_phrases = [phrase.text for phrase in phrases]
# for frase in real_phrases:
#     if 'is' in frase:
#         frases_is.append(frase)
        
# print(frases_is)



#################################################################################################################################
#################################################################################################################################



 
##################################################################################################################################
####################################### TASK4: download a image through web scraping #############################################


# imagens = site.select('div.row div.column img')
# image_url = imagens[0]['src']
# full_url = base_url + image_url

# img_data = requests.get(full_url).content
# with open('lake_comoKG.jpg', 'wb') as handler:
#     handler.write(img_data)
    
    
#################################################################################################################################
#################################################################################################################################



##################################################################################################################################
############################################## TASK5: Mistery Message Challenge ##################################################

message = []
links = site.select('div div.block li a')
real_links = [link['href'] for link in links]
for link in real_links:
    link_completo = base_url + link
    palavra = requests.get(link_completo).content
    palavra_bs = BeautifulSoup(palavra, 'html.parser')
    fixe = palavra_bs.find('p', attrs = {'id': 'secret-word'})
    message.append(fixe.string)

mistery_phrase = ' '.join(message)
print(mistery_phrase)
