import pygame
import constants as consts
from bullet import Bullet
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_LCTRL
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.transform.rotate(pygame.image.load('./assets/playerShip1_blue.png'), -90)
        self.rect = self.surf.get_rect()
        self.mask = pygame.mask.from_surface(self.surf)
        self.speed = 5
        self.total_bullets = 5
        self.bullets = [Bullet() for n in range(self.total_bullets)]

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect = self.rect.move(0, -self.speed)
            self.speed = 5
        if pressed_keys[K_DOWN]:
            self.rect = self.rect.move(0, self.speed)
            self.speed = 5
        if pressed_keys[K_LEFT]:
            self.rect = self.rect.move(-self.speed, 0)
            self.speed = 5
        if pressed_keys[K_RIGHT]:
            self.rect = self.rect.move(self.speed, 0)
            self.speed = 5
        if pressed_keys[K_SPACE]:
            # print(pressed_keys[K_SPACE])
            self.speed *= 3
        if pressed_keys[K_LCTRL]:
            if self.total_bullets > 0:
                self.bullets[self.total_bullets-1].enable_shooting()
                self.total_bullets -= 1;

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > consts.SCREEN_WIDTH:
            self.rect.right = consts.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= consts.SCREEN_HEIGHT:
            self.rect.bottom = consts.SCREEN_HEIGHT
