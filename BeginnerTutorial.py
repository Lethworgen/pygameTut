import pygame, sys
from pygame.locals import *
import random

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

# Asign FPS a value
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
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


# Defining the enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center=(random.randint(40, 360), 0))

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Defining the Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect()

    def update(self):
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

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()

    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)