class Settings:
    """ Initialize all game settings """
    def __init__(self):

        # game settings
        self.screen_width = None
        self.screen_height = None
        self.bg_color = (0, 0, 0)

        self.objects_width = 20
        self.objects_height = 20

        # snake settings
        self.snake_color = (255, 255, 0)
        self.piece_width = self.objects_width
        self.piece_height = self.objects_height

        # apple settings
        self.apple_color = (255, 0, 0)
        self.apple_count = 1
        self.apple_width = self.objects_width
        self.apple_height = self.objects_height

    def initialize_dynamic_settings(self):
        self.v_direction = -1
        self.h_direction = 0
        self.snake_speed = float(self.objects_width)

