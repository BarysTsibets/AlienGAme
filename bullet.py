import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for bullets control , striked by the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create bullet object in the current ship possition"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Creating bullet in (0, 0) position and seting correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Bullet position saved in 'float' format
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """"Moving bullet Up pf the screen"""

        # Updating bullet position
        self.y -= self.speed_factor

        # Updating rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """"showing bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
