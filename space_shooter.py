import pygame, sys
from pygame.locals import *

import constants as consts
from sound import Sound
from game import Game

pygame.init()
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

# sound = Sound()
clock = pygame.time.Clock()

# game = Game(screen, sound, clock)
font = pygame.font.SysFont(consts.FONT, 30)

def draw_text(text, font, color, surface, position):
    text = font.render(text, 1, color)
    text_rect = text.get_rect()
    text_rect.center = position
    surface.blit(text, text_rect)

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
def main_menu():
    running = True
    btn_1 = pygame.image.load(consts.BTN_BLUE)
    btn_2 = pygame.image.load(consts.BTN_RED)
    btn_2_rect = btn_2.get_rect()
    btn_1_rect = btn_1.get_rect()
    btn_1_rect.center = (screen.get_width() / 2, screen.get_height() / 2 - 100)
    btn_2_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
    click = False

    while running:
        screen.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()
        if btn_1_rect.collidepoint((mx, my)):
            if click:
                sound = Sound()
                sound.main_theme()

                game = Game(screen, sound, clock)
                game.run()
        if btn_2_rect.collidepoint((mx, my)):
            if click:
                running = False

        draw_background()
        screen.blit(btn_1, btn_1_rect)
        screen.blit(btn_2, btn_2_rect)
        draw_text('Main Menu', font, (255,255,255), screen, (screen.get_width() / 2, screen.get_height() / 2 - 180))
        draw_text('Start', font, (0, 0, 0), screen, (btn_1_rect.centerx, btn_1_rect.centery))
        draw_text('Exit', font, (0, 0, 0), screen, (btn_2_rect.centerx, btn_2_rect.centery))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


main_menu()
pygame.quit()
sys.exit()
