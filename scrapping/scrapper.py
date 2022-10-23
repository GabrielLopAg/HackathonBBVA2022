# new packages: requests, lxml, beautifulsoup4
import requests
from bs4 import BeautifulSoup

def scrap_inegi(name='us stick'):
    token = '6d38855b-79b2-49c8-b7e4-46ae7fdd605c'
    r = requests.get(f'https://www.inegi.org.mx/app/api/denue/v1/consulta/Nombre/{name}/00/1/1/'+token)
    if r.status_code==200:
        a = r.json()[0]
        return [a['Estrato'], a['Nombre']]
    else:
        return ['No data']

def scrap_pyme_org(name='us stick', city='CDMX'):
    cities = {
        'CDMX': 'Ciudad-de-México',
        'Estado de Mexico': 'Estado-de-México'
    }
    r = requests.get(f'https://pymes.org.mx/entidad/{cities[city]}.html',params={
        "Pyme[nombre]":name,
        'Pyme_page': 1
        })
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.find('a', itemprop='name')
    # if data:
    #     cp = data[-1]
    #     muni = data[-2]

    if data:
        r = requests.get('https://pymes.org.mx'+data.get('href'))
        soup = BeautifulSoup(r.text, 'lxml')
        return [c for c in soup.find('article', class_='pyme').div.div.div.div.div.p.children][3].string
    else:
        return ['No data']
    
scrap_inegi()