import pygame
import constants as consts

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = pygame.transform.rotate(pygame.image.load('./assets/laserBlue01.png'), -90)
        self.rect = self.surf.get_rect()
        self.mask = pygame.mask.from_surface(self.surf)
        self.shoot = False

    def update(self, position):
        if self.shoot:
            self.rect.move_ip(5, 0)
            if self.rect.left > consts.SCREEN_WIDTH:
                self.kill()
        else:
            self.rect = position

    def enable_shooting(self):
        self.shoot = True
