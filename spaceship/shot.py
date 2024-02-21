import pygame
from pygame.sprite import Group


Widht = 800
Height = 600

Black = (25, 26, 22)
White = (231, 232, 230)
Red = (161, 47, 47)
RedWine = (158, 47, 47)
Green = (40, 102, 47)
Blue = (41, 86, 135)

class shot (pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("spaceship/assets/shot.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y -=10

        if self.rect.bottom < 0:
            self.kill