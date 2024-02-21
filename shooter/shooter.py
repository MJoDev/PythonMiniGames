import pygame


Width = 1200
Height = 600

class start():
    pygame.init()

screen = pygame.display.set_mode((Width, Height))
execute = True

while execute:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execute = False
            pygame.display.flip()