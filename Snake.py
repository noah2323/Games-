import pygame
import random
from collections import namedtuple
pygame.init() #Pygame initalization

Coord = namedtuple('Coord', 'x, y')

clock_speed = 20

BLOCK_SIZE = 20

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

font = pygame.font.SysFont('arial', 25)

class Snake_Game:
    def __init__(self, width = 800, height = 600):
        self.width = width
        self.height = height

        #Initalize the window for the game
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Roger')
        self.clock = pygame.time.Clock()

        #Inital game state. 
        self.direction = RIGHT

        self.head = Coord(self.width/2, self.height/2)
        self.snake = [self.head, Coord(self.head.x-BLOCK_SIZE, self.head.y), Coord(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.snack = 0
        self.giveSnack()

    def giveSnack(self):
        x = random.randint(0, (self.width-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE 
        y = random.randint(0, (self.height-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.snack = Coord(x, y)
        if self.snack in self.snake:
            self.giveSnack()

    def game_Play(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN: #Checks for a key press
                if event.key == pygame.K_LEFT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = UP
                elif event.key == pygame.K_DOWN:
                    self.direction = DOWN
        #Update the head of the snake
        self.Snake_movement(self.direction)
        self.snake.insert(0, self.head)
        #Check collision for game ending
        snake_dead = False
        if self.collision():
            snake_dead = True
            return snake_dead, self.score
        
        #Check if the coordinates of the food and the head match
        if self.head == self.snack:
            self.score +=1
            self.giveSnack() #Gives new snack
        else:
            self.snake.pop()

        #Updates the screen consistently
        self.update_screen()
        self.clock.tick(clock_speed)
        return snake_dead, self.score
    
    def collision(self):
        #Checks horizontal boundary in positive
        if self.head.x > self.width - BLOCK_SIZE: 
            return True
        #Checks vertical boundary in positive
        if self.head.y > self.height - BLOCK_SIZE:
            return True
        #Checks vertical and horizontal in negative
        if self.head.x < 0 or self.head.y < 0:
            return True
        #Checks if the snake ran into itself
        if self.head in self.snake[1:]:
            return True
        
        return False
    
    def update_screen(self):
        Green = (0, 255, 0)
        Black = (0, 0, 0)
        Red = (255, 0, 0)
        White = (255, 255, 255)

        self.window.fill(Black)#Makes the screen black
        for i in self.snake:
            #Draws the snake body with 3 segments on it.
            pygame.draw.rect(self.window, Green, pygame.Rect(i.x+3, i.y+3, BLOCK_SIZE, BLOCK_SIZE))

            pygame.draw.rect(self.window, Red, pygame.Rect(self.snack.x, self.snack.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render("Score: " + str(self.score), True, White)
        self.window.blit(text, [0,0])
        pygame.display.flip()

    def Snake_movement(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == RIGHT:
            x += BLOCK_SIZE
        elif direction == LEFT:
            x -= BLOCK_SIZE
        elif direction == DOWN:
            y += BLOCK_SIZE
        elif direction == UP:
            y -= BLOCK_SIZE
            
        self.head = Coord(x, y)

if __name__ == '__main__':
    game = Snake_Game()

    #Main game loop
    while True:
        snake_dead, score = game.game_Play()

        if snake_dead == True:
            break

    print('Final Score:', score)

    pygame.quit()
