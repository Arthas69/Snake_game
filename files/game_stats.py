class GameStats:

    def __init__(self, game):
        self.settings = game.settings
        self.game_active = False

    def reset_stats(self):
        self.score = 0
        self.settings.initialize_dynamic_settings()
