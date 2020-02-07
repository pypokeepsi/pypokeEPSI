# -*- coding: utf-8 -*-
# pip install pygame
# pip install requests
# pip install Pillow

import pygame # Import de Pygame
from pygame.locals import * # Import des constante de Pygame
from PlayerBean import *
from BusinessObject import *
from DecorBean import *
from constants import *
from BoardBean import *
from EncounterBean import *
from PokedexBean import *
import globalVar
import random
# --- Initialisation de pygame ---
pygame.init()
screen = pygame.display.set_mode(windows_size)
# Set Icone
pygame.display.set_icon(pygame.image.load(icone_image).convert_alpha())
# Set title
pygame.display.set_caption(windows_title)
# Disable mouse
pygame.mouse.set_visible(False)

#fond = pygame.image.load(fond_image).convert()
#fond = pygame.transform.scale(fond, windows_size)
globalVar.gameStatus = 'boardStatus'
globalVar.persoMain = PlayerBO('sacha')
globalVar.persoMain.initInventory()


currentBoard = Board8()
currentDisplay = currentBoard

# Permet de repeter une action quand une touche reste enfoncee set_repeat(DelaiDePriseEnCompte, DelaiEntreChaqueExecution)
pygame.key.set_repeat(200, 30)
# Fixer le fps
clock = pygame.time.Clock()
done = 0

globalVar.currentTextBox.write('Welcome', (0,0,225))
globalVar.currentTextBox.write('on PyPoke', (0,0,225))
globalVar.currentTextBox.write('Move with ZQSD', (0,0,225))
globalVar.currentTextBox.write('Escape fight with space', (0,0,225))
globalVar.currentTextBox.write('Press E to interact', (0,0,225))
globalVar.currentTextBox.write('Have FUN', (255,0,225))


# Boucle infinie
while not done:
	# --- ------------------------------------------- ---
	# ---                 GAME STATUS                 ---
	# ---                                             ---
	# - On sort d'un affichage pour revenir sur le plateau -
	if globalVar.gameStatus == 'boardStatus':
		currentDisplay = currentBoard
		globalVar.currentTextBox = currentDisplay.decorList[-1]
	if globalVar.gameStatus == 'newBroadStatus':
		if globalVar.currentPlateau == 5:
			globalVar.currentPlateau = 8
			currentBoard = Board8()
		else:
			globalVar.currentPlateau = 5
			currentBoard = Board5()
		currentDisplay = currentBoard
		globalVar.gameStatus = 'boardStatus'


	# --- Phase de combat ---
	# - Déclenchement du combat -
	if globalVar.gameStatus == 'startEncounterStatus':
		# - Creation du pokemon rencountre -
		#pokemonEncounter = getRandomEncounterPokemon(areaType.get(globalVar.currentPlateau), globalVar.currentPlateau)
		#pokemonEncounter = PokemonBO(pokemonEncounter)
		computerPlayer = PlayerBO('computer',[PokemonBO(getRandomEncounterPokemon(currentDisplay.area, globalVar.currentPlateau))])
		globalVar.currentEncounter = EncounterBO(globalVar.persoMain, computerPlayer)
		currentDisplay = EncounterBean(computerPlayer)
		globalVar.gameStatus = 'currentEncounterStatus'
	# - Début du combat -
	if globalVar.gameStatus == 'currentEncounterStatus':		
		# - Waiting player action -
		if globalVar.playerAction == 'actionWaiting':
			pass
			#print('--- Waiting for player action ---')
		# - Computer play -
		elif globalVar.playerAction == 'actionRelease':
			print('- COMPUTER PLAYED -')
			print('Computer damage result : '+globalVar.currentEncounter.computerPlay())
			currentDisplay.update()
			globalVar.playerAction = 'actionWaiting'
	# - Fin du combat -
	if globalVar.gameStatus == 'endEncounterStatus':
		print (' --- ENCOUNTER ENDING --- ')
		print('Winner is : ' + globalVar.currentEncounter.getWinner())
		globalVar.gameStatus = 'boardStatus'
		globalVar.currentEncounter = None
		globalVar.playerAction = 'actionWaiting'
		currentDisplay = currentBoard
		globalVar.currentTextBox = currentDisplay.decorList[-1]
		if not globalVar.persoMain.pokemonsAlive():
			globalVar.currentTextBox.write('Vous avez perdu', (255,255,0))
		else:
			globalVar.currentTextBox.write('Vous avez gagné', (255,255,0))
			gain = random.randint(1,50)
			globalVar.persoMain.money += gain
			globalVar.currentTextBox.write(str(gain)+' poke$', (255,255,0))


	# --- ------------------------------------------- ---
	# ---             GESTION DE L AFFICHAGE          ---
	# ---                                             ---
	# - Re-collage -
	#screen.fill((0,0,0,0))
	screen.blit(currentDisplay.fond, (0,0))

	# - Ajout de tous les elements de l'ecran -
	for item in currentDisplay.decorList:
		screen.blit(item.surf, item.position)

	# - Affichage du personnage sur l'ecran -
	#if globalVar.gameStatus == 'boardStatus':
	screen.blit(currentDisplay.perso.surf, currentDisplay.perso.position)
	
	# - Rafraichissement -
	pygame.display.flip()
	

	# --- ------------------------------------------- ---
	# ---           GESTION DE ENTRE CLAVIER          ---
	# ---                                             ---
	for event in pygame.event.get(): # On parcours la liste de tous les événements reçus
		keys = pygame.key.get_pressed()
		# --- EXIT ---
		if event.type == QUIT or (event.type == KEYDOWN and keys[pygame.K_F4] and keys[pygame.K_LALT]):
			globalVar.gameStatus = 'closing'
			done = 1 # On arrête la boucle

		# --- EVENT SUR PLATEAU ---
		if (globalVar.gameStatus == 'boardStatus' or globalVar.gameStatus == 'currentEncounterStatus' or globalVar.gameStatus == 'infoStatus')  and event.type == KEYDOWN:
			#if event.type == KEYDOWN: # and globalVar.gameStatus == 'boardStatus':
			if event.key == move_right:
				currentDisplay.perso.deplacer('droite', keys[courir], currentDisplay.collisionList, currentDisplay.interactionListArea, currentDisplay.interactionObjectListArea)
			if event.key == move_left:
				currentDisplay.perso.deplacer('gauche', keys[courir], currentDisplay.collisionList, currentDisplay.interactionListArea, currentDisplay.interactionObjectListArea)
			if event.key == move_bottom:
				currentDisplay.perso.deplacer('bas', keys[courir], currentDisplay.collisionList, currentDisplay.interactionListArea, currentDisplay.interactionObjectListArea)
			if event.key == move_top:
				currentDisplay.perso.deplacer('haut', keys[courir], currentDisplay.collisionList, currentDisplay.interactionListArea, currentDisplay.interactionObjectListArea)
			if event.key == fuire_combat:
				globalVar.gameStatus = 'boardStatus'
			if event.key == interact:
				currentDisplay.perso.interact(currentDisplay.interactionListArea, currentDisplay.interactionObjectListArea)
			if event.key == info_key:
				currentDisplay = PokedexBean()
				globalVar.gameStatus = 'infoStatus'

		if event.type == KEYDOWN and event.key == K_h:
			print('Game Status : '+ globalVar.gameStatus)
			print('Position : '+ str(currentDisplay.perso.position))
			print('Pokemon player : '+ str(globalVar.persoMain.pokemons))
			print('Inventory player : '+ str(globalVar.persoMain.inventory))
	
	clock.tick(fps_max) # default is 60 FPS

