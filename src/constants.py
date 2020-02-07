# -*- coding: utf-8 -*-
from pygame.locals import * # Import des constante de Pygame
"""Constantes du jeu PyPoke"""

# Paramètres de la fenêtre
windows_size = (768, 480)
windows_title = 'PyPoke [EPSI-Python]'
icone_image = '../Images/ico.jpg'
fps_max = 60

# Paramètres du jeu
walk_speed = 3
run_speed = 6
combat_chance = 20 # On a une chance sur combat_chance de declancher un combat
display_delay = 3

# Paramètres de l'affichage
perso_size = 32
perso_size_tuple = (perso_size,perso_size)
perso_scale = (128,128)
hit_box = False

# Zone en fonction du plateau
areaType = {1:'mountain',2:'field',3:'pond',4:'field',5:'field',6:'field',7:'foret',8:'field',9:'sea'}

# Listes des images du jeu
accueil_image = '../Images/background.jpg'
fond_image = '../Images/background.jpg'
fondNoir_image = '../Images/fond_noir.jpg'
fondgrass_image = '../Images/backgroundGrass.png'
perso_sprite = '../Images/SpritePerso.png'
pin_sprite = '../Images/pinIcon2.png'
dresseur1_sprite = '../Images/SpriteDresseur1.png'
dresseur2_sprite = '../Images/SpriteDresseur2.png'
dresseur3_sprite = '../Images/SpriteDresseur3.png'
arbre_image = '../Images/ElementDecor5.png'
arbreDouble_image = '../Images/ElementDecor5.png'
maison_image = '../Images/ElementDecor4.png'
maison2_image = '../Images/ElementDecor4.png'
maison3_image = '../Images/ElementDecor4.png'
centrePokemon_image = '../Images/ElementDecor4.png'
market_image = '../Images/ElementDecor4.png'
hauteHerbe_image = '../Images/ElementDecor4.png'
barriere_image = '../Images/ElementDecor5.png'
dirt_image = '../Images/ElementDecor4.png'
road_image = '../Images/ElementDecor4.png'
route_image = '../Images/ElementDecor4.png'
grass_image = '../Images/ElementDecor4.png'
tas_image = '../Images/ElementDecor5.png'
eau_image = '../Images/ElementDecor5.png'
combat_image = '../Images/CombatBackground.png'
pokeball_image = '../Images/PokeBall.png'

# Touches, /!\ Pygame est en qwerty /!\
move_right = K_d
move_left = K_a
move_bottom = K_s
move_top = K_w
courir = K_LALT
interact = K_e
hit_box_show = K_h
fuire_combat = K_SPACE
info_key = K_i

def hitBox(surface, border=6):
    surface.fill(Color(20, 20, 244))
    surface.fill(Color(244, 20, 20), surface.get_rect().inflate(-border, -border))