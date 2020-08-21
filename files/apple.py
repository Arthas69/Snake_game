import pygame
from pygame.sprite import Sprite


class Apple(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.rect = pygame.Rect(0, 0, self.settings.apple_width, self.settings.apple_height)

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.apple_color, self.rect)
