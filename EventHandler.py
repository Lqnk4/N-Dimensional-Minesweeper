from enum import Enum
from itertools import product

import pygame

from FrameRendering.FrameRenderer import FrameRenderer
from FrameRendering.FrameRenderer import GameState
from Minesweeper.GameBoard import GameBoard
from Minesweeper.GameSettings import GameSettings

class GameWin(Enum):
    WIN = 1
    LOSS = -1
    CONTINUE = 0

class EventHandler:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.frame_renderer = FrameRenderer(self.screen)

        self.clock = pygame.time.Clock()
        self.dt = 0

        self.game_state = GameState.TITLE

        self.game_settings = GameSettings(4, 4, 40) # Default Values

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
                    click_button = event.button # 1 is left click, 3 is right click
                    if self.game_state == GameState.GAME:
                        # 1 is won
                        if self.game_board.update_game_board(click_button) == 1:
                            pass
                        break
                    for button_key, button in self.frame_renderer.get_active_buttons(self.game_state).items():
                        if button.is_mouse_overed():

                            match button_key:
                                case"Title":
                                    pass
                                case "Title_Start":
                                    self.game_state = GameState.SETTINGS
                                case "Dimension_Counter":
                                    self.game_settings.dimensions += 1
                                case "dimension_decrement":
                                    self.game_settings.dimensions -= 1
                                case "Width Counter":
                                    self.game_settings.width += 1
                                case "Width Decrement":
                                    self.game_settings.width -= 1
                                case "Mine Counter":
                                    self.game_settings.mine_count += 5
                                case "Mine Decrement":
                                    self.game_settings.mine_count -= 5
                                case "Game Start":
                                    self.game_board = GameBoard(self.game_settings)
                                    self.game_state = GameState.GAME
                            break









            # Renders the game frame based on the menu the player is in
            # Title, Settings, Game, etc
            self.frame_renderer.render_frame(self.game_state, self.game_settings, self.game_board)

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = self.clock.tick(60) / 1000
