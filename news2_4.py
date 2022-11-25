import requests
from bs4 import BeautifulSoup
import pandas as pd


lista_noticias = []

resposta = requests.get(url='https://g1.globo.com/')

#print(resposta.content)    #imprime conteudo html da pagina à qual fizemos o request

content = resposta.content

#vamos converter este conteudo do html num Object do BeautifulSoup
site = BeautifulSoup(content, 'html.parser')

#print(type(site))   #site é um object do BeautifulSoup
#print(site.prettify())    #ver o conteudo do site (object BeautifulSoup mais bonito e menos confuso)

# #Agora em vez de procurar uma noticia vou procurar varias (HTML de varias noticias)
noticias = site.findAll('div', attrs = {'class': 'feed-post-body'})  #procurar todas as ocorrencias daquela tag com aquela class no conteudo TML do site

for noticia in noticias:
    
    #Titulo da noticia
    titulo = noticia.find('a', attrs = {'class': 'feed-post-link'})
    #print(titulo.text)    #para obter só mesmo o conteudo escrito do titulo
    #print(titulo['href'])   #permite sacar o link da noticia    

    #Subtitulo
    subtitulo = noticia.find('div', attrs = {'class': 'bstn-fd-relatedtext'})
    
    if subtitulo:    #é necessário verificar se o subtitulo existe
        #print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
        
    lista_noticias.append([titulo.text, '', titulo['href']])
    
#print(lista_noticias)

#com esta lista de listas podemos criar uma dataframe
news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtitulo', 'Link'])
#print(news)

#Se quisermos gravar esta dataframe como um csv ou excel
news.to_excel('noticias.xlsx', index=False)
