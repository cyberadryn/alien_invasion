import pygame


class Sounds:
    """Manage music and sound effects for Alien Invasion."""

    def __init__(self):
        """Load game audio."""

        # Check if the audio mixer is available.
        self.audio_enabled = pygame.mixer.get_init() is not None

        if self.audio_enabled:
            # Background music.
            pygame.mixer.music.load("sounds/alien_invader_music.mp3")
            pygame.mixer.music.set_volume(0.3)

            # Laser sound effect.
            self.laser_sound = pygame.mixer.Sound("sounds/laser.mp3")
            self.laser_sound.set_volume(0.5)

        else:
            print("Audio unavailable. Running without sound.")

    def play_music(self):
        """Play background music."""
        if self.audio_enabled:
            pygame.mixer.music.play(-1)

    def stop_music(self):
        """Stop background music."""
        if self.audio_enabled:
            pygame.mixer.music.stop()

    def play_laser(self):
        """Play laser sound."""
        if self.audio_enabled:
            self.laser_sound.play()
