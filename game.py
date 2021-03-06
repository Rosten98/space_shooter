import pygame
import constants as consts
from player import Player
from enemy import Enemy
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Game():
    def __init__(self, screen, sound, clock):
        self.screen = screen
        self.sound = sound
        self.clock = clock
        # self.time_elapsed = 0
        # self.last_time = self.time_elapsed
        self.difficulty = 500
        self.player = Player()
        self.enemies = []
        # Create a custom event for adding a new enemy
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, self.difficulty)

    def draw_background(self):
        background = pygame.image.load(consts.BG_BLUE).convert()
        bg_w = background.get_width()
        bg_h = background.get_height()

        # Calculate size of the screen and draw as many backgrounds as needed
        for idx in range(round(consts.SCREEN_WIDTH / bg_w + 1 )):
            x = 0 + bg_w * idx
            self.screen.blit(background, (x, 0))
            for idx in range(round(consts.SCREEN_HEIGHT / bg_h + 1)):
                y = 0 + bg_h * idx
                self.screen.blit(background, (x, y))


    def draw_bullet_counter(self):
        bullets_img = pygame.image.load(consts.PLAYER_BULLET1)
        x = pygame.image.load(consts.X)
        number = pygame.image.load(consts.NUMBERS[self.player.total_bullets])
        bullets_img = pygame.transform.scale(bullets_img, (bullets_img.get_width(), 40))
        # textsurface = pygame.font.Font(consts.FONT, 25).render(str(player.total_bullets), False, (255, 255, 255))
        # screen.blit(textsurface,(40,5))

        self.screen.blit(bullets_img, (0, 0))
        self.screen.blit(x, (15, 10))
        self.screen.blit(number, (40, 10))


    def draw_lives_counter(self):
        player_life = pygame.image.load(consts.PLAYER_SHIP3_LIFE)
        x = pygame.image.load(consts.X)
        number = pygame.image.load(consts.NUMBERS[self.player.lives])

        self.screen.blit(player_life, (100, 10))
        self.screen.blit(x, (140, 10))
        self.screen.blit(number, (165, 10))


    # def set_difficulty(self):
    #     self.time_elapsed = self.clock.get_time()
    #     print(self.time_elapsed)
    #     print(self.last_time)
    #     if self.last_time >= self.time_elapsed + 1000:
    #         self.last_time = self.time_elapsed
    #         if self.difficulty >= 100:
    #             self.difficulty -= 100
    #             pygame.time.set_timer(self.ADDENEMY, self.difficulty)


    def run(self):
        running = True
        while running:
            # Check events in game
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    self.sound.quit_mixer()
                    running = False
                elif event.type == self.ADDENEMY:
                    new_enemy = Enemy()
                    self.enemies.append(new_enemy)

            self.screen.fill((0, 0, 0))
            # Draw background image
            self.draw_background()

            # Get last pressed key event
            pressed_keys = pygame.key.get_pressed()

            # Update position of player, enemies and bullets
            self.player.update(pressed_keys)

            for bullet in self.player.bullets:
                bullet.update(self.player.rect.copy(), self.player.surf.get_size())
                self.screen.blit(bullet.surf, bullet.rect)

            self.screen.blit(self.player.surf, self.player.rect)

            for enemy in self.enemies:
                enemy.update()
                self.screen.blit(enemy.surf, enemy.rect)

            # Check collisions with enemies
            for enemy in self.enemies:
                if pygame.sprite.collide_mask(self.player, enemy):
                    if self.player.lives > 0:
                        self.sound.live_down()
                        enemy.rect.move_ip((0, -1000))
                        self.player.lives -= 1
                    else:
                        self.player.kill()
                        self.sound.quit_mixer()
                        running = False
                for bullet in self.player.bullets:
                    if pygame.sprite.collide_mask(bullet, enemy):
                        self.sound.explosion()
                        enemy.rect.move_ip((0, -1000))
                        bullet.rect.move_ip((0, -1000))
                        enemy.kill()
                        bullet.kill()

            pygame.draw.rect(self.screen, (0,0,0), (0,0, consts.SCREEN_WIDTH, 50))
            self.draw_bullet_counter()
            self.draw_lives_counter()

            pygame.display.flip()
            self.clock.tick(30)
            # self.set_difficulty()
