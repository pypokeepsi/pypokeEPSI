# -*- coding: utf-8 -*-
import globalVar
from constants import *
from PokeAPI import *
from random import *
import json

class PlayerBO:
	def __init__(self, name, pokemons=None):
		self.pseudo = name
		self.age = 8
		self.money = 0
		self.currentPokemon = 0
		if pokemons == None:
			self.pokemons = [PokemonBO(getFirstPokemon()), PokemonBO(getRandomEncounterPokemon('field', 8))]
		else:
			self.pokemons = pokemons
		self.inventory = {}

	def changeCurrentPokemon(self):
		for i in range(len(self.pokemons)):
			if self.pokemons[i].isAlive():
				self.currentPokemon = i
				break

	def addPokemon(self,pokemon):
		self.pokemons.append(PokemonBO(pokemon))

	def pokemonsAlive(self):
		for p in self.pokemons:
			if p.isAlive():
				return True
		return False
	def killPokemon(self):
		self.pokemons[self.currentPokemon].pokeData['pv']=-1
	def getPokemonsData(self):
		res = ''
		for p in self.pokemons:
			res += json.dumps(p.pokeData)+'\n ======================= \n'
		return res

	def healPokemons(self):
		for p in self.pokemons:
			p.pokeData['pv'] = p.pokeData['fullPV']
			self.currentPokemon=0

	def initInventory(self):
		self.inventory = {
			'pokeball':[
					{'name':'PokeBall','id':0,'quantity':5,'bonus':1},
					{'name':'SuperBall','id':1,'quantity':3,'bonus':1.5},
					{'name':'Hyperball','id':2,'quantity':1,'bonus':2},
					{'name':'MasterBall','id':3,'quantity':0,'bonus':999}
				],
			'object':[
					{'name':'Escape rope','id':0,'quantity':0,'description':'Very use full in cave'},
					{'name':'Potion','id':1,'quantity':0, 'description':"Restore little part of PV"},
					{'name':'SuperPotion','id':2,'quantity':0, 'description':"Restore part of PV"},

					{'name':'HyperPotion','id':3,'quantity':0, 'description':"Restore great part of PV"},
					{'name':'Revive','id':4,'quantity':0, 'description':"Revive pokemon"},
					{'name':'Repel','id':5,'quantity':0, 'description':"Reduce the sauvage encounter"},

					{'name':'Fluffy Tail','id':6,'quantity':0, 'description':"Increase the sauvage encounter"},
					{'name':'Sports Shoe','id':7,'quantity':0, 'description':"Indispensable object"},
					{'name':'Fishing rod','id':8,'quantity':0, 'description':"Take some break and fish"}
				]
		}

class PokemonBO:
	def __init__(self, pokemonDataJSON):
		self.pokeData = pokemonDataJSON

	def isAlive(self):
		print(self.pokeData['name'],' : ',str(self.pokeData['pv']),' / ',str(self.pokeData['fullPV']))
		return self.pokeData['pv'] > 0

	def defense(self, power, typeAttack):
		"""
		--- Critical coefficient ---
		1,2,3,4,5,6,7,8,9 	→ 1
		10 					→ 1.5
		"""
		critical = {10:1.5}.get(randint(1,10),1)
		damage = round((((int(power)//(int(self.pokeData['stat']['def']) *50))+2)*1.5) * weatherCoefficient(globalVar.weather,self.pokeData['type']) * critical * randint(8,10)/10 * typeCoefficient(self.pokeData['type'], typeAttack))
		self.pokeData['pv'] -= damage
		return {'Attack damage': damage, 'Critical hit': critical==1.5, 'Opponent pv':self.pokeData['pv']}

	def attack(self, power):
		if power == None:
			power = 0
		return round(((int(self.pokeData['level'])*0.4+2)*int(self.pokeData['stat']['att'])*power))

	def capture(self,pokeballBonus):
		capture = (1-(2/3)*(self.pokeData['pv']/self.pokeData['fullPV']))*pokeballBonus*1
		globalVar.currentTextBox.write("Capture : "+str(capture),(120,80,80))
		if capture >= 1:
			return True
		return False

class EncounterBO:
	def __init__(self, player, computer):
		self.player = player
		self.computer = computer

	def attack(self, power, typeAttack):
		attack = self.player.pokemons[self.player.currentPokemon].attack(power)
		damage = self.computer.pokemons[self.computer.currentPokemon].defense(attack,typeAttack)
		if damage['Opponent pv'] < 0:
			if not self.computer.pokemonsAlive():
				globalVar.gameStatus = 'endEncounterStatus'
			else:
				self.computer.changeCurrentPokemon()
		return json.dumps(damage)

	def computerPlay(self):
		attackIndex = randint(0,len(self.computer.pokemons[self.computer.currentPokemon].pokeData['attacks'])-1)
		powerAttack = self.computer.pokemons[self.computer.currentPokemon].pokeData['attacks'][attackIndex]['power']
		globalVar.currentTextBox.write(self.computer.pokemons[self.computer.currentPokemon].pokeData['attacks'][attackIndex]['name'],(50,80,80))
		typeAttack = self.computer.pokemons[self.computer.currentPokemon].pokeData['attacks'][attackIndex]['type']
		attack = self.computer.pokemons[self.computer.currentPokemon].attack(powerAttack)
		damage = self.player.pokemons[self.player.currentPokemon].defense(attack, typeAttack)
		if damage['Opponent pv'] < 0:
			if not self.player.pokemonsAlive():
				globalVar.gameStatus = 'endEncounterStatus'
			else:
				self.player.changeCurrentPokemon()
		return json.dumps(damage)

	def getWinner(self):
		if self.player.pokemonsAlive():
			return 'player'
		return 'computer'

	def help(self):
		return 'player Pokemon : '+str(self.player.pokemons[self.player.currentPokemon].pokeData['pv']) + '    ' + 'computer Pokemon : '+str(self.computer.pokemons[self.computer.currentPokemon].pokeData['pv'])

	def useItem(self):
		globalVar.currentTextBox.write("Ce n'est pas très efficace",(50,50,50))

	def usePokeball(self,id):
		chance = pokeballCoefficient(id)
		if self.computer.pokemons[self.computer.currentPokemon].capture(chance):
			globalVar.persoMain.addPokemon(self.computer.pokemons[self.computer.currentPokemon].pokeData)
			self.computer.killPokemon()
			globalVar.currentTextBox.write("Capture réussi",(120,120,120))
		else :
			globalVar.currentTextBox.write("Capture echoué",(120,80,80))


		




def weatherCoefficient(typePokemon,weather):
	"""
	--- Power effect by weather status ---
	sunny 	→ nothing
	rain 	→ fire↓25% water↑25% grass↑15% 
	snow 	→ fire↓15% water↓15% grass↓15% rock↓15% ice↑25%
	thunder → electric↑25%
	"""
	switcher = {('rain','fire'):0.75, ('rain','water'):1.25, ('rain','grass'):1.15,
				('snow','fire'):0.85, ('snow','water'):0.85, ('snow','grass'):0.85, ('snow','rock'):0.85, ('snow','snow'):1.25,
				('thunder','electric'):1.25}
	bonus = switcher.get((weather,typePokemon),1)
	return bonus

def typeCoefficient(typeDefense, typeAttack):
	# https://i.imgur.com/D5xlT9d.png
	switcher = {
		'normal': 	{'normal': 1,	'fire': 1,	'water': 2, 'electric': 0, 'grass': 2, 'ice': 2, 'poison': 0.5,	'flying': 1, 	'psychic': 1,	'bug': 1,	'rock': 0.5, 'ghost': 0, 	'dragon': 1, 	'dark': 1, 'steel': 1},
		'fire': 	{'normal': 1,	'fire': 0.5,'water': 4, 'electric': 0, 'grass': 1, 'ice': 1, 'poison': 0.5, 'flying': 1, 	'psychic': 1,	'bug': 0.5, 'rock': 1, 	 'ghost': 1, 	'dragon': 1, 	'dark': 1, 'steel': 0.5},
		'water': 	{'normal': 1,	'fire': 0.5,'water': 1, 'electric': 0, 'grass': 4, 'ice': 1, 'poison': 0.5, 'flying': 1, 	'psychic': 1,	'bug': 1, 	'rock': 0.5, 'ghost': 1, 	'dragon': 1, 	'dark': 1, 'steel': 0.5},
		'electric': {'normal': 1,	'fire': 1,	'water': 2, 'electric': 0, 'grass': 2, 'ice': 2, 'poison': 0.5, 'flying': 0.5, 	'psychic': 1,	'bug': 1, 	'rock': 0.5, 'ghost': 1, 	'dragon': 1, 	'dark': 1, 'steel': 1},
		'grass': 	{'normal': 1,	'fire': 2,	'water': 1, 'electric': 0, 'grass': 1, 'ice': 4, 'poison': 0.5, 'flying': 2, 	'psychic': 1, 	'bug': 2, 	'rock': 0.5, 'ghost': 1, 	'dragon': 1, 	'dark': 1, 'steel': 1},
		'ice': 		{'normal': 1,	'fire': 2,	'water': 2, 'electric': 0, 'grass': 2, 'ice': 1, 'poison': 0.5, 'flying': 1, 	'psychic': 1, 	'bug': 1, 	'rock': 1, 	 'ghost': 1, 	'dragon': 1, 	'dark': 1, 'steel': 2},
		'poison': 	{'normal': 1,	'fire': 1,	'water': 2, 'electric': 0, 'grass': 1, 'ice': 2, 'poison': 0.5, 'flying': 1, 	'psychic': 2, 	'bug': 0.5, 'rock': 0.5, 'ghost': 1, 	'dragon': 1, 	'dark': 1, 'steel': 1},
		'flying': 	{'normal': 1,	'fire': 1,	'water': 2, 'electric': 0, 'grass': 1, 'ice': 4, 'poison': 0.5, 'flying': 1, 	'psychic': 1, 	'bug': 0.5, 'rock': 1, 	 'ghost': 1, 	'dragon': 1, 	'dark': 1, 'steel': 1},
		'psychic': 	{'normal': 1,	'fire': 1,	'water': 2, 'electric': 0, 'grass': 2, 'ice': 2, 'poison': 0.5, 'flying': 1, 	'psychic': 0.5, 'bug': 2, 	'rock': 0.5, 'ghost': 1, 	'dragon': 1, 	'dark': 1, 'steel': 1},
		'bug': 		{'normal': 1,	'fire': 2,	'water': 2, 'electric': 0, 'grass': 1, 'ice': 2, 'poison': 0.5, 'flying': 2, 	'psychic': 1, 	'bug': 1, 	'rock': 0.5, 'ghost': 1, 	'dragon': 1, 	'dark': 1, 'steel': 1},
		'rock': 	{'normal': 0.5,	'fire': 0.5,'water': 4, 'electric': 0, 'grass': 4, 'ice': 2, 'poison': 0.5, 'flying': 0.5, 	'psychic': 1, 	'bug': 1, 	'rock': 0.5, 'ghost': 1, 	'dragon': 1, 	'dark': 1, 'steel': 2},
		'ghost': 	{'normal': 0,	'fire': 0,	'water': 2, 'electric': 0, 'grass': 2, 'ice': 2, 'poison': 0.5, 'flying': 1, 	'psychic': 1, 	'bug': 0.5, 'rock': 0.5, 'ghost': 2, 	'dragon': 2, 	'dark': 1, 'steel': 1},
		'dragon': 	{'normal': 1,	'fire': 0.5,'water': 1, 'electric': 0, 'grass': 1, 'ice': 4, 'poison': 0.5, 'flying': 1, 	'psychic': 1, 	'bug': 1, 	'rock': 0.5, 'ghost': 1, 	'dragon': 1, 	'dark': 2, 'steel': 1},
		'dark': 	{'normal': 1,	'fire': 1,	'water': 2, 'electric': 0, 'grass': 2, 'ice': 2, 'poison': 0.5, 'flying': 1, 	'psychic': 0, 	'bug': 2, 	'rock': 0.5, 'ghost': 0.5,	'dragon': 0.5, 	'dark': 1, 'steel': 1},
		'steel': 	{'normal': 1,	'fire': 2,	'water': 2, 'electric': 0, 'grass': 1, 'ice': 1, 'poison': 0, 	'flying': 0.5, 	'psychic': 0.5, 'bug': 0.5, 'rock': 0.25,'ghost': 1, 	'dragon': 1, 	'dark': 0.5, 'steel': 0.5}
	}
	return switcher.get(typeDefense,{'default':1}).get(typeAttack,1)

def pokeballCoefficient(id):
	pokeball = {0:1,1:1.5,2:2,3:999}
	return pokeball.get(id,0)
					
					
				
	