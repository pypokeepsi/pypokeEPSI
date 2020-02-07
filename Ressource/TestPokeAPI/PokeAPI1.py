from random import *
import json
import requests

field = 'https://pokeapi.co/api/v2/pal-park-area/2/'
foret = 'https://pokeapi.co/api/v2/pal-park-area/1/'
mountain = 'https://pokeapi.co/api/v2/pal-park-area/3/'
pond = 'https://pokeapi.co/api/v2/pal-park-area/4/'
sea = 'https://pokeapi.co/api/v2/pal-park-area/5/'

url = field

# --- Recupere un index dans la liste pokemon_encounters ---
data = requests.get(url).json()
rnd = randint(1,len(data['pokemon_encounters'])) - 1

# --- Recupere l'id du pokemon avec l'index precedent ---
urlPokemonSpec = data['pokemon_encounters'][rnd]['pokemon_species']['url']
dataSpec = requests.get(urlPokemonSpec).json()
id = dataSpec['id']

# --- Recupere le pokemon avec l'id precedent ---
urlPokemon = 'https://pokeapi.co/api/v2/pokemon/'+str(id)
dataPokemon = requests.get(urlPokemon).json()

# --- Recupere 4 attaques dans la liste des moves du pokemon ---
attacks = []
moveFullSpec = []
moveSpec = []
if len(dataPokemon['moves']) <= 4:
	attacks = dataPokemon['moves']
else:
	for i in range(4):
		move = dataPokemon['moves'][randint(1,len(dataPokemon['moves'])) - 1]
		if not move in attacks:
			attacks.append(move)
for i in range(len(attacks)):
	moveFullSpec.append(attacks[i]['move'])
for i in range(len(moveFullSpec)):
		dataMove = requests.get(moveFullSpec[i]['url']).json()
		moveSpec.append({'name':dataMove['name'], 'power':dataMove['power']})

# --- Creation du pokemon dans PyPoke ---
pokemon = {
	'name':dataPokemon['name'],
	'id' : id,
	'level' : -1,
	'pv': -1,
	'fullPV': -1,
	'attacks': moveSpec,
	'stat':{
		'def': dataPokemon['stats'][3]['base_stat'],
		'att': dataPokemon['stats'][4]['base_stat'],
		'basePV': dataPokemon['stats'][5]['base_stat']
	},
	'capture_rate': dataSpec['capture_rate'],
	'evolution_chain': dataSpec['evolution_chain']['url'],
	'image':{
			'front':'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/'+str(id)+'.png',
			'back':'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/'+str(id)+'.png'
		},
	'flavor_text':dataSpec['flavor_text_entries'][1]['flavor_text']
}

#print(pokemon)

# --- Formule de calcul des differentes stats ---
# damage = (((((niv*0.4+2)*att*pui)/( defense *50))+2)*0.8

# if capture > 254
# capture = (1-(2/3)*(pv/initPv))*capture_rate*ballRate*1

# pv = ((2*base*16*42)*niveau/(100))+niveau+10
