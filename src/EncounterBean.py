# -*- coding: utf-8 -*-
import pygame # Import de Pygame
from math import * # Import math function
from pygame.locals import * # Import des constante de Pygame
from constants import *
from PlayerBean import *
from DecorBean import *
from random import *
import globalVar
from EncounterContainers import *
import io
from urllib.request import urlopen
from PokeAPI import *
from datetime import datetime

class EncounterBean:
	"""Classe permettant de créer un combat sauvage"""
	def __init__(self, computer):
		# --- Initialisation des variables ---
		self.perso = PersoBean(pin_sprite,450,290, True)
		self.decorList = []
		self.collisionList = []
		self.interactionListArea = []
		self.interactionObjectListArea = []
		# --- Recupere le fond de la fenetre ---
		self.fond = pygame.image.load(fond_image).convert()
		self.fond = pygame.transform.scale(self.fond, windows_size)
		# --- Recupere le pokemon encore en vie dans la liste de CombatImageContainerpokemons du joueur ---
		self.persoPokemons = globalVar.persoMain.pokemons		
		self.computerPokemons = computer.pokemons		
		self.updateAll()

	def update(self):
		computerPokemonIndex = -1
		for i in reversed(range(len(self.computerPokemons))):
			if self.computerPokemons[i].isAlive():
				computerPokemonIndex = i	
		persoPokemonIndex = -1
		for i in reversed(range(len(self.persoPokemons))):
			if self.persoPokemons[i].isAlive():
				persoPokemonIndex = i
		attackList = []
		for i in range(len(self.persoPokemons[persoPokemonIndex].pokeData['attacks'])):
			attackList.append(AttackImage(self.persoPokemons[persoPokemonIndex].pokeData['attacks'][i], i))	
		combatImageContainer = CombatImageContainer(self.computerPokemons[computerPokemonIndex].pokeData)

		self.decorList.extend(combatImageContainer.decorList)
		self.decorList.extend(attackList)

	def updateAll(self):
		persoPokemonIndex = -1
		for i in reversed(range(len(self.persoPokemons))):
			if self.persoPokemons[i].isAlive():
				persoPokemonIndex = i
		# --- Recupere les pokemons du dresseur ou si le combat est un combat sauvage recupere un pokemon sauvage ---
		computerPokemonIndex = -1
		for i in reversed(range(len(self.computerPokemons))):
			if self.computerPokemons[i].isAlive():
				computerPokemonIndex = i
		
		# --- Recupere le container de l'affichage du combat ---
		combatImageContainer = CombatImageContainer(self.computerPokemons[computerPokemonIndex].pokeData)
		menuImageContainer = MenuImageContainer()
		textBoxContainer = TextBoxContainer()
		attackList = []

		# --- Recupere les attaques du pokemon allier sur le terrain ---
		for i in range(len(self.persoPokemons[persoPokemonIndex].pokeData['attacks'])):
			attackList.append(AttackImage(self.persoPokemons[persoPokemonIndex].pokeData['attacks'][i], i))

		# --- Ajout les elements graphique dans la liste des decors ---
		self.decorList.extend(combatImageContainer.decorList)
		self.decorList.extend(textBoxContainer.decorList)
		self.decorList.extend(menuImageContainer.decorList)
		#self.decorList.extend(textBoxContainer.decorList)
		self.decorList.extend(attackList)

		# --- Ajout les elements de collision dans la liste de collision ---
		for item in self.decorList:
			if item.collisionType == 'mur':
				self.collisionList.append(item.position)
		# --- Ajout des elements interactifs dans la liste interactives ---
		for item in self.decorList:
			if item.collisionType == 'interact':
				self.interactionListArea.append(item.position)
				self.interactionObjectListArea.append(item)


