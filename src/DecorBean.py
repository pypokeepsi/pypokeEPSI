# -*- coding: utf-8 -*-
import pygame # Import de Pygame
from pygame.locals import * # Import des constante de Pygame
from constants import *
from random import *
import globalVar

# --- Decord Interactif ---
class MaisonBean:
	"""Classe permettant de créer une maison"""
	def __init__(self,x ,y):
		self.collisionType = 'mur'
		self.dimensionObjet = (95, 103)
		# Chargement de l'image et prise en compte de la transparence
		imageMaison = pygame.image.load(maison_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		imageMaisonCoordonate = (33, 108, 95, 103) 
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( imageMaison, (0, 0), imageMaisonCoordonate)

class Maison2Bean:
	"""Classe permettant de créer une maison"""
	def __init__(self,x ,y):
		self.collisionType = 'mur'
		self.dimensionObjet = (77, 90)
		# Chargement de l'image et prise en compte de la transparence
		image = pygame.image.load(maison2_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		imageCoordonate = (188, 350, self.dimensionObjet[0], self.dimensionObjet[1]) 
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( image, (0, 0), imageCoordonate)

class Maison3Bean:
	"""Classe permettant de créer une maison"""
	def __init__(self,x ,y):
		self.collisionType = 'mur'
		self.dimensionObjet = (75, 75)
		# Chargement de l'image et prise en compte de la transparence
		image = pygame.image.load(maison3_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		imageCoordonate = (45, 220, self.dimensionObjet[0], self.dimensionObjet[1]) 
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( image, (0, 0), imageCoordonate)

class CentrePokemonBean:
	"""Classe permettant de créer un arbre"""
	def __init__(self,x ,y):
		self.collisionType = 'mur'
		self.dimensionObjet = (84, 78)
		# Chargement de l'image et prise en compte de la transparence
		imageCentrePokemon = pygame.image.load(centrePokemon_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		imageCentrePokemonCoordonate = (51, 19, 84, 78)
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( imageCentrePokemon, (0, 0), imageCentrePokemonCoordonate)

class MarketBean:
	"""Classe permettant de créer un arbre"""
	def __init__(self,x ,y):
		self.collisionType = 'mur'
		self.dimensionObjet = (68, 59)
		# Chargement de l'image et prise en compte de la transparence
		image = pygame.image.load(market_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		imageCoordonate = (158, 30, self.dimensionObjet[0], self.dimensionObjet[1])
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( image, (0, 0), imageCoordonate)

# --- Decord Statique ---
class ArbreBean:
	"""Classe permettant de créer un arbre"""
	def __init__(self,x ,y):
		self.collisionType = 'mur'
		self.dimensionObjet = (38, 45)
		# Chargement de l'image et prise en compte de la transparence
		self.imageArbre = pygame.image.load(arbre_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		self.imageArbreCoordonate = (20, 4, 38, 45)
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( self.imageArbre, (0, 0), self.imageArbreCoordonate)

	def fill(self, nb_x, nb_y):
		self.surf = pygame.Surface((self.dimensionObjet[0]*nb_x,self.dimensionObjet[1]*nb_y),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb_x):
			for o in range(nb_y):
				self.surf.blit( self.imageArbre, (self.dimensionObjet[0]*i, self.dimensionObjet[1]*o), self.imageArbreCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		return self

class ArbreDoubleBean:
	"""Classe permettant de créer un arbre"""
	def __init__(self,x ,y):
		self.collisionType = 'mur'
		self.dimensionObjet = (68, 60)
		# Chargement de l'image et prise en compte de la transparence
		self.imageArbreDouble = pygame.image.load(arbreDouble_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		self.imageArbreDoubleCoordonate = (1622, 2, 68, 60)
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( self.imageArbreDouble, (0, 0), self.imageArbreDoubleCoordonate)

	def fill(self, nb_x, nb_y):
		self.surf = pygame.Surface((self.dimensionObjet[0]*nb_x,self.dimensionObjet[1]*nb_y/1.5+60),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb_x):
			for o in range(nb_y):
				self.surf.blit( self.imageArbreDouble, (self.dimensionObjet[0]*i, self.dimensionObjet[1]*o/1.5), self.imageArbreDoubleCoordonate)
			self.surf.blit( self.imageArbreDouble, (self.dimensionObjet[0]*i, self.dimensionObjet[1]*nb_y/1.5), self.imageArbreDoubleCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		return self

class TasBean:
	"""Classe permettant de créer un arbre"""
	def __init__(self,x ,y):
		self.collisionType = 'mur'
		self.dimensionObjet = (49, 49)
		# Chargement de l'image et prise en compte de la transparence
		self.image = pygame.image.load(tas_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		self.imageCoordonate = (303, 511, self.dimensionObjet[0], self.dimensionObjet[1])
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( self.image, (0, 0), self.imageCoordonate)

	def fill(self, nb_x, nb_y):
		self.surf = pygame.Surface((self.dimensionObjet[0]*nb_x,self.dimensionObjet[1]*nb_y),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb_x):
			for o in range(nb_y):
				self.surf.blit( self.image, (self.dimensionObjet[0]*i, self.dimensionObjet[1]*o), self.imageCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		return self

class HealAreaBean:
	def __init__(self,x ,y):
		self.collisionType = 'interact'
		self.collisionSpec = 'passif'
		self.dimensionObjet = (40,20)
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.fill(Color(20, 20, 80))
	def interact(self):
		globalVar.persoMain.healPokemons()
		globalVar.currentTextBox.write('Pokemons soignés', (255,255,0))



class ChangeArea:
	def __init__(self,x ,y):
		self.collisionType = 'interact'
		self.collisionSpec = 'passif'
		self.dimensionObjet = (40,20)
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.fill(Color(20, 20, 80))
	def interact(self):
		globalVar.gameStatus='newBroadStatus'
		globalVar.currentTextBox.write('Changement de zone', (255,255,0))



class HauteHerbeBean:
	"""Classe permettant de créer un arbre"""
	def __init__(self, x, y):
		self.collisionType = 'interact'
		self.collisionSpec = 'passif'
		self.dimensionObjet = (16, 16)
		# Chargement de l'image et prise en compte de la transparence
		self.imageHauteHerbe = pygame.image.load(hauteHerbe_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		self.imageHauteHerbeCoordonate = (98, 1025, 16, 16)
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( self.imageHauteHerbe, (0, 0), self.imageHauteHerbeCoordonate)

	def fill(self, nb_x, nb_y):
		self.surf = pygame.Surface((self.dimensionObjet[0]*nb_x,self.dimensionObjet[1]*nb_y),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb_x):
			for o in range(nb_y):
				self.surf.blit( self.imageHauteHerbe, (self.dimensionObjet[0]*i, self.dimensionObjet[1]*o), self.imageHauteHerbeCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		return self

	def interact(self):
		if randint(1,combat_chance) == 1:
			globalVar.gameStatus = 'startEncounterStatus'

class BarriereBean:
	"""Classe permettant de créer un arbre"""
	def __init__(self, x, y):
		self.collisionType = 'mur'
		self.dimensionObjet = (16, 16)
		# Chargement de l'image et prise en compte de la transparence
		self.imageBarriere = pygame.image.load(barriere_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		self.imageBarriereXCoordonate = (1192, 1025, 16, 16)
		self.imageBarriereYCoordonate = (1180, 1009, 16, 16)
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( self.imageBarriere, (0, 0), self.imageBarriereXCoordonate)

	def fillX(self, nb):
		self.surf = pygame.Surface((self.dimensionObjet[0]*nb,self.dimensionObjet[1]),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb):
			self.surf.blit( self.imageBarriere, (self.dimensionObjet[0]*i, 0), self.imageBarriereXCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		return self

	def fillY(self, nb):
		self.surf = pygame.Surface((self.dimensionObjet[0],self.dimensionObjet[1]*nb),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb):
			self.surf.blit( self.imageBarriere, (self.dimensionObjet[0]-16, self.dimensionObjet[1]*i), self.imageBarriereYCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		return self

class DirtLineBean:
	"""Classe permettant de créer un arbre"""
	def __init__(self, x, y):
		self.collisionType = 'mur'
		self.dimensionObjet = (16, 16)
		# Chargement de l'image et prise en compte de la transparence
		self.image = pygame.image.load(dirt_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		self.imageCoordonate = (251, 1147, self.dimensionObjet[0], self.dimensionObjet[1])
		self.imageXCoordonate = (251, 1164, self.dimensionObjet[0], self.dimensionObjet[1])
		self.imageXCornerCoordonate = (268, 1164, self.dimensionObjet[0], self.dimensionObjet[1])
		self.imageYCoordonate = (268, 1130, self.dimensionObjet[0], self.dimensionObjet[1])
		self.imageYCornerCoordonate = (268, 1147, self.dimensionObjet[0], self.dimensionObjet[1])
		self.imageYCornerTop1Coordonate = (299, 1124, self.dimensionObjet[0], self.dimensionObjet[1])
		self.imageYCornerTop2Coordonate = (299, 1140, self.dimensionObjet[0], self.dimensionObjet[1])

		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( self.image, (0, 0), self.imageXCoordonate)

	def fillX(self, nb):
		self.surf = pygame.Surface((self.dimensionObjet[0]*nb,self.dimensionObjet[1]),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb):
			self.surf.blit( self.image, (self.dimensionObjet[0]*i, 0), self.imageXCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		return self

	def fillY(self, nb):
		self.surf = pygame.Surface((self.dimensionObjet[0],self.dimensionObjet[1]*nb),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb-2):
			self.surf.blit( self.image, (0, self.dimensionObjet[1]*i), self.imageYCoordonate)
		self.surf.blit( self.image, (0, self.dimensionObjet[1]*nb-16), self.imageXCornerCoordonate)
		self.surf.blit( self.image, (0, self.dimensionObjet[1]*nb-32), self.imageYCornerCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		return self

	def fillYCorner(self, nb):
		self.surf = pygame.Surface((self.dimensionObjet[0],self.dimensionObjet[1]*nb),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb-3):
			self.surf.blit( self.image, (0, self.dimensionObjet[1]*(i+1)), self.imageYCoordonate)
		self.surf.blit( self.image, (0, self.dimensionObjet[1]*nb-16), self.imageXCornerCoordonate)
		self.surf.blit( self.image, (0, self.dimensionObjet[1]*nb-32), self.imageYCornerCoordonate)
		self.surf.blit( self.image, (0, 0), self.imageYCornerTop1Coordonate)
		self.surf.blit( self.image, (0, self.dimensionObjet[1]), self.imageYCornerTop2Coordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		return self

class DirtTopLineBean:
	"""Classe permettant de créer un arbre"""
	def __init__(self, x, y):
		self.collisionType = 'empty'
		self.dimensionObjet = (16, 16)
		# Chargement de l'image et prise en compte de la transparence
		self.image = pygame.image.load(dirt_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		self.imageCoordonate = (251, 1147, self.dimensionObjet[0], self.dimensionObjet[1])
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( self.image, (0, 0), self.imageCoordonate)

	def fillX(self, nb):
		self.surf = pygame.Surface((self.dimensionObjet[0]*nb,self.dimensionObjet[1]*2),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb):
			self.surf.blit( self.image, (self.dimensionObjet[0]*i, 0), self.imageCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		return self

	def fillY(self, nb):
		self.surf = pygame.Surface((self.dimensionObjet[0],self.dimensionObjet[1]*nb),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb):
			self.surf.blit( self.image, (self.dimensionObjet[0]-16, self.dimensionObjet[1]*i), self.imageCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		return self


class GrassBean:
	"""Classe permettant de créer un arbre"""
	def __init__(self,x ,y, nb_x, nb_y):
		self.collisionType = 'empty'
		self.dimensionObjet = (16, 16)
		# Chargement de l'image et prise en compte de la transparence
		self.image = pygame.image.load(grass_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		self.imageCoordonate = (149, 1025, 16, 16)
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface((self.dimensionObjet[0]*nb_x,self.dimensionObjet[1]*nb_y),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb_x):
			for o in range(nb_y):
				self.surf.blit( self.image, (self.dimensionObjet[0]*i, self.dimensionObjet[1]*o), self.imageCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)

class WaterBean:
	"""Classe permettant de créer un sol d'eau"""
	def __init__(self,x ,y):
		self.collisionType = 'mur'
		self.dimensionObjet = (16, 16)
		# Chargement de l'image et prise en compte de la transparence
		self.image = pygame.image.load(eau_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		self.imageCoordonate = (640, 420, self.dimensionObjet[0], self.dimensionObjet[1])
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface(self.dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( self.image, (0, 0), self.imageCoordonate)	

	def fill(self, nb_x, nb_y):
		self.surf = pygame.Surface((self.dimensionObjet[0]*nb_x,self.dimensionObjet[1]*nb_y),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb_x):
			for o in range(nb_y):
				self.surf.blit( self.image, (self.dimensionObjet[0]*i, self.dimensionObjet[1]*o), self.imageCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		return self

class RoadBean:
	"""Classe permettant de créer un arbre"""
	def __init__(self,x ,y, nb_x, nb_y):
		self.collisionType = 'empty'
		self.dimensionObjet = (16, 16)
		# Chargement de l'image et prise en compte de la transparence
		self.image = pygame.image.load(grass_image).convert_alpha()
		# Cordonnees de l'objet dans l'image
		self.imageBorderTopCoordonate = (103, 1129, 16, 16)
		self.imageCornerTopRightCoordonate = (120, 1129, 16, 16)
		self.imageCornerTopLeftCoordonate = (86, 1129, 16, 16)
		
		self.imageBorderBottomCoordonate = (103, 1163, 16, 16)
		self.imageCornerBottomRightCoordonate = (120, 1163, 16, 16)
		self.imageCornerBottomLeftCoordonate = (86, 1163, 16, 16)
		
		self.imageBorderRightCoordonate = (120, 1146, 16, 16)
		self.imageBorderLeftCoordonate = (86, 1146, 16, 16)
		self.imageCenterCoordonate = (103, 1146, 16, 16)
		# Position en pixels
		self.x = x
		self.y = y
		# Surface utiliser pour l'affichage
		self.surf = pygame.Surface((self.dimensionObjet[0]*nb_x,self.dimensionObjet[1]*nb_y),pygame.SRCALPHA, 32)
		if hit_box:
			hitBox(self.surf)
		for i in range(nb_x):
			for o in range(nb_y):
				self.surf.blit( self.image, (self.dimensionObjet[0]*i, self.dimensionObjet[1]*o), self.imageCenterCoordonate)
		for i in range(nb_x):
			self.surf.blit( self.image, (self.dimensionObjet[0]*i, self.dimensionObjet[1]-16), self.imageBorderTopCoordonate)
		for i in range(nb_x):
			self.surf.blit( self.image, (self.dimensionObjet[0]*i, self.dimensionObjet[1]*nb_y-16), self.imageBorderBottomCoordonate)	
		for o in range(nb_y):
			self.surf.blit( self.image, (self.dimensionObjet[0]-16, self.dimensionObjet[1]*o), self.imageBorderLeftCoordonate)
		for o in range(nb_y):
			self.surf.blit( self.image, (self.dimensionObjet[0]*nb_x-16, self.dimensionObjet[1]*o), self.imageBorderRightCoordonate)
		self.surf.blit( self.image, (self.dimensionObjet[0]-16, self.dimensionObjet[1]-16), self.imageCornerTopLeftCoordonate)
		self.surf.blit( self.image, (self.dimensionObjet[0]*nb_x-16, self.dimensionObjet[1]-16), self.imageCornerTopRightCoordonate)
		self.surf.blit( self.image, (self.dimensionObjet[0]-16, self.dimensionObjet[1]*nb_y-16), self.imageCornerBottomLeftCoordonate)
		self.surf.blit( self.image, (self.dimensionObjet[0]*nb_x-16, self.dimensionObjet[1]*nb_y-16), self.imageCornerBottomRightCoordonate)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
