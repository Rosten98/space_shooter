import pygame
import constants as consts
from player import Player
from enemy import Enemy

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

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
pygame.time.set_timer(ADDENEMY, 500)

player = Player()
enemies = []
clock = pygame.time.Clock()

running = True
while running:

    # Check events in game
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
    # Draw background image
    drawBackground()
    # Get last pressed key event
    pressed_keys = pygame.key.get_pressed()

    # Update position of player, enemies and bullets
    player.update(pressed_keys)
    screen.blit(player.surf, player.rect)

    for bullet in player.bullets:
        bullet.update(player.rect.copy())
        screen.blit(bullet.surf, bullet.rect)

    for enemy in enemies:
        enemy.update()
        screen.blit(enemy.surf, enemy.rect)

    # Check collisions with enemies
    for enemy in enemies:
        if pygame.sprite.collide_mask(player, enemy):
            player.kill()
            running = False
        # Add if to check collisions with bullets

    pygame.display.flip()
    clock.tick(30)
