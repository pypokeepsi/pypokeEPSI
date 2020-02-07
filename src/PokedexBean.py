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

class TextBoxContainer:
	def __init__(self):
		self.decorList = []
		textBoxBackGroung = TextBoxBackGroung()
		textBox = TextBox()
		self.decorList.extend([textBoxBackGroung,textBox])

class TextBox:
	def __init__(self):
		self.collisionType = 'empty'
		self.surf = pygame.Surface((312,235),pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(0, 0)
		self.surf.fill((218, 212, 227))
		globalVar.currentTextBox = self
		if hit_box:
			hitBox(self.surf)

	def write(self, text, color):
		font = pygame.font.SysFont('arial', 15, True)
		text = font.render(' - '+text, True, color)
		textRect = text.get_rect().move( 5, self.position[3])
		newsurf = pygame.Surface((self.surf.get_rect()[2],self.surf.get_rect()[3]+15),pygame.SRCALPHA, 32)
		self.position = self.position.move(0,-15)
		newsurf.fill((218, 212, 227))
		newsurf.blit(self.surf, self.position)
		newsurf.blit(text, textRect)
		self.surf = newsurf
		self.position = self.position.move(0,15)
		if hit_box:
			hitBox(self.surf)

class TextBoxBackGroung:
	def __init__(self):
		self.collisionType = 'empty'
		self.surf = pygame.Surface((318,250),pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(0, 0)
		self.surf.fill((253, 252, 250))
		if hit_box:
			hitBox(self.surf)


class MenuImageContainer:
	def __init__(self):
		self.decorList = []
		hrx = HR('x',0,250)
		hry = HR('y',318,0, (768,250))
		menuBackGround = MenuBackGround(0,255)
		menuPokeballBackGround = MenuPokeballBackGround(10,288)
		menuItemBackGround = MenuItemBackGround(173,288)
		menuPokemonBackGround = MenuPokemonBackGround(385,263)
		
		pokeballs = []
		for i in range(len(globalVar.persoMain.inventory['pokeball'])):
			pokeballs.append(PokeBallBean(globalVar.persoMain.inventory['pokeball'][i]))
		
		pokemons = []
		for i in range(len(globalVar.persoMain.pokemons)):
			pokemons.append(PokemonBallBean(globalVar.persoMain.pokemons[i],i))
		
		items = []
		for i in range(len(globalVar.persoMain.inventory['object'])):
			items.append(ItemBean(globalVar.persoMain.inventory['object'][i]))

		self.decorList.extend([hrx, hry, menuBackGround, menuPokeballBackGround, menuItemBackGround, menuPokemonBackGround])
		self.decorList.extend(pokeballs)
		self.decorList.extend(pokemons)
		self.decorList.extend(items)

class HR:
	def __init__(self, axe, x, y , size=(768,470)):
		self.collisionType = 'mur'
		if axe == 'x':
			self.surf = pygame.Surface((size[0],5),pygame.SRCALPHA, 32)
		else:
			self.surf = pygame.Surface((5,size[1]),pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(x, y)
		self.surf.fill((45, 37, 56))
		if hit_box:
			hitBox(self.surf)

class MenuBackGround:
	def __init__(self, x, y):
		self.collisionType = 'empty'
		self.surf = pygame.Surface((768,225),pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(x, y)
		self.surf.fill((253, 252, 250))

		RoundedRect(self.surf,(10, 8, 110, 25),(200,20,200), 'PokeBall', 1)
		RoundedRect(self.surf,(173, 8, 70, 25),(20,200,200), 'Item', 0.8)
		#RoundedRect(self.surf,(360, 20, 90, 25),(200,200,20), 'Attack', 0.9)
		if hit_box:
			hitBox(self.surf)

class MenuPokeballBackGround:
	def __init__(self, x, y):
		self.collisionType = 'empty'
		self.surf = pygame.Surface((150,180),pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(x, y)
		self.surf.fill((218, 212, 227))
		if hit_box:
			hitBox(self.surf)

class MenuItemBackGround:
	def __init__(self, x, y):
		self.collisionType = 'empty'
		self.surf = pygame.Surface((200,180),pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(x, y)
		self.surf.fill((218, 212, 227))
		if hit_box:
			hitBox(self.surf)

class MenuPokemonBackGround:
	def __init__(self, x, y):
		self.collisionType = 'empty'
		self.surf = pygame.Surface((372,39),pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(x, y)
		self.surf.fill((218, 212, 227))
		if hit_box:
			hitBox(self.surf)

class ItemBean:
	def __init__(self, item):
		switcher = {
			0:(183,298), 1:(248,298), 2:(313,298),
			3:(183,353), 4:(248,353),  5:(313,353),
			6:(183,408), 7:(248,408), 8:(313,408)
		}
		x = switcher.get(item['id'])[0]
		y = switcher.get(item['id'])[1]
		dimensionObjet = (50,50)
		self.collisionType = 'interact'
		self.collisionSpec = 'actif'
		self.surf = pygame.Surface(dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(x, y)
		size = (50, 50)
		radius = 18
		circleSurf = pygame.Surface(size).convert_alpha()
		circleSurf.fill(Color(128,0,128,0))
		pygame.draw.circle(circleSurf, (48, 48, 48), (radius, radius), radius)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( circleSurf, (5, 5))
		self.item = item
	def interact(self):
		if self.item['quantity'] > 0:
			globalVar.currentTextBox.write(self.item['name'], (50,50,50))
		else:
			globalVar.currentTextBox.write('Not enought', (134,134,134))

class PokemonBallBean:
	def __init__(self, pokemon, i):
		switcher = { 0:(400,270), 1:(450,270), 2:(500,270), 3:(550,270), 4:(600,270),  5:(650,270) }
		x = switcher.get(i)[0]
		y = switcher.get(i)[1]
		dimensionObjet = (39,39)
		self.collisionType = 'interact'
		self.collisionSpec = 'actif'
		self.surf = pygame.Surface(dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(x, y)
		size = (26, 26)
		radius = 13
		circleSurf = pygame.Surface(size).convert_alpha()
		circleSurf.fill(Color(128,0,128,0))
		pygame.draw.circle(circleSurf, (48, 48, 48), (radius, radius), radius)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( circleSurf, (0, 0))
		self.pokemon = pokemon
	def interact(self):
		
		globalVar.currentTextBox.write(self.pokemon.pokeData['name'], (50,50,50))
		

class PokeBallBean:
	def __init__(self, pokeball):
		switcher = {0:(20,310),1:(90,310),2:(20,380),3:(90,380)}
		x = switcher.get(pokeball['id'])[0]
		y = switcher.get(pokeball['id'])[1]

		pokeballCoordonate = (20,310)
		dimensionObjet = (60, 60)
		switcher = {0:(0,0,dimensionObjet[0],dimensionObjet[1]),1:(60,0,dimensionObjet[0],dimensionObjet[1]),2:(122,0,dimensionObjet[0],dimensionObjet[1]),3:(183,0,dimensionObjet[0],dimensionObjet[1])}
		imageCoordonate = switcher.get(pokeball['id'])
		self.collisionType = 'interact'
		self.collisionSpec = 'actif'
		image = pygame.image.load(pokeball_image).convert_alpha()
		self.surf = pygame.Surface(dimensionObjet,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(x, y)
		font = pygame.font.SysFont('arial', 15, True)
		text = font.render('x'+str(pokeball['quantity']), True, (48, 48, 48))
		textRect = text.get_rect().move(35,42)
		size = (60, 60)
		radius = 26
		circleSurf = pygame.Surface(size).convert_alpha()
		circleSurf.fill(Color(128,0,128,0))
		pygame.draw.circle(circleSurf, (48, 48, 48), (radius, radius), radius)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( circleSurf, (4, 4))
		if pokeball['quantity'] != 0:
			self.surf.blit( image, (2, 2), imageCoordonate)
			self.surf.blit( text, textRect)
		self.pokeball = pokeball

	def interact(self):
		if self.pokeball['quantity'] > 0:
			globalVar.currentTextBox.write(self.pokeball['name'], (50,50,50))
		else:
			globalVar.currentTextBox.write('Not enought', (134,134,134))

class PokemonImage:
	def __init__(self,x ,y, url, front = True):
		if front:
			sizeImage = (128,128)
		else:
			sizeImage = (128,90)
		self.collisionType = 'mur'
		image = io.BytesIO(urlopen(url).read())
		image = pygame.image.load(image).convert_alpha()
		self.surf = pygame.Surface(sizeImage,pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(x, y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( image, (0, 0) )

class MoneyBean:
	def __init__(self, x , y):
		self.collisionType = 'empty'
		font = pygame.font.SysFont('arial', 35)
		text = font.render(str(globalVar.persoMain.money)+' poke$', True, (48, 48, 48))
		textRect = text.get_rect()
		self.surf = pygame.Surface((150,70),pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect().move(x, y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( text, textRect )
		

class PokedexBean:
	def __init__(self):
		# Ajout du personnage
		self.perso = PersoBean(pin_sprite,450,290, True)
		self.decorList = []
		self.collisionList = []
		self.interactionListArea = []
		self.interactionObjectListArea = []
		# --- Recupere le fond de la fenetre ---
		self.fond = pygame.image.load(fond_image).convert()
		self.fond = pygame.transform.scale(self.fond, windows_size)

		# --- Recupere le container de l'affichage du combat ---
		menuImageContainer = MenuImageContainer()
		textBoxContainer = TextBoxContainer()
		#switcher = {0:(395,330),1:(575,330),2:(395,395),3:(575,395)}
		moneyBean = MoneyBean(450,330)
		# --- Recupere les attaques du pokemon allier sur le terrain ---
		# --- Ajout les elements graphique dans la liste des decors ---
		self.decorList.extend(textBoxContainer.decorList)
		self.decorList.extend(menuImageContainer.decorList)
		self.decorList.append(moneyBean)
		# --- Ajout les elements de collision dans la liste de collision ---
		for item in self.decorList:
			if item.collisionType == 'mur':
				self.collisionList.append(item.position)
		# --- Ajout des elements interactifs dans la liste interactives ---
		for item in self.decorList:
			if item.collisionType == 'interact':
				self.interactionListArea.append(item.position)
				self.interactionObjectListArea.append(item)



def RoundedRect(surface, rect, color, text, radius=0.4):
    font = pygame.font.SysFont('arial', 22, True)
    text = font.render(text, True, (232, 208, 208))
    textRect = text.get_rect()
    textRect.center = (rect[2] // 2 + rect[0], rect[3] // 2 + rect[1])
    rect         = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = pygame.Surface(rect.size,SRCALPHA)

    circle       = pygame.Surface([min(rect.size)*3]*2,SRCALPHA)
    pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)

    miniRect = pygame.Surface((rect[2], rect[3] // 2 + 1),SRCALPHA)
    pygame.draw.rect(miniRect,(0,0,0),miniRect.get_rect(),0)

    circle       = pygame.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)
    radius = rectangle.blit(circle,(0,0))
    radius.topright = rect.topright
    rectangle.blit(circle,radius)
    rectangle.blit(miniRect,(rect[0], rect[0] + rect[3] // 2))
    """
    radius.bottomright = rect.bottomright
    rectangle.blit(circle,radius)
    radius.bottomleft = rect.bottomleft
    rectangle.blit(circle,radius)
	"""
    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)
    surface.blit(rectangle,pos)
    surface.blit( text, textRect )
    return surface
