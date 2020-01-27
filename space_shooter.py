import pygame
import constants as consts
from sound import Sound
import game

pygame.init()
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))


sound = Sound()
sound.main_theme()
clock = pygame.time.Clock()
running = True
game = game.Game(screen, sound, clock, running)

while running:
    running = game.run()
pygame.quit()
