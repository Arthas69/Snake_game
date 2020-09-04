import sys
from random import randint
from time import sleep

import pygame

from files.apple import Apple
from files.button import Button
from files.game_stats import GameStats
from files.info import Info
from files.scoreboard import Scoreboard
from files.settings import Settings
from files.snake import Snake


class SnakeGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.settings = Settings()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.play_button = Button(self, 'Play')
        self.info = Info(self)

        pygame.display.set_caption('Snake')
        self.snake = Snake(self)
        self.apples = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self._update_snake()
                sleep(0.03)
            self._update_screen()

    def _create_apple(self):
        apple = Apple(self)
        x = randint(0, self.settings.screen_width)
        y = randint(0, self.settings.screen_height)

        apple.rect.x = x - x % 20
        apple.rect.y = y - y % 20

        self.apples.add(apple)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_DOWN:
            if not self.settings.v_direction:
                self.settings.v_direction = 1
                self.settings.h_direction = 0
        elif event.key == pygame.K_UP:
            if not self.settings.v_direction:
                self.settings.v_direction = -1
                self.settings.h_direction = 0
        elif event.key == pygame.K_LEFT:
            if not self.settings.h_direction:
                self.settings.h_direction = -1
                self.settings.v_direction = 0
        elif event.key == pygame.K_RIGHT:
            if not self.settings.h_direction:
                self.settings.h_direction = 1
                self.settings.v_direction = 0
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_end_game(self):
        if any((self.snake.check_boundaries(), self.snake.check_self_eaten())):
            self._game_over()

    def _check_play_button(self):
        mouse_pos = pygame.mouse.get_pos()
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _game_over(self):
        self.stats.game_active = False
        pygame.mouse.set_visible(True)

    def _grow_apple(self):
        if len(self.apples) < self.settings.apple_count:
            self._create_apple()

    def _snake_eats_apple(self):
        collisions = pygame.sprite.spritecollide(self.snake, self.apples, True)

        if collisions:
            x = collisions[0].rect.x
            y = collisions[0].rect.y
            self.snake.body.insert(0, self.snake.head)
            self.snake.head = [x, y]
            self._create_apple()
            self.stats.score += 1

    def _start_game(self):
        self.stats.game_active = True
        self.stats.reset_stats()
        self.snake.create_snake()
        pygame.mouse.set_visible(False)

    def _update_snake(self):
        self._check_end_game()
        self.snake.update()

    def _update_screen(self):
        self._grow_apple()
        self._snake_eats_apple()
        self.update_screen()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)

        for apple in self.apples.sprites():
            apple.draw_apple()

        self.snake.draw_snake()
        if not self.stats.game_active:
            self.sb.prep_images()
            self.sb.draw_score()
            self.info.draw_info()
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()
