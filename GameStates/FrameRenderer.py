from enum import Enum


# Class containing all menus in the game
# Might be associated with buttons in the future
class GameState(Enum):
    TITLE = 0
    SETTINGS = 1


class FrameRenderer:

    # Class requires the pygame screen to render frames
    def __init__(self, screen):
        self.screen = screen

    # Method with match statement to decide what game menu to render based on the game state
    def render_frame(self, game_state):
        match game_state:
            case GameState.TITLE:
                self.screen.fill("purple")

            case GameState.SETTINGS:
                self.screen.fill("blue")
