import sys
from random import randint
from time import sleep

import pygame

from files.settings import Settings
from files.snake import Snake
from files.apple import Apple


class SnakeGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.settings = Settings()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Snake')

        self.snake = Snake(self)
        self.apples = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.snake.update()
            self._update_screen()
            sleep(0.5)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_DOWN:
            self.snake.moving_down = True
            self.snake.moving_up = False
            self.snake.moving_left = False
            self.snake.moving_right = False
        elif event.key == pygame.K_UP:
            self.snake.moving_up = True
            self.snake.moving_down = False
            self.snake.moving_left = False
            self.snake.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.snake.moving_left = True
            self.snake.moving_up = False
            self.snake.moving_down = False
            self.snake.moving_right = False
        elif event.key == pygame.K_RIGHT:
            self.snake.moving_right = True
            self.snake.moving_left = False
            self.snake.moving_up = False
            self.snake.moving_down = False
        elif event.key == pygame.K_q:
            sys.exit()

    def _grow_apple(self):
        if len(self.apples) < self.settings.apple_count:
            self._create_apple()

    def _create_apple(self):
        apple = Apple(self)
        x = randint(0, self.settings.screen_width)
        y = randint(0, self.settings.screen_height)

        apple.rect.x = x - x % 20
        apple.rect.y = y - y % 20

        self.apples.add(apple)

    def _snake_eats_apple(self):
        collisions = pygame.sprite.spritecollide(self.snake, self.apples, True)

        if collisions:
            self._create_apple()

    def _update_screen(self):
        self._grow_apple()
        self._snake_eats_apple()
        self.update_screen()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)

        for apple in self.apples.sprites():
            apple.draw()

        self.snake.blit_me()

        pygame.display.flip()


if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()
