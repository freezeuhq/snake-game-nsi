import pygame
import random
import sys 

# Initialiser pygame (permet de démarrer le code de pygame)
pygame.init()

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

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # on apelle pygame puis le module display et on en retire la fonction set.mode et on lui indique la taille de la fenetre
pygame.display.set_caption("Snake") # initulé a la fenetre

font = pygame.font.Font(None, 36) # la police sera de taille 36 et None ca veut dire qu'il prend pas un style de police particulières 

class Snake:
    def _init_(self):
        self.postions = [(5, 5), (4,5), (3,5)] # coordonnée du snake dans le plan il a une longueur de 3 sa tete et le premier tuple
        self.direction = (1,0) # direction du serpent (de droite a gauche)
        self.grow = False # attribut qui va changer
    
    def move(self): 
        head_x , head_y = self.positions[0] # coordonné de la téte du serpent le tuple (5,5)
        delta_x, delta_y = self.direction # la direction par défaut est la droite (1.0)
        new_head = (head_x + delta_x, head_y + delta_y)
    

    # Vérifier si il y a une colision sur une bordure ou avec lui meme
        if (
            new_head in self.positions or
            not (1 <= new_head[0] < GRID_SIZE - 1 and 1 <= new_head[1] < GRID_SIZE - 1)
        ):
            return False
        
        self.positions.insert(0, new_head)


        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False 

        return True 
    
    def change_direction(self, direction):
        
        opposite_direction = (-self.direction[0], -self.direction[1])
        if direction != opposite_direction:
            self.direction = direction 

    def grow_snake(self):
        self.grow = True 

    def draw(self, surface):
        for x, y in self.positions:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, SNAKE_COLOR, rect)


        #Ajouter des yeux au snake 
        head_x, head_y = self.positions[0]
        eye1 = pygame.Rect(head_x * CELL_SIZE + 8, head_y * CELL_SIZE + 8, 5, 5)
        eye2 = pygame.Rect(head_x * CELL_SIZE + 17, head_y *CELL_SIZE + 8, 5, 5)
        pygame.draw.rect(surface, (0, 0, 0), eye1)
        pygame.draw.rect(surface, (0, 0, 0), eye2)




class Apple:
    def __init__(self, snake): 
        self.position = self.random_position(snake)


        def random_position(self, snake):
            running = True 
            while running: 
                postion = (random.randint(1, GRID_SIZE))
    
    
    









 





    
    
    









 




