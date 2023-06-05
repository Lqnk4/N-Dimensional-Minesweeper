from itertools import product

import pygame

from FrameRendering.FrameRenderer import FrameRenderer
from FrameRendering.FrameRenderer import GameState
from Minesweeper.GameBoard import GameBoard
from Minesweeper.GameSettings import GameSettings


class EventHandler:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.frame_renderer = FrameRenderer(self.screen)

        self.clock = pygame.time.Clock()
        self.dt = 0

        self.game_state = GameState.TITLE

        self.game_settings = GameSettings(2, 5, 25)

        self.game_board = GameBoard(self.game_settings)

        self.running = True

    def deploy(self):

        pygame.mixer.music.load("Music/for-elevator-jazz-music-124005.mp3")
        pygame.mixer.music.play(-1)

        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_button = event.button
                    for button_key, button in self.frame_renderer.get_active_buttons(self.game_state).items():
                        if button.is_mouse_overed():

                            if button_key == "Title":
                                pass
                            elif button_key == "Start":
                                self.game_state = GameState.GAME
                            elif button_key == "Dimension_Counter":
                                self.game_settings.dimensions += 1
                            elif button_key == "Width Counter":
                                self.game_settings.width += 1

                    if self.game_state == GameState.GAME:
                        pass





            # Renders the game frame based on the menu the player is in
            # Title, Settings, Game, etc
            self.frame_renderer.render_frame(self.game_state, self.game_settings, self.game_board)

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = self.clock.tick(60) / 1000
