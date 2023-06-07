from enum import Enum
import pygame
from FrameRendering.Buttons.Button import Button
from Minesweeper.GameBoard import GameBoard
from itertools import product
from FrameRendering.Buttons.Tile import Tile
from Minesweeper.GameBoard import GameBoard
from Minesweeper.GameSettings import GameSettings


# Class containing all menus in the game
# Might be associated with buttons in the future
class GameState(Enum):
    TITLE = 0
    SETTINGS = 1
    CREDITS = 2
    GAME = 3
    LOADING = 4


class FrameRenderer:

    # Class requires the pygame screen to render frames
    def __init__(self, screen: pygame.Surface | pygame.SurfaceType):
        self.screen = screen

        self.base_font = pygame.font.SysFont("arial.ttf", 24)
        self.med_font = pygame.font.SysFont("arial.ttf", 48)
        self.title_font = pygame.font.SysFont("arial.ttf", 96)
        self.button_dict = {
            GameState.TITLE: {"Title": Button((self.screen.get_width() / 2 - 250, self.screen.get_height() / 2 - 80),
                                              (500, 120),
                                              pygame.color.Color(0, 154, 23), pygame.color.Color(0, 0, 0),
                                              self.title_font,
                                              "MINESWEEPER"),
                              "Title_Start": Button((self.screen.get_width() / 2 - 250, self.screen.get_height() / 2 + 30),
                                              (500, 50),
                                              pygame.color.Color(0, 154, 23), pygame.color.Color(0, 0, 0),
                                              self.med_font,
                                              "Now in n-Dimensions!!!", ),
                              },
            GameState.SETTINGS: {
                "Dimension_Counter": Button((140, 100), (320, self.screen.get_height() / 6),
                                            pygame.color.Color(0, 154, 23),
                                            pygame.color.Color(0, 0, 0), self.med_font, "Dimension_Counter"),
                "dimension_decrement": Button((140, 380), (320, self.screen.get_height() / 6),
                                            pygame.color.Color(0, 154, 23),
                                            pygame.color.Color(0, 0, 0), self.med_font, ""),
                "Width Counter": Button((800, 100),  (320, self.screen.get_height() / 6), pygame.color.Color(0, 154, 23),
                                            pygame.color.Color(0, 0, 0), self.med_font, "Width Counter"),
                "Game Start": Button((550, 450), (
                    self.screen.get_width() / 6, self.screen.get_height() / 6), pygame.color.Color(0, 154, 23),
                                            pygame.color.Color(0, 0, 0), self.med_font, "Game Start")
            },
            GameState.CREDITS: {},
            GameState.GAME: {}

        }

    # Method with match statement to decide what game menu to render based on the game state
    def render_frame(self, game_state: GameState, game_settings: GameSettings, game_board: GameBoard):

        background_color = pygame.color.Color(36, 36, 36)


        match game_state:
            case GameState.TITLE:

                # fills the screen to overwrite anything from previous frame
                self.screen.fill(background_color)

                mouse_pos = pygame.mouse.get_pos()

                for button in self.button_dict.get(GameState.TITLE).values():
                    button.render_button(self.screen)

            case GameState.SETTINGS:
                self.screen.fill(background_color)

                mouse_pos = self.base_font.render(str(pygame.mouse.get_pos()), False, pygame.Color(255,255,255))
                self.screen.blit(mouse_pos, (1100, 50))

                for button in self.button_dict.get(GameState.SETTINGS).values():
                    button.render_button(self.screen)
                dim_count_image = self.med_font.render(str(game_settings.dimensions), False, pygame.Color(255, 255, 255))
                self.screen.blit(dim_count_image, (290, 275))
                dim_down_image = self.med_font.render("Down", False, pygame.Color(255, 255, 255))
                width_count_image = self.med_font.render(str(game_settings.width),  False, pygame.Color(255, 255, 255))
                self.screen.blit(width_count_image, (960, 275))

            case GameState.CREDITS:
                self.screen.fill(background_color)
            case GameState.GAME:
                self.screen.fill(background_color)
                for idx in product(*[range(s) for s in game_board.tile_board.shape]):
                    game_board.tile_board[idx].render_button(self.screen)


    def get_active_buttons(self, game_state: GameState) -> dict:
        return self.button_dict.get(game_state)
