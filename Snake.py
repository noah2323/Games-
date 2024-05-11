import pygame
import random

pygame.init() #Pygame initalization

BLOCK_SIZE = 10
RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

class Snake_Game:
    def __init__(self, width = 800, height = 600):
        self.width = width
        self.height = height

        #Initalize the window for the game
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Roger')
        self.clock = pygame.time.Clock()

        #Inital game state. 
        self.drection = RIGHT

        self.head = (self.width/2, self.height/2)
        self.snake = [(self.head.x-BLOCK_SIZE, self.head.y), (self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.snack = 0
        self.giveSnack()

    def giveSnack(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE 
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = (x, y)
        if self.food in self.snake:
            self.giveSnack()

    def game_Play(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type


if __name__ == '__main__':
    game = Snake_Game()

    #Main game loop
    while True:
        pass

        if snake_dead == True:
            break

    print('Final Score:', score)

    pygame.quit()
