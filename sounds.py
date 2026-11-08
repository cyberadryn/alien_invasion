import pygame


class Sounds:
    """Manage music for Alien Invasion."""

    def __init__(self):
        self.audio_enabled = True

        try:
            # Explicitly try to initialize the mixer
            pygame.mixer.init()

            # Double-check that it successfully initialized
            if pygame.mixer.get_init() is None:
                self.audio_enabled = False
        except Exception:
            self.audio_enabled = False

        if self.audio_enabled:
            try:
                pygame.mixer.music.load("sounds/alien_invader_music.mp3")
                pygame.mixer.music.set_volume(0.3)
            except pygame.error as e:
                print(f"Could not load music file: {e}")
                self.audio_enabled = False
        else:
            print(
                "Warning: Audio device not found. Running game in silent mode."
            )

    def play_music(self):
        """Play background music continuously if audio is enabled."""
        if self.audio_enabled:
            pygame.mixer.music.play(-1)

    def stop_music(self):
        """Stop the background music if audio is enabled."""
        if self.audio_enabled:
            pygame.mixer.music.stop()
