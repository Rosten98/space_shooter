import pygame
import constants as consts

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load('./assets/laserBlue01.png')
        self.rect = self.surf.get_rect()
        self.mask = pygame.mask.from_surface(self.surf)
        self.position = ()
        self.shoot = False

    def update(self):
        if self.shoot:
            self.rect.move_ip(10, 0)

        if self.rect.left > consts.SCREEN_WIDTH:
            self.kill()

    def updateByShip(self, x, y):
            self.rect.move_ip = (x, y)

    def isShootin(self):
        self.shoot = True
