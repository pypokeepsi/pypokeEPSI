import json
from random import *
import globalVar
from globalVar import getFirstPokemon
from globalVar import weatherCoefficient
from globalVar import typeCoefficient

# --- BUSINESS OBJECT ---
class PlayerBO:
	def __init__(self, name, pokemons=None):
		self.pseudo = name
		self.age = 8
		self.money = 0
		self.currentPokemon = 0
		self.inventory = {}
		if pokemons == None:
			self.pokemons = [PokemonBO(getFirstPokemon()),PokemonBO(getFirstPokemon())]
		else:
			self.pokemons = pokemons
	def getPokemonsData(self):
		res = ''
		for p in self.pokemons:
			res += json.dumps(p.pokeData)+'\n ======================= \n'
		return res
	def pokemonsAlive(self):
		for p in self.pokemons:
			if p.isAlive():
				return True
		return False
	def changeCurrentPokemon(self):
		for i in range(len(self.pokemons)):
			if self.pokemons[i].isAlive():
				self.currentPokemon = i
				break

class PokemonBO:
	def __init__(self, pokemonDataJSON):
		self.pokeData = pokemonDataJSON
	def isAlive(self):
		return self.pokeData['pv']>0
	def defense(self, power, typeAttack):
		critical = {10:1.5}.get(randint(1,10),1)
		damage = round((((int(power)//(int(self.pokeData['stat']['def']) *50))+2)*1.5) * weatherCoefficient(globalVar.weather,self.pokeData['type']) * critical * randint(8,10)/10 * typeCoefficient(self.pokeData['type'], typeAttack))
		self.pokeData['pv'] -= damage
		return {'Attack damage': damage, 'Critical hit': critical==1.5, 'Opponent pv':self.pokeData['pv']}
	def attack(self, power):
		if power == None:
			power = 0
		return round(((int(self.pokeData['level'])*0.4+2)*int(self.pokeData['stat']['att'])*power))

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

# --- GAME FUNCTION ---
def startEncounterFunc():
	globalVar.currentEncounter = EncounterBO(globalVar.mainPlayer, PlayerBO('computer',[PokemonBO(getFirstPokemon())]))
	globalVar.gameStatus = 'currentEncounterStatus'
def moveFunc():
	print('you moved')
	if randint(1,3) == 1:
		globalVar.gameStatus = 'startEncounterStatus'
def quitFunc():
	print('exit')
	globalVar.quit = False

# --- GAME INIT ---
globalVar.mainPlayer = PlayerBO('sacha')
# --- GAME LOOP ---
while(globalVar.quit):

	# --- GAME STATUS ---
	# - Start encounter -
	if globalVar.gameStatus == 'startEncounterStatus':
		print('start encounter')
		startEncounterFunc()
	# - During encounter -
	if globalVar.gameStatus == 'currentEncounterStatus':
		# - Waiting player action -
		if globalVar.playerAction == 'actionWaiting':
			print('--- Waiting for player action ---')
		# - Computer play -
		elif globalVar.playerAction == 'actionRelease':
			print('- COMPUTER PLAYED -')
			print('Computer damage result : '+globalVar.currentEncounter.computerPlay())
			globalVar.playerAction = 'actionWaiting'
	# - At end of encounter -
	if globalVar.gameStatus == 'endEncounterStatus':
		print (' --- ENCOUNTER ENDING --- ')
		print('Winner is : ' + globalVar.currentEncounter.getWinner())
		globalVar.gameStatus = 'board'
		globalVar.currentEncounter = None
		globalVar.playerAction = 'actionWaiting'

	# --- EVENT ---
	commande = input("Enter commande: ")
	if commande == 'quit':
		quitFunc()
	elif commande == 'move':
		moveFunc()
	elif commande == 'attack':
		if globalVar.gameStatus == 'currentEncounterStatus':
			globalVar.playerAction = 'actionRelease'
			print('- PLAYER PLAYED -')
			print('Player damage result : '+globalVar.currentEncounter.attack(50,'normal'))
		else:
			print('error - not in encounter')
	elif commande == 'help':
		print('Game status : '+globalVar.gameStatus)
		if globalVar.gameStatus == 'currentEncounterStatus':
			print('Current encounter : '+str(globalVar.currentEncounter.help()))
	elif commande == 'info':
		print(globalVar.mainPlayer.getPokemonsData())
	else:
		print('/!\\ ERROR /!\\')
