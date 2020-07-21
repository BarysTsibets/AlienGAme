import sys
import pygame


def check_events(ship):
    """Handles a key press and a mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False





def update_screen(ai_settings, screen, ship):
    """Drawing BackGround screen color"""
    """Drawing every time during  each loop"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    """Tracking the last drawn screen """
    pygame.display.flip()

