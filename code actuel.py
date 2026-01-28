import pygame as pg
import random
import sys 
# faire une boucle de jeu pas de return cheloux
# Initialiser pygame (permet de démarrer le code de pygame)
pg.init()

# Constantes en MAJ et ne vont jamais changer (définir les paramétres de l'interface graphique)
SCREEN_WIDTH = 750 # LARGEUR
SCREEN_HEIGHT = 750 # HAUTEUR 
CELL_SIZE = 25 # UNE CELLULE (un carré)
GRID_SIZE = SCREEN_WIDTH // CELL_SIZE # division entiére largeur(fenetre)//largeur d'une cellule 750//25 il y aura 30 cases
FPS = 10 # combien de fois par seconde la fenetre va s'actualiser , j'ai mit 10 fps car le serpent se déplace d'une case a la fois et a 60 il ira trop vite

# Couleurs (tuple de couleur avec les canneaux rgb)

SNAKE_COLOR  = (248, 168, 0)# couleur du serpent = jaune 
BACKGROUND_COLOR = (184, 56, 0) # couleur de  fond = noir un peu orrangé
APPLE_COLOR = (1, 252, 128) # couleur de la pomme = vert
BORDER_COLOR = (232, 168, 0) # couleur de la bordure = orange
SCORE_COLOR = (248, 252, 248) # couleur du score = blanc

# Creé l'interface graphique

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # on apelle pygame puis le module display et on en retire la fonction set.mode et on lui indique la taille de la fenetre
pg.display.set_caption("Snake") # initulé a la fenetre

font = pg.font.Font(None, 36) # la police sera de taille 36 et None ca veut dire qu'il prend pas un style de police particulières 

class Snake:
    def _init_(self):
        self.postions = [(5, 5), (4,5), (3,5)] # coordonnée du snake dans le plan il a une longueur de 3 sa tete et le premier tuple
        self.direction = (1,0) # direction du serpent (de gauche a droite)
        self.grow = False # attribut qui va changer
    
    def move(self): 
        head_x , head_y = self.positions[0] # coordonné de la téte du serpent le tuple (5,5)
        delta_x, delta_y = self.direction # la direction par défaut est la droite (1.0)
        new_head = (head_x + delta_x, head_y + delta_y)
    

    # Vérifier si il y a une colision sur une bordure ou avec lui meme

    
    
    









 



