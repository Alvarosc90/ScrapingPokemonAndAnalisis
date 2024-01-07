import requests
from bs4 import BeautifulSoup
import pandas as pd
# URL de la página web que deseas analizar
url = 'https://pokemondb.net/pokedex/all'

import os

print("Directorio actual:", os.getcwd())

# Realiza una solicitud HTTP para obtener el contenido HTML
response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')

arrows = soup.find('table',attrs={"id":"pokedex"}).find('tbody').find_all('tr')

names = []
types = []
total = []
hp = []
attack = []
defense = []
sp_att = []
sp_def = []
speed = []

for arrow in arrows:
    names.append(arrow.find_all('td')[1].get_text())
    types.append(arrow.find_all('td')[2].get_text())
    total.append(arrow.find_all('td')[3].get_text())
    hp.append(arrow.find_all('td')[4].get_text())
    attack.append(arrow.find_all('td')[5].get_text())
    defense.append(arrow.find_all('td')[6].get_text())
    sp_att.append(arrow.find_all('td')[7].get_text())
    sp_def.append(arrow.find_all('td')[8].get_text())
    speed.append(arrow.find_all('td')[9].get_text())

df = pd.DataFrame({'Nombre':names,'Tipo':types,'Total':total,'Vida':hp,'Ataque':attack,'Defensa':defense,'Ataque_Esp':sp_att,'Defense_Esp':sp_def,'Velocidad':speed})
print(df)

df.to_csv('pokemon.csv', index=False)
'''
src_todos = soup.find_all(src=True)
url_imagenes = ['https://img.pokemondb.net/sprites/sword-shield/icon/']

#descargado imagenes de pokemon
for i, imagen in enumerate(src_todos):

  if imagen['src'].endswith('png'):

    print(imagen['src'])
    r = requests.get(f"https://img.pokemondb.net/sprites/sword-shield/icon/{imagen['src']}")

    with open(f'imagen_{i}.png', 'wb') as f:
      f.write(r.content)
'''
