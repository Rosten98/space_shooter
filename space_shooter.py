import pygame, sys
from pygame.locals import *

import constants as consts
from sound import Sound
from game import Game

pygame.init()
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

sound = Sound()
clock = pygame.time.Clock()

game = Game(screen, sound, clock)
font = pygame.font.SysFont(consts.FONT, 30)

def draw_text(text, font, color, surface, x, y):
    text = font.render(text, 1, color)
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text, text_rect)


def main_menu():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('Main menu', font, (255,255,255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        btn_1 = pygame.Rect(50, 100, 200, 50)
        btn_2 = pygame.Rect(50, 200, 200, 50)

        if btn_1.collidepoint((mx, my)):
            if click:
                sound.main_theme()
                game.run()
        if btn_2.collidepoint((mx, my)):
            if click:
                running = False

        pygame.draw.rect(screen, (255, 0, 0), btn_1)
        pygame.draw.rect(screen, (255, 0, 0), btn_2)

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
