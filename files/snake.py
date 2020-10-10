import pygame


class Snake:

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.rect = pygame.Rect(0, 0, self.settings.piece_width, self.settings.piece_height)

        self.create_snake()

    def create_snake(self):
        self.rect.center = self.screen_rect.center

        self.y = float(self.rect.y - self.rect.y % self.settings.objects_width)
        self.x = float(self.rect.x - self.rect.x % self.settings.objects_width)

        self.head = [self.x, self.y]
        self.body = []
        for i in range(0, 4):
            self.body.append([self.x, self.y + self.settings.objects_width * i])
        self.tail = self.body[-1]

    def _grow_snake(self, x, y):
        self.head = [x, y]
        self.body.insert(0, self.head)
        self.tail = self.body.pop()

    def draw_snake(self):
        for part in self.body:
            body_rect = pygame.Rect(part[0], part[1], self.settings.piece_width, self.settings.piece_height)
            pygame.draw.rect(self.screen, self.settings.snake_color, body_rect)

    def check_self_eaten(self):
        if self.head in self.body[1:]:
            return True

    def check_boundaries(self):
        if not 0 <= self.head[0] < self.screen_rect.right or not \
                0 <= self.head[1] < self.screen_rect.bottom:
            return True

    def update(self):
        self.x += self.settings.snake_speed * self.settings.h_direction
        self.y += self.settings.snake_speed * self.settings.v_direction

        self.rect.x = self.x
        self.rect.y = self.y

        self._grow_snake(self.x, self.y)
