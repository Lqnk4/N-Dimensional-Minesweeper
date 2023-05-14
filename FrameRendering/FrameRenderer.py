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
        self.base_font = pygame.font.SysFont("arial.ttf", 48)

    # Method with match statement to decide what game menu to render based on the game state
    def render_frame(self, game_state: GameState):
        match game_state:
            case GameState.TITLE:
                # fills the screen to overwrite anything from previous frame
                self.screen.fill("black")

                # Test Button

                # b = Button((self.screen.get_width() / 2, self.screen.get_height() / 2),
                #            (self.screen.get_width() / 2, self.screen.get_height() / 2),
                #            pygame.color.Color(255, 255, 255), pygame.color.Color(0, 0, 0), self.base_font, "hi")
                # b.render_button(self.screen)
                #
                # mouse_pos = pygame.mouse.get_pos()
                #
                # if b.is_mouse_overed(mouse_pos):
                #     print("true")

                # Test Header

                # header = self.base_font.render("X: " + str(mouse_pos[0]) + " Y: " + str(mouse_pos[1]), True, pygame.color.Color(255, 255, 255))
                # self.screen.blit(header, (1000, 40))

            case GameState.SETTINGS:
                self.screen.fill("blue")
