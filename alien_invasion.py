import pygame
import sys


def run_game():
    """Create screen object"""
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Alien Invasion")

    """Run main loop of the game"""
    while True:
        """Tracking keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        """Tracking the last drawn screen """
        pygame.display.flip()
run_game()


