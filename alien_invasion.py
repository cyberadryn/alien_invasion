import os
import sys
import pygame
from settings import Settings
from ship import Ship
# """
# In Alien Invasion, the player controls a rocketship tha appears at the bottom center of the screen. The player can move the ship right
# and left using the arrow keys and shoot builders using the spacebar. When the game begins, a fleet of aliens fills the sky destroys
# the aliens. If the player destorys all the aliens, a new fleet appears that move faster than the previous fleet. If any alien hits the
# player's ship or reaches the bottom of the screen, the player loses a ship. If the player loses three ships, the game ends.
# """


class AlienInvasion:
    """Overall class to manage game assests and behavior."""

    def __init__(self):
        """Initalize the game, and create the game resources."""

        # Initializes Pygame's modules so they're ready to use.
        pygame.init()

        # Set Title of the Window
        pygame.display.set_caption("Alien Invasion")

        # Set dimension of the PyGame Window
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)
        # Set background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            # self.screen.fill(self.bg_color)
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
