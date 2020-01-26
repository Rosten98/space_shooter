import pygame
import constants as consts
from player import Player
from enemy import Enemy
from sound import Sound
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def draw_background():
    background = pygame.image.load(consts.BG_BLUE).convert()
    bg_w = background.get_width()
    bg_h = background.get_height()

    # Calculate size of the screen and draw as many backgrounds as needed
    for idx in range(round(consts.SCREEN_WIDTH / bg_w + 1 )):
        x = 0 + bg_w * idx
        screen.blit(background, (x, 0))
        for idx in range(round(consts.SCREEN_HEIGHT / bg_h + 1)):
            y = 0 + bg_h * idx
            screen.blit(background, (x, y))


def draw_bullet_counter():
    bullets_img = pygame.image.load(consts.PLAYER_BULLET1)
    x = pygame.image.load(consts.X)
    number = pygame.image.load(consts.NUMBERS[player.total_bullets])
    bullets_img = pygame.transform.scale(bullets_img, (bullets_img.get_width(), 40))
    # textsurface = pygame.font.Font(consts.FONT, 25).render(str(player.total_bullets), False, (255, 255, 255))
    # screen.blit(textsurface,(40,5))

    screen.blit(bullets_img, (0, 0))
    screen.blit(x, (15, 10))
    screen.blit(number, (40, 10))

def draw_lives_counter():
    player_life = pygame.image.load(consts.PLAYER_SHIP3_LIFE)
    x = pygame.image.load(consts.X)
    number = pygame.image.load(consts.NUMBERS[player.lives])

    screen.blit(player_life, (100, 10))
    screen.blit(x, (140, 10))
    screen.blit(number, (165, 10))


pygame.init()
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)

player = Player()
enemies = []
sound = Sound()
sound.main_theme()
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
    draw_background()
    draw_bullet_counter()
    draw_lives_counter()
    # Get last pressed key event
    pressed_keys = pygame.key.get_pressed()

    # Update position of player, enemies and bullets
    player.update(pressed_keys)

    for bullet in player.bullets:
        bullet.update(player.rect.copy(), player.surf.get_size())
        screen.blit(bullet.surf, bullet.rect)

    screen.blit(player.surf, player.rect)

    for enemy in enemies:
        enemy.update()
        screen.blit(enemy.surf, enemy.rect)

    # Check collisions with enemies
    for enemy in enemies:
        if pygame.sprite.collide_mask(player, enemy):
            if player.lives > 0:
                sound.live_down()
                enemy.rect.move_ip((0, -1000))
                player.lives -= 1
            else:
                player.kill()
                running = False
        for bullet in player.bullets:
            if pygame.sprite.collide_mask(bullet, enemy):
                sound.explosion()
                enemy.rect.move_ip((0, -1000))
                bullet.rect.move_ip((0, -1000))
                enemy.kill()
                bullet.kill()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
