import pygame
from pygame.sprite import Sprite


class Apple(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.rect = pygame.Rect(0, 0, self.settings.apple_width, self.settings.apple_height)
        self.image = pygame.image.load('images/apple.png')

    def draw_apple(self):
        self.screen.blit(self.image, self.rect)
