# -*- coding: utf-8 -*-
import sys
import time
import pygame # Import de Pygame
from threading import Thread
from pygame.locals import * # Import des constante de Pygame

from PlayerBean import *
from DecorBean import *
from constants import *
import globalVar


# --- ------------------------------------------- ---
# --- AFFICHAGE DES NOTIFICATIONS POUR LE PLATEAU ---
# ---                                             ---
class DisplayNotif(Thread):
	queue = []
	running = False
	def __init__(self, surface):
		super().__init__()
		self.element = surface

	def addQueue(self, text, color):
		self.queue.append({'text':text,'color':color})
		# If thread is not running, start it
		if not self.running:
			self.__init__(self.element)
			self.start()

	def run(self):
		# Set thread as runnning
		self.running = True
		# Run thread while queue is not empty
		while(len(self.queue) > 0 and globalVar.gameStatus != 'closing'):
			item = self.queue.pop(0)
			text = self.element.font.render(str(item['text']), True, item['color'])
			textRect = text.get_rect()
			textRect.center = (self.element.position[2] // 2, self.element.position[3] // 2)
			
			text = self.element.font.render(str(item['text']), True, (item['color'][0],item['color'][1],item['color'][2] ,84))
			self.element.surf.fill((48,48,48,84))
			self.element.surf.blit(text,textRect)
			time.sleep(0.1)

			text = self.element.font.render(str(item['text']), True, (item['color'][0],item['color'][1],item['color'][2] ,192))
			self.element.surf.fill((48,48,48,192))
			self.element.surf.blit(text,textRect)
			time.sleep(0.1)

			text = self.element.font.render(str(item['text']), True, (item['color'][0],item['color'][1],item['color'][2] ,255))
			self.element.surf.fill(Color(48,48,48))
			self.element.surf.blit(text,textRect)
			time.sleep(display_delay)

			text = self.element.font.render(str(item['text']), True, (item['color'][0],item['color'][1],item['color'][2] ,192))
			self.element.surf.fill((48,48,48,192))
			self.element.surf.blit(text,textRect)
			time.sleep(0.1)
			
			text = self.element.font.render(str(item['text']), True, (item['color'][0],item['color'][1],item['color'][2] ,84))
			self.element.surf.fill((48,48,48,84))
			self.element.surf.blit(text,textRect)
			time.sleep(0.1)

			self.element.surf.fill(Color(0,0,0,0))

		# When queue is empty set thread as not running
		self.running = False

class NotificationBox:
	def __init__(self):
		self.collisionType = 'empty'
		dimensionObjet = (230,60)
		self.surf = pygame.Surface(dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(windows_size[0]-dimensionObjet[0], 5)
		self.font = pygame.font.SysFont('arial', 28, False)
		#self.surf.fill((150,48,100,1))
		globalVar.currentTextBox = self
		self.thread = DisplayNotif(self)
		if hit_box:
			hitBox(self.surf)

	def write(self, text, color):
		self.thread.addQueue(text, color)
		if hit_box:
			hitBox(self.surf)
# --- ------------------------------------------- ---
# ---          Gestion global des plateau         ---
# ---                                             ---
class Board:
	def __init__(self):
		# Ajout du personnage
		self.perso = PersoBean(perso_sprite,150,200)
		self.perso.perso = globalVar.persoMain
		self.notificationBox = NotificationBox()

# --- ------------------------------------------- ---
# ---              Gestion du plateau 8           ---
# ---                                             ---
class Board8(Board):
	"""Classe permettant de créer le plateau 8, plateau de depart"""
	def __init__(self):
		super().__init__()
		self.area = 'field'
		self.decorList = []
		self.collisionList = []
		self.interactionListArea = []
		self.interactionObjectListArea = []
		
		# --- Ajout Fond ---
		self.fond = pygame.image.load(fondgrass_image).convert()
		#self.fond = pygame.image.load(fondNoir_image).convert()
		self.fond = pygame.transform.scale(self.fond, windows_size)

		water = WaterBean(0,400).fill(30,5)
		water2 = WaterBean(461,336).fill(30,10)
		
		self.decorList.extend([water, water2])

		# --- Ajout Decors ---
		# - CHEMIN et ROUTE -
		# Ajout du chemin vertical
		roadVerti = RoadBean(210,-10,4,20)
		roadVertiDroite = RoadBean(524,95,4,11)
		roadHoriTop = RoadBean(278,155,15,3)
		roadHoriRight = RoadBean(592,220,9,3)
		self.decorList.extend([roadVerti,roadHoriTop,roadVertiDroite,roadHoriRight])

		# - HAUTE HERBE -
		# Ajout Haute Herbe en haut
		hauteHerbeTop = HauteHerbeBean(280,3).fill(9,7)
		# Ajout Haute Herbe maison haut droite
		hauteHerbeTopRight = HauteHerbeBean(685,95).fill(1,5)
		hauteHerbeTopLeft = HauteHerbeBean(140,3).fill(4,6)
		self.decorList.extend([hauteHerbeTop,hauteHerbeTopRight,hauteHerbeTopLeft])

		# - ARBRE ROCHER BARRIERE -
		# Ajout Arbres en haut a gauche
		arbreTopLeft = ArbreDoubleBean(-2,-10).fill(2,1)
		# Ajout Arbres a gauche
		arbreLeft = ArbreDoubleBean(-2,70).fill(1,6)
		# Ajout Arbres haut droite
		arbreTopRight = ArbreDoubleBean(430,-10).fill(5,1)
		# Ajout Arbres droite
		arbreRight = ArbreDoubleBean(702,70).fill(1,2)
		# Ajout Tas de Terre droite
		tasRight = TasBean(67,325).fill(2,1)
		# Ajout Ligne de terre en bas
		dirtLineXTop = DirtTopLineBean(0,384).fillX(28)
		dirtLineX = DirtLineBean(0,400).fillX(28)
		# Ajout Ligne de terre droite
		#dirtLineY = DirtLineBean(420,336).fillY(5)
		dirtLineY = DirtLineBean(445,304).fillYCorner(7)
		dirtLineXRightTop = DirtTopLineBean(461,304).fillX(20)
		dirtLineXRight = DirtLineBean(461,320).fillX(20)
		

		self.decorList.extend([arbreTopLeft, arbreLeft,arbreTopRight, arbreRight,tasRight,dirtLineXTop,dirtLineX,dirtLineY,dirtLineXRightTop,dirtLineXRight])

		# Ajout de barriere
		# Ajout de grass
		grassBarriereY = GrassBean(280,50,1,4)
		barriereYTopMid = BarriereBean(280,50).fillY(4)
		barriereXTopMid = BarriereBean(280,113).fillX(9)
		barriereXTopLeft = BarriereBean(125,95).fillX(5)
		barriereYTopLeft = BarriereBean(193,100).fillY(7)
		self.decorList.extend([grassBarriereY, barriereYTopMid, barriereXTopMid, barriereXTopLeft, barriereYTopLeft])

		# - BATIMENT -
		# Ajout Centre Pokemon
		centrePokemon = CentrePokemonBean(435,80)
		healAreaBean = HealAreaBean(460,150)
		# Ajout Maison haut droite
		maisonTopRight = MaisonBean(590,65)
		# Ajout Market
		market = MarketBean(450,200)
		# Ajout Maison2 gauche
		maison2 = Maison2Bean(67,65)
		# Ajout Maison3 milieu
		maison3 = Maison3Bean(360,200)
		self.decorList.extend([centrePokemon,maisonTopRight,market,maison2,maison3,healAreaBean])

		# - BONUS and Notification-


		changeArea = ChangeArea(250,2)
		self.decorList.extend([changeArea,self.notificationBox])




		for item in self.decorList:
			if item.collisionType == 'mur':
				self.collisionList.append(item.position)
		for item in self.decorList:
			if item.collisionType == 'interact':
				self.interactionListArea.append(item.position)
				self.interactionObjectListArea.append(item)








class Board5(Board):
	"""Classe permettant de créer le plateau 8, plateau de depart"""
	def __init__(self):
		super().__init__()
		self.area = 'foret'
		self.decorList = []
		self.collisionList = []
		self.interactionListArea = []
		self.interactionObjectListArea = []
		
		# --- Ajout Fond ---
		self.fond = pygame.image.load(fondgrass_image).convert()
		self.fond = pygame.transform.scale(self.fond, windows_size)

		# --- Ajout Decors ---
		# - CHEMIN et ROUTE -
		# Ajout du chemin vertical
		roadVerti = RoadBean(210,-10,4,35)
		roadHoriTop = RoadBean(278,155,25,3)
		self.decorList.extend([roadVerti,roadHoriTop])

		# - HAUTE HERBE -
		# Ajout Haute Herbe en haut
		hauteHerbeTop = HauteHerbeBean(280,3).fill(12,12)
		self.decorList.extend([hauteHerbeTop])

		# - ARBRE ROCHER BARRIERE -
		# Ajout Arbres en haut a gauche
		arbreTopLeft = ArbreDoubleBean(-2,-10).fill(2,2)
		# Ajout Arbres a gauche
		arbreLeft = ArbreDoubleBean(-2,70).fill(2,6)
		# Ajout Arbres haut droite
		arbreTopRight = ArbreDoubleBean(430,-10).fill(5,9)
		# Ajout Arbres droite
		arbreRight = ArbreDoubleBean(702,70).fill(1,2)
		
		self.decorList.extend([arbreTopLeft, arbreLeft,arbreTopRight, arbreRight])

		# - BATIMENT -
		
		# Ajout Maison haut droite
		maisonTopRight = MaisonBean(590,65)
		self.decorList.extend([maisonTopRight])

		# - BONUS and Notification-


		changeArea = ChangeArea(250,420)
		self.decorList.extend([changeArea,self.notificationBox])




		for item in self.decorList:
			if item.collisionType == 'mur':
				self.collisionList.append(item.position)
		for item in self.decorList:
			if item.collisionType == 'interact':
				self.interactionListArea.append(item.position)
				self.interactionObjectListArea.append(item)




"""
# Ajout Arbre
arbre = ArbreBean(450,320).fill(4,3)
# Ajout ArbreDouble
arbreDouble = ArbreDoubleBean(220,280).fill(3,4)
# Ajout Maison
maison = MaisonBean(0,0)
# Ajout Centre Pokemon
centrePokemon = CentrePokemonBean(250,0)
# Ajout Haute Herbe
hauteHerbe = HauteHerbeBean(500,200).fill(5,4)
# Ajout d'un chemin
road = RoadBean(500,50,9,7)
# Ajout de grass
grass = GrassBean(650,260,5,8)
# Ajout de barriere
barriereX = BarriereBean(100,300).fillX(5)
barriereY = BarriereBean(100,300).fillY(8)
"""
		