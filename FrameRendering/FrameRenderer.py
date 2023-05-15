from enum import Enum

import pygame


# Class containing all menus in the game
# Might be associated with buttons in the future
class GameState(Enum):
    TITLE = 0
    SETTINGS = 1
    CREDITS = 2


class FrameRenderer:

    # Class requires the pygame screen to render frames
    def __init__(self, screen: pygame.Surface | pygame.SurfaceType):
        self.screen = screen

        self.base_font = pygame.font.SysFont("arial.ttf", 48)

    # Method with match statement to decide what game menu to render based on the game state
    def render_frame(self, game_state: GameState):

        background_color = pygame.color.Color(36, 36, 36)

        match game_state:
            case GameState.TITLE:
                # fills the screen to overwrite anything from previous frame
                self.screen.fill(background_color)
            case GameState.SETTINGS:
                self.screen.fill(background_color)

            case GameState.CREDITS:
                self.screen.fill(background_color)
