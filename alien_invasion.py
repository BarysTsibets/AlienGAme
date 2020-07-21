import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_fynctions as gf


def run_game():
    """Initialising pygame, settings and  screen object"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    """Creating Ship"""
    ship = Ship(ai_settings, screen)
    """Creating Group for storing bullets"""
    bullets = Group()

    """Run main loop of the game"""
    while True:
        """Tracking keyboard and mouse events"""
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # Delete bullets outside of the screen.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()


