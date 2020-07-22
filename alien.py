import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """class for representing one alien"""

    def __init__(self, ai_settings, screen):
        """Initialising ship and set ship starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading Alien image and set attribute rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # new alien appear in the left top corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # saving float position of the Alien
        self.x = float(self.rect.x)


    def blitme(self):
        """showing alien in the current position"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Move aliens to the right"""
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x