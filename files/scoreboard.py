import pygame.font


class Scoreboard:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.stats = game.stats

        self.font = pygame.font.SysFont(None, 24)
        self.text_color = (0, 0, 0)

        self.prep_images()

    def prep_images(self):
        self.prep_score()

    def prep_score(self):
        score = "{:,}".format(self.stats.score)
        self.score_img = self.font.render(f"Score: {score}", True, self.text_color)
        self.score_rect = self.score_img.get_rect()

        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = self.screen_rect.top + 150

    def draw_score(self):
        self.screen.blit(self.score_img, self.score_rect)
