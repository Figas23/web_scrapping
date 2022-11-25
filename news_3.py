import requests
from bs4 import BeautifulSoup

resposta = requests.get(url='https://g1.globo.com/')

#print(resposta.content)    #imprime conteudo html da pagina à qual fizemos o request

content = resposta.content

#vamos converter este conteudo do html num Object do BeautifulSoup
site = BeautifulSoup(content, 'html.parser')

#print(type(site))   #site é um object do BeautifulSoup
#print(site.prettify())    #ver o conteudo do site (object BeautifulSoup mais bonito e menos confuso)

#HTML da noticia
noticia = site.find('div', attrs = {'class': 'feed-post-body'})  #procurar algo especifico no codigo html do site
#print(noticia.prettify())

#Titulo da noticia
titulo = noticia.find('a', attrs = {'class': 'feed-post-link'})
print(titulo.text)    #para obter só mesmo o conteudo escrito do titulo


#Subtitulo <div class="bstn-fd-relatedtext">
subtitulo = noticia.find('div', attrs = {'class': 'bstn-fd-relatedtext'})
print(subtitulo.text)






