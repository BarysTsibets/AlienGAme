class GameStats():
    """Statistic ащк ФдшутШтмфышщт пфьу"""

    def __init__(self, ai_settings):
        """Initialising statistic"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Game starting at  inactive status
        self.game_active = False


    def reset_stats(self):
        """Initialising statistics during the game"""
        self.ships_left = self.ai_settings.ship_limit


