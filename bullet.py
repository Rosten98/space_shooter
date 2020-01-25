import pygame
import constants as consts

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = pygame.transform.rotate(pygame.image.load(consts.PLAYER_BULLET1), -90)
        self.size = self.surf.get_size()
        self.rect = self.surf.get_rect()
        self.mask = pygame.mask.from_surface(self.surf)
        self.shoot = False

    def update(self, position, player_size):
        y = 1
        position.y += player_size[y] / 2.0 - self.size[1]
        if self.shoot:
            self.rect.move_ip(13, 0)
            if self.rect.left > consts.SCREEN_WIDTH:
                self.kill()
        else:
            self.rect = position

    def enable_shooting(self):
        self.shoot = True
