import pygame
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
    ship = Ship(screen)

    """Run main loop of the game"""
    while True:
        """Tracking keyboard and mouse events"""
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()


