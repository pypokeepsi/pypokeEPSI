# -*- coding: utf-8 -*-
import pygame # Import de Pygame
from pygame.locals import * # Import des constante de Pygame
from constants import *
from BusinessObject import *
from random import *
import globalVar

class PersoBean:
	""" Classe permettant de créer un personnage """
	def __init__(self, sprite, x, y, pin = False):
		# --- Sprites du personnage ---
		self.perso=None
		# Chargement de l'image et prise en compte de la transparence
		self.imagePerso = pygame.image.load(sprite).convert_alpha()
		# Redimensionnement de l'image
		if not pin:
			self.imagePerso = pygame.transform.scale(self.imagePerso, perso_scale)

		# Direction sur le sprite
		if not pin:
			self.right = (0, perso_size * 2 , perso_size, perso_size * 3)
			self.left = (0, perso_size, perso_size, perso_size * 2)
			self.top = (0, perso_size * 3, perso_size, perso_size * 4)
			self.bottom = (0, 0, perso_size, perso_size)
		else:
			self.right = self.left = self.top = self.bottom = (0, 0, 50, 90)
		# Direction par défaut
		self.direction = self.bottom

		# Position du personnage en pixels
		self.x = x
		self.y = y
		
		# Surface utiliser pour afficher le personnage
		if not pin:
			self.surf = pygame.Surface(perso_size_tuple, pygame.SRCALPHA, 32)
		else:
			self.surf = pygame.Surface((32,40), pygame.SRCALPHA, 32)
		self.position = self.surf.get_rect()
		self.position = self.position.move(self.x, self.y)
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( self.imagePerso, (0, 0), self.direction)
		if not pin:
			self.persoSize = perso_size
		else:
			self.persoSize = 40
		self.pin = pin

	def deplacer(self, direction, courir, collisionList, interactionListArea, interactionObjectListArea):
		# --- Déplacement ---
		# Déplacement vers la droite
		move_speed = walk_speed
		if not self.pin:
			inflateValueX = -16
			inflateValueY = -16
		else:
			inflateValueX = 1
			inflateValueY = 1
		
		if courir:
			move_speed = run_speed
		if self.pin:
			move_speed = run_speed*5

		if direction == 'droite':
			# Pour ne pas dépasser l'écran
			self.direction = self.right
			if self.x + (self.persoSize - 1) < windows_size[0] and self.position.move(move_speed, 0).inflate(inflateValueX, inflateValueY).move(0,5).collidelist(collisionList) == -1:
				self.x += move_speed
				self.position = self.position.move(move_speed, 0)
		# Déplacement vers la gauche
		if direction == 'gauche':
			self.direction = self.left
			if self.x > 0 and self.position.move(-1*move_speed, 0).inflate(inflateValueX, inflateValueY).move(0,5).collidelist(collisionList) == -1:
				self.x -= move_speed
				self.position = self.position.move(-1*move_speed, 0)
		# Déplacement vers le haut
		if direction == 'haut':
			self.direction = self.top
			if self.y > 0 and self.position.move(0,move_speed * -1).inflate(inflateValueX, inflateValueY).move(0,5).collidelist(collisionList) == -1:
				self.y -= move_speed
				self.position = self.position.move(0,move_speed* -1)
		# Déplacement vers le bas
		if direction == 'bas':
			self.direction = self.bottom
			if self.y + (self.persoSize + 5) < windows_size[1] and self.position.move(0,move_speed).inflate(inflateValueX, inflateValueY).move(0,5).collidelist(collisionList) == -1:
				self.y += move_speed
				self.position = self.position.move(0,move_speed)
		# Verifie que le joueur ne se trouve pas sur une zone d'interaction passive
		indexItemInteract = self.position.inflate(-16, -16).move(0,5).collidelist(interactionListArea)
		if indexItemInteract != -1:
			if interactionObjectListArea[indexItemInteract].collisionSpec == 'passif':
				interactionObjectListArea[indexItemInteract].interact()
		# Collage sur la surface
		self.surf.fill((0,0,0,0))
		if hit_box:
			hitBox(self.surf)
		self.surf.blit( self.imagePerso, (0, 0), self.direction)

	def interact(self, interactionListArea, interactionObjectListArea):
		indexItemInteract = self.position.inflate(-16, -16).move(0,5).collidelist(interactionListArea)
		if indexItemInteract != -1:
			if interactionObjectListArea[indexItemInteract].collisionSpec == 'actif':
				interactionObjectListArea[indexItemInteract].interact()

""" DEPACEMENT AVEC colliderect()
collisionList = [arbre, maison, centrePokemon]
collisionTest = False
if event.key == move_left:
	for i in collisionList:
		if perso.position.colliderect(i.position):
			print(' --- ---')
			print(centrePokemon.position)
			print(perso.position)
			print(' --- ---')
			collisionTest = True
	if not collisionTest:
		perso.deplacer('gauche', keys[courir])
"""