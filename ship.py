import pygame

class Ship:

    def __init__(self, screen):
        """Initialising ship and set ship starting position"""
        self.screen = screen

        """Loading image and get rectangle"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """New ship will be centered in the  bottom of the screen """
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """Drawing ship in the current position"""
        self.screen.blit(self.image, self.rect)



