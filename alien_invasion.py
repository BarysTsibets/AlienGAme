import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
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
    """Creating Aliens Group"""
    aliens = Group()
    """creating Alien"""
    alien = Alien(ai_settings, screen)
    """Run main loop of the game"""
    # Creating alien fleet
    gf.create_fleet(ai_settings, screen, ship,  aliens)
    while True:
        """Tracking keyboard and mouse events"""
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()

# Creating Ship, bullets Group, and Aliens Group.



