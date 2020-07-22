class Settings:
    """Class to store all game Settings"""

    def __init__(self):
        """screen settings"""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        """Bullet settings"""
        self.bullet_speed_factor = 2
        self.bullet_width = 390
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        """Aliens settings"""
        self.alien_speed_factor = 1
        self.fleet_drop_speed= 10
        # fleet_direction = 1 mean move to the right ; '-1' -   to the left
        self.fleet_direction =1