class Settings:
    """ Initialize all game settings """
    def __init__(self):

        # game settings
        self.screen_width = None
        self.screen_height = None
        self.bg_color = (0, 0, 0)

        # snake settings
        self.snake_color = (255, 255, 0)
        self.piece_width = 20
        self.piece_height = 20
        self.snake_speed = 20.0

        # apple settings
        self.apple_color = (255, 0, 0)
        self.apple_count = 1
        self.apple_width = 20
        self.apple_height = 20

        self.v_direction = 1
        self.h_direction = 1