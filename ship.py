import os
import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting postion."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()


        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        print(self.image.get_at((0, 0)))

        # Make the white background transparent.
        self.image.set_colorkey((255, 255, 255,255))

        # Resize the image.
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Start each enew ship a the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
