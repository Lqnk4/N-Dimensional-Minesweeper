import pygame
from GameStates.FrameRenderer import GameState
from GameStates.FrameRenderer import FrameRenderer


class EventHandler:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.frame_renderer = FrameRenderer(self.screen)
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.game_state = GameState.TITLE

        self.running = True

    def deploy(self):

        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break

            # Renders the game frame based on the menu the player is in
            # Title, Settings, Game, etc
            self.frame_renderer.render_frame(self.game_state)

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = self.clock.tick(60) / 1000
