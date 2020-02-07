# Source : https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399995-gestion-des-evenements-1
# pip install pygame
import pygame # Import de Pygame
from pygame.locals import * # Import des constante de Pygame

# Initialisation de pygame
pygame.init()

# Creation d'une fenetre
fenetre = pygame.display.set_mode((640, 480))
# Pour rendre la fenetre redimensionnable
#fenetre = pygame.display.set_mode((640,480), RESIZABLE)

fond = pygame.image.load("background.jpg")
# convert() permet de simplifier le traitement de l'Image et rend l'affichage plus rapide
#fond = pygame.image.load("background.jpg").convert()

# Ajout de l'image dans la fenetre
fenetre.blit(fond, (0,0))
# Met a jour la fenetre
pygame.display.flip()

# Pour l'utilisation d'image avec de la transparence on utilise convert_alpha()
perso = pygame.image.load("perso.png").convert_alpha()
perso2 = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
perso2_x = 50
perso2_y = 50

fenetre.blit(perso, position_perso)
fenetre.blit(perso2, (perso2_x , perso2_y))
pygame.display.flip()

# Pour rendre une couleur transparente on utilise
#image.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent

# Permet de repeter une action quand une touche reste enfoncee set_repeat(DelaiDePriseEnCompte, DelaiEntreChaqueExecution)
pygame.key.set_repeat(400, 30)

# Gestion du son avec le module mixer
son = pygame.mixer.Sound("son.wav")
son.play()
#son.stop()

# Met en pause tous les sons
#pygame.mixer.pause()
# Sortir du mode pause
#pygame.mixer.unpause()
# Stoper tous les son
pygame.mixer.stop()
#son.fadeout(300) #Fondu à 300ms de la fin de l'objet "son"
#pygame.mixer.fadeout(300) #Fondu à 300ms de la fin de tous les objets Sound

# Gestion du son avec le module music
# Chargement du fichier
pygame.mixer.music.load("son.wav")
# Ajout de la musique a la queue
pygame.mixer.music.queue("son.wav")
# Lecture de la queue
pygame.mixer.music.play()
# Arret de la lecture
#pygame.mixer.music.stop()
# On peut utiliser les memes fonctions vu precedement
pygame.mixer.music.pause() #Met la musique en pause
pygame.mixer.music.unpause() #Reprend la musique là où elle a été coupée
pygame.mixer.music.fadeout(400) #Fondu à 400ms de la fin des musiques
# Gestion du volume
volume = pygame.mixer.music.get_volume() #Retourne la valeur du volume, entre 0 et 1
pygame.mixer.music.set_volume(0.5) #Met le volume à 0.5 (moitié)

# Gestion d'une mannette
#On compte les joysticks
nb_joysticks = pygame.joystick.get_count()
print("Il y a", nb_joysticks, "joystick(s) branché(s)")
#Et on en crée un s'il y a en au moins un
if nb_joysticks > 0:
	mon_joystick = pygame.joystick.Joystick(0)
	mon_joystick.init() #Initialisation
	# Caracteristique de la manette
	print("Axes :", mon_joystick.get_numaxes())
	print("Boutons :", mon_joystick.get_numbuttons())
	print("Trackballs :", mon_joystick.get_numballs())
	print("Hats :", mon_joystick.get_numhats())


# Clear l'ecran
#fenetre.fill((0, 0, 0))

# Fixer le fps
clock = pygame.time.Clock()

continuer = 1
#Boucle infinie
while continuer:

	#Re-collage
	fenetre.blit(fond, (0,0))	
	fenetre.blit(perso, position_perso)
	fenetre.blit(perso2, (perso2_x, perso2_y))
	#Rafraichissement
	pygame.display.flip()

	for event in pygame.event.get():   # On parcours la liste de tous les événements reçus
		if event.type == QUIT:     # Si un de ces événements est de type QUIT (Croix rouge haut gauche)
			continuer = 0      #On arrête la boucle
		# Event Clavier
		if event.type == KEYDOWN:
			# Lettres: K_a ... K_z
			# Nombres: K_0 ... K_9
			# Controles: K_TAB K_RETURN K_ESCAPE K_SCROLLOCK K_SYSREQ K_BREAK K_DELETE K_BACKSPACE K_CAPSLOCK K_CLEAR K_NUMLOCK
			# Ponctuation: K_SPACE K_PERIOD K_COMMA K_QUESTION K_AMPERSAND K_ASTERISK K_AT K_CARET K_BACKQUOTE K_DOLLAR K_EQUALS K_EURO K_EXCLAIM K_SLASH K_BACKSLASH K_COLON K_SEMICOLON K_QUOTE K_QUOTEDBL K_MINUS K_PLUS K_GREATER K_LESS 
			# Parenthèses:  K_RIGHTBRACKET K_LEFTBRACKET K_RIGHTPAREN K_LEFTPAREN
			# Touches F: K_F1 ... K_F15
			# Touches d'édition: K_HELP K_HOME K_END K_INSERT K_PRINT K_PAGEUP K_PAGEDOWN K_FIRST K_LAST
			# Clavier numérique: K_KP0 ... K_KP9 K_KP_DIVIDE K_KP_ENTER K_KP_EQUALS K_KP_MINUS K_KP_MULTIPLY K_KP_PERIOD K_KP_PLUS
			# SHF,CTL,ALT etc: K_LALT K_RALT K_LCTRL K_RCTRL K_LSUPER K_RSUPER K_LSHIFT K_RSHIFT K_RMETA K_LMETA
			# Flèches: K_LEFT K_UP K_RIGHT K_DOWN
			# Autres: K_MENU K_MODE K_PAUSE K_POWER K_UNDERSCORE K_HASH
			if event.key == K_SPACE:
				position_perso = position_perso.move(50, 50)
				print("La touche appuyée est Espace")

		# Event souris : MOUSEBUTTONDOWN MOUSEBUTTONUP MOUSEMOTION
		# event.button peut prendre les valeurs suivantes : 1 (bouton gauche) 2 (bouton milieu ou gauche+droite) 3 (bouton droite) 4 (molette haut) 5 (molette bas)
		# event.pos renvoie un tuple contenant l'abscisse et l'ordonnée à partir de l'angle haut-gauche
		# event.pos[0] = abscisse_clic et event.pos[1] = ordonnee_clic
		if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
			print("Zone dangereuse")
		
		# MOUSEMOTION possède 3 attributs : la nouvelle position (pos (nouvelle à chaque pixel de mouvement) le déplacement relatif (rel, le nombre de pixel de déplacement depuis la dernière position) les boutons pressés pendant le mouvement (buttons)
		# coordonnées x et y pour pos coordonnées x et y pour rel (gauche, milieu, droit) prenant pour valeur 0 (non pressé) ou 1 (pressé) pour buttons
		if event.type == MOUSEMOTION and event.buttons[0] == 1:
			print('Clique bouton haut gauche souris')
		
		# Deplacement d'une image au clic souris
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:	#Si clic gauche
				#On change les coordonnées du perso
				perso2_x = event.pos[0]
				perso2_y = event.pos[1]

		# Gestion des evenement manette
		if event.type == JOYBUTTONDOWN:
			print(event.button)
		if event.type == JOYAXISMOTION:
			if event.axis == 0 and event.value > 0:
				mouvement_droite()
			if event.axis == 0 and event.value < 0:
				mouvement_gauche()
		
		if event.type == ACTIVEEVENT:
			if event.gain == 1 and event.state == 1:
				print("Une souris est dans la fenêtre !! aaaah !!")

		if event.type == VIDEORESIZE:
			if event.w > 500 or event.h > 500:
					continue
					#continuer = 0
	# will block execution until 1/60 seconds have passed
    # since the previous time clock.tick was called.
    #clock.tick(60)









