import pygame
import sys
from settings import Settings


def run_game():
    """Initialising pygame, settings and  screen object"""
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    """Run main loop of the game"""
    while True:

        """Tracking keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        """Drawing BackGround screen color"""
        screen.fill(ai_settings.bg_color)

        """Tracking the last drawn screen """
        pygame.display.flip()


run_game()


