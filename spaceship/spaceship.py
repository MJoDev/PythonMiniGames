import pygame
from enemy import enemy
from shot import shot
import random

#Window
Width = 800
Height = 600
FPS = 60

# Fonts
console = pygame.font.match_font('consolas')
Times = pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')

Black = (25, 26, 22)
White = (231, 232, 230)
Red = (161, 47, 47)
RedWine = (158, 47, 47)
Green = (40, 102, 47)
Blue = (41, 86, 135)





class player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        # Init player
        self.image = pygame.image.load("spaceship/assets/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)

        self.velocity_x = 0
        self.velocity_y = 0

        self.frequency = 300
        self.ultimate = pygame.time.get_ticks()

    def update(self):
        self.velocity_x = 0
        self.velocity_y = 0
        
        keys = pygame.key.get_pressed()

        # Movement
        if keys[pygame.K_a]:
            self.velocity_x = -10
        if keys[pygame.K_d]:
            self.velocity_x = 10
        if keys[pygame.K_s]:
            self.velocity_y = 10
        if keys[pygame.K_w]:
            self.velocity_y = -10        
        if keys[pygame.K_SPACE]:   
            time = pygame.time.get_ticks()
            if time - self.ultimate > self.frequency:
                self.ultimate = time
                self.shots()
                laser.play()
            

        # Update position
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y


        # Border
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.bottom > Height:
            self.rect.bottom = Height
        if self.rect.top < 0:
            self.rect.top = 0    
        
    def shots(self):
        bullet = shot(self.rect.centerx, self.rect.centery -30)
        Bullets.add(bullet)
        




# Init
class start():
    pygame.init()


# Sound
laser = pygame.mixer.Sound("spaceship/assets/shot.wav")
point = pygame.mixer.Sound("spaceship/assets/point.wav")
background_sound = pygame.mixer.Sound("spaceship/assets/background_sound.mp3")
pygame.mixer.music.set_volume(0.2)

background_sound.play()


# Screen set
screen = pygame.display.set_mode((Width, Height))

# Background
background = pygame.transform.scale(pygame.image.load("spaceship/assets/background.jpg").convert(), (1000,600))

# Title
pygame.display.set_caption("Spaceship")

clock = pygame.time.Clock()

# Player
Player = pygame.sprite.Group()
Players = player()
Player.add(Players)
Bullets = pygame.sprite.Group()

##  Score System
def text(screen, font, text, color, dimension, x,y):
    letter_type = pygame.font.Font(font, dimension)
    surface = letter_type.render(text, True, color)
    rectangle = surface.get_rect()
    rectangle.center = (x,y)
    screen.blit(surface, rectangle)


# Enemy
Enemys = pygame.sprite.Group()

score = 0
execute = True

while execute:

    clock.tick(FPS)

    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execute = False
    
    text(screen, Times, str(score).zfill(4), White, 50, 700, 50)


    Enemys.update()
    Player.update()
    Bullets.update()
    # Enemys generation
    if not Enemys:
        for x in range(random.randrange(1,5)): 
            enemys = enemy()
            Enemys.add(enemys)

    collision_spaceship = pygame.sprite.groupcollide(Enemys, Player, False, False)
    collision_bullet = pygame.sprite.groupcollide(Enemys, Bullets, True, True)

    if collision_spaceship:
        enemys.kill()
        score -= 10
    if collision_bullet:
        score += 10
        point.play()
    if score < - 10:
        break
    
    Player.draw(screen)
    Enemys.draw(screen)
    Bullets.draw(screen)

    pygame.display.flip()