import pygame 
import random 
import enum

pygame.init()


class SnakeyDirection(enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4



class SnakeySnake():

    def __inti__(self, width = 640, height = 480):
        self.width = width
        self.height = height

        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock() #Control speed of the game.
        pygame.display.set_caption("Roger") #Screen caption.

        #Define the state of the game
        self.direction = SnakeyDirection.RIGHT

if __name__ == '__main__':
    game = SnakeySnake()
    
    #MAIN GAME LOOP
    while True:
        pass

pygame.quit()