from importlib.resources import contents
import requests

resposta = requests.get(url='https://www.walissonsilva.com/')

print('Status code: ', resposta.status_code)    #status referente à requesição que fizemos ao website (url)
print('Headers: ', resposta.headers)

print()
print('Content: ', resposta.content)