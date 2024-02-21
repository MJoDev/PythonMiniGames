import pygame
from pygame.sprite import Group
import random

Widht = 800
Height = 600

Black = (25, 26, 22)
White = (231, 232, 230)
Red = (161, 47, 47)
RedWine = (158, 47, 47)
Green = (40, 102, 47)
Blue = (41, 86, 135)


class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship/assets/UFO.png")

        self.rect = self.image.get_rect()

        self.rect.center = (200, 500)

        # Spawn
        self.rect.x = random.randrange(Widht - self.rect.width)
        self.rect.y = random.randrange(300 - self.rect.height)

        # Movement
        self.velocity_x = random.randrange(1,10)
        self.velocity_y = random.randrange(1,10)
    
    def update(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        # Border
        if self.rect.left < 0:
            self.velocity_x += 1
        if self.rect.right > Widht:
            self.velocity_x -= 1

        if self.rect.bottom > Height:
            self.velocity_y -=1
        if self.rect.top < 0:
            self.velocity_y +=1