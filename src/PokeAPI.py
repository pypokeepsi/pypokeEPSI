# -*- coding: utf-8 -*-
from random import *
import json
import requests
from math import *

def getArea(area):
	field = 'https://pokeapi.co/api/v2/pal-park-area/2/'
	foret = 'https://pokeapi.co/api/v2/pal-park-area/1/'
	mountain = 'https://pokeapi.co/api/v2/pal-park-area/3/'
	pond = 'https://pokeapi.co/api/v2/pal-park-area/4/'
	sea = 'https://pokeapi.co/api/v2/pal-park-area/5/'
	switcher={'field':field, 'foret':foret,'mountain':mountain,'pond':pond,'sea':sea}
	return switcher.get(area,"Invalid area")

def getLevel(board):
	# REPARTITION DES NIVEAUX DE POKEMON EN FONCTION DU PLATEU
	# 8 --> 5-10
	# 5,9 --> 10-20
	# 1,2,3,6 --> 15-25
	# 4 --> 20-30
	# 7 --> 30-40
	switcher={8:randint(5,10),5:randint(10,20),9:randint(10,20),1:randint(15,25),2:randint(15,25),3:randint(15,25),6:randint(15,25),4:randint(20,30),7:randint(30,40)}
	return switcher.get(board,"Invalid board")	

def getRandomEncounterPokemon(area, board):
	# PLATEAU
	# 1 2 3
	# 4 5 6
	# 7 8 9
	url = getArea(area)
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
			moveSpec.append({'name':dataMove['name'], 'power':dataMove['power'], 'type': dataMove['type']['name']})
	
	level = getLevel(board)
	pv =ceil( ((2*dataPokemon['stats'][5]['base_stat']+90)*level/(100))+level+10 )
	# --- Creation du pokemon dans PyPoke ---
	pokemon = {
		'name':dataPokemon['name'],
		'id' : id,
		'level' : level,
		'pv': pv,
		'fullPV': pv,
		'type': dataPokemon['types'][0]['type']['name'],
		'attacks': moveSpec,
		'stat':{
			'def': dataPokemon['stats'][3]['base_stat'],
			'att': dataPokemon['stats'][4]['base_stat'],
			'basePV': dataPokemon['stats'][5]['base_stat']
		},
		'xp':0,
		'nextLevel':50,
		'capture_rate': dataSpec['capture_rate'],
		'evolution_chain': dataSpec['evolution_chain']['url'],
		'image':{
				'front':'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/'+str(id)+'.png',
				'back':'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/'+str(id)+'.png'
			},
		'flavor_text':dataSpec['flavor_text_entries'][1]['flavor_text']
	}
	#print(pokemon)
	return pokemon

	# --- Formule de calcul des differentes stats ---
	# damage = (((((niv*0.4+2)*att*pui)/( defense *50))+2)*1.5

	# if capture > 254
	# capture = (1-(2/3)*(pv/initPv))*capture_rate*ballRate*1

	# pv = ((2*base*16*42)*niveau/(100))+niveau+10

# print (getEncounterPokemon('field',8))

def getFirstPokemon(id=25):
	url = getArea('field')
	urlPokemonSpec = 'https://pokeapi.co/api/v2/pokemon-species/'+str(id)
	dataSpec = requests.get(urlPokemonSpec).json()
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
			moveSpec.append({'name':dataMove['name'], 'power':dataMove['power'], 'type': dataMove['type']['name']})
	
	level = 7
	pv =ceil( ((2*dataPokemon['stats'][5]['base_stat']+90)*level/(100))+level+10 )
	# --- Creation du pokemon dans PyPoke ---
	pokemon = {
		'name':dataPokemon['name'],
		'id' : id,
		'level' : level,
		'pv': pv,
		'fullPV': pv,
		'type': dataPokemon['types'][0]['type']['name'],
		'attacks': moveSpec,
		'stat':{
			'def': dataPokemon['stats'][3]['base_stat'],
			'att': dataPokemon['stats'][4]['base_stat'],
			'basePV': dataPokemon['stats'][5]['base_stat']
		},
		'xp':0,
		'nextLevel':50,
		'capture_rate': dataSpec['capture_rate'],
		'evolution_chain': dataSpec['evolution_chain']['url'],
		'image':{
				'front':'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/'+str(id)+'.png',
				'back':'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/'+str(id)+'.png'
			},
		'flavor_text':dataSpec['flavor_text_entries'][1]['flavor_text'],
		'captureEnable':True
	}
	return pokemon

def noConnection():
	return {
		'name': 'pikachu',
		'id': 25,
		'level': 7,
		'pv': 29,
		'fullPV': 29,
		'type':'normal',
		'attacks': [{'name': 'captivate', 'power': None, 'type':'normal'}, {'name': 'brick-break', 'power': 75, 'type':'normal'}, {'name': 'dynamic-punch', 'power': 100, 'type':'normal'}, {'name': 'rollout', 'power': 30, 'type':'normal'}],
		'stat': {'def': 40, 'att': 55, 'basePV': 35},
		'xp': 0,
		'nextLevel': 50,
		'capture_rate': 190,
		'evolution_chain': 'https://pokeapi.co/api/v2/evolution-chain/10/',
		'image': {
			'front': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png',
			'back': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png'
			},
		'flavor_text': '電気を\u3000ため込む\u3000性質。\nピカチュウが\u3000群れて\u3000暮らす\u3000森は\n落雷が\u3000絶えず\u3000危険だ。',
		'captureEnable': True
	}