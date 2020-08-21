import pygame
from pygame.sprite import Sprite


class Snake(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.rect = pygame.Rect(0, 0, self.settings.piece_width, self.settings.piece_height)
        self.rect.center = self.screen_rect.center

        self.y = float(self.rect.y - self.rect.y % 20)
        self.x = float(self.rect.x - self.rect.x % 20)

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def blit_me(self):
        pygame.draw.rect(self.screen, self.settings.snake_color, self.rect)

    def update(self):
        if self.moving_up:
            self.y -= self.settings.snake_speed
        elif self.moving_down:
            self.y += self.settings.snake_speed
        elif self.moving_left:
            self.x -= self.settings.snake_speed
        elif self.moving_right:
            self.x += self.settings.snake_speed

        self.rect.x = self.x
        self.rect.y = self.y
