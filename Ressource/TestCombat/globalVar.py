# --- GLOBAL VAR ---
quit = True
gameStatus = 'board'
currentEncounter = None
mainPlayer = None
weather = 'sunny'
playerAction = 'actionWaiting'

def getFirstPokemon():
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
		'captureEnable': True
	}

def weatherCoefficient(typePokemon,weather):
	switcher = {('rain','fire'):0.75, ('rain','water'):1.25, ('rain','grass'):1.15,
				('snow','fire'):0.85, ('snow','water'):0.85, ('snow','grass'):0.85, ('snow','rock'):0.85, ('snow','snow'):1.25,
				('thunder','electric'):1.25}
	bonus = switcher.get((weather,typePokemon),1)
	return bonus

def typeCoefficient(typeDefense, typeAttack):
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
