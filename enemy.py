import pygame
import random
import constants as consts

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.enemy_meteor = random.randint(0, 4)
        self.surf = pygame.image.load(consts.METEORS[random.randint(0, 6)])
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
