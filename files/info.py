import pygame.font


class Info:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.pb = game.play_button

        self._prep_info()

    def _prep_game_over_info(self):
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.game_over_image = self.font.render('Game Over', True, self.text_color)
        self.game_over_rect = self.game_over_image.get_rect()

        self.game_over_rect.centerx = self.screen_rect.centerx
        self.game_over_rect.top = self.screen_rect.top + 50

    def _prep_play_button_info(self):
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 24)

        self.play_info_image = self.font.render("For play press 'P'", True, self.text_color)
        self.play_info_rect = self.play_info_image.get_rect()

        self.play_info_rect.midbottom = self.pb.msg_rect.midtop
        self.play_info_rect.y -= 20

    def _prep_info(self):
        self._prep_game_over_info()
        self._prep_play_button_info()

    def draw_info(self):
        self.screen.blit(self.game_over_image, self.game_over_rect)
        self.screen.blit(self.play_info_image, self.play_info_rect)
