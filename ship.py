import pygame

class Ship:

    def __init__(self, ai_settings, screen):
        """Initialising ship and set ship starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        """Loading Ship image and get rectangle"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """New ship will be centered in the  bottom of the screen """
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        """"Ship Move  FLAG"""
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updating ship position depending of FLAG status"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center



    def blitme(self):
        """Drawing ship in the current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Create ship in the center of the screen"""
        self.center = self.screen_rect.centerx


