import pygame
import random
import constants as consts
from player import Player
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE
)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load('./assets/meteorBrown_big1.png')
        self.rect = self.surf.get_rect(
            center=(
                random.randint(consts.SCREEN_WIDTH + 20, consts.SCREEN_WIDTH + 100),
                random.randint(0, consts.SCREEN_HEIGHT),
            )
        )
        self.mask = pygame.mask.from_surface(self.surf)
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        screen.blit(self.surf, self.rect)
        # self.mask = pygame.mask.from_surface(self.surf)

def drawBackground():
    background = pygame.image.load('./assets/blue.png').convert()
    bg_w = background.get_width()
    bg_h = background.get_height()

    for idx in range(round(consts.SCREEN_WIDTH / bg_w + 1 )):
        x = 0 + bg_w * idx
        screen.blit(background, (x, 0))
        for idx in range(round(consts.SCREEN_HEIGHT / bg_h + 1)):
            y = 0 + bg_h * idx
            screen.blit(background, (x, y))

pygame.init()
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instantiate player. Right now, this is just a rectangle.
player = Player()
enemies = []

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.append(new_enemy)

    screen.fill((0, 0, 0))
    drawBackground()

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)
    screen.blit(player.surf, player.rect)

    for enemy in enemies:
        enemy.update()

    for enemy in enemies:
        if pygame.sprite.collide_mask(player, enemy):
            player.kill()
            running = False

    pygame.display.flip()
    clock.tick(30)
