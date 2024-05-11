import pygame 
import random 
import enum
from  collections import namedtuple

pygame.init()

BLOCK_SIZE = 20

Coord = namedtuple('Coord', 'x', 'y')

class SnakeyDirection(enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4



class SnakeySnake():

    def __init__(self, width = 640, height = 480):
        self.width = width
        self.height = height

        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock() #Control speed of the game.
        pygame.display.set_caption("Roger") #Screen caption.

        #Define the state of the game
        self.direction = SnakeyDirection.RIGHT
        self.head = Coord(self.width/2, self.height/2)
        self.snake = [self.head, Coord(self.head.x-BLOCK_SIZE, self.head.y), Coord(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.food = None
        self.giveFood()

#Funtion to give food at random coordinates on the window after snake has eaten the damn thing
def giveFood(self):
    x = random.randint(0, (self.width-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
    y = random.randint(0, (self.height-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
    self.food = Coord(x,y)
    if self.food in self.snake: #Check to see of the coordinate of the snake matches with the food
        self.giveFood()

if __name__ == '__main__':
    game = SnakeySnake()
    
    #MAIN GAME LOOP
    while True:
        pass

pygame.quit()