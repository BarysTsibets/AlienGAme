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

        """"Ship Move  FLAG"""
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updating ship position depending of FLAG status"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1



    def blitme(self):
        """Drawing ship in the current position"""
        self.screen.blit(self.image, self.rect)



