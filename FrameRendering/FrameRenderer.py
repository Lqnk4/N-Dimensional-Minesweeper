from enum import Enum
from Buttons.Button import Button

from Buttons.Button import Button
import pygame


# Class containing all menus in the game
# Might be associated with buttons in the future
class GameState(Enum):
    TITLE = 0
    SETTINGS = 1


class FrameRenderer:

    # Class requires the pygame screen to render frames
    def __init__(self, screen: pygame.Surface | pygame.SurfaceType):
        self.screen = screen

    # Method with match statement to decide what game menu to render based on the game state
    def render_frame(self, game_state: GameState):
        match game_state:
            case GameState.TITLE:
                self.screen.fill("purple")
                # b = Button((self.screen.get_width() / 2, self.screen.get_height()/2), (self.screen.get_width() / 2, self.screen.get_height()/2), "hi", pygame.color.Color(255, 255, 255), pygame.color.Color(0, 0, 0))
            case GameState.SETTINGS:
                self.screen.fill("blue")
