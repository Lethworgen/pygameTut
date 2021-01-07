import pygame, sys
from pygame.locals import *
import random, time

# Game Loop Skeleton
# Changes in the game are not implemented until display.update() has been called
"""
while True:
    # Code
    # Code
    .
    .
    pygame.display.update()
"""

# Quitting Game Loop Example
# Call pygame.quit() and sys.exit() to close the window
"""
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
"""
# Initalizing a program
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Setting up Color objects. RGB
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup a 400x600 pixel display with caption
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


# Defining the enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30,370), 0)


# Defining the Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect(center = (150, 550))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
#        if pressed_keys[K_UP]:
#            self.rect.move_ip(0, -5)
#        if pressed_keys[K_DOWN]:
#            self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# Setting up Sprites
P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
"""
Creates groups for sprites. A sprite group is like a classification.
It's much easier to deal with two or three groups rather than dozens
of sprites. Use the add() function to add a sprite to a group.
"""
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
"""
Pygame gives us the option to create custom events.
"""
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:

    #Cycles through all events occuring
    for event in pygame.event.get():
        if event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 2

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Collision Detection
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(RED)
        pygame.display.update()

        """
        A benefit of the grouping system allows us to call
        the move functions for all sprites and rewdraw them
        in just 3 lines of code. draw() functions removed from
        Player and Enemy class
        """
        for entity in all_sprites:

            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)