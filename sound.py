import pygame
import constants as consts

class Sound():
    def __init__(self):
        self.shot = pygame.mixer.Sound(consts.LASER1)
        self.live_down_sound = pygame.mixer.Sound(consts.LIVE_DOWN)


    def main_theme(self):
        self.main_theme = pygame.mixer.Sound(consts.MAIN_THEME)
        self.main_theme.play(-1)


    def shoot(self):
        self.shot.play(0)


    def live_down(self):
        self.live_down_sound.play(0)


    def explosion(self):
        # self.shot = pygame.mixer.Sound(consts.EXPLOSION)
        # self.shot.play(0)
        pass

    def quit_mixer(self):
        pygame.mixer.stop()
