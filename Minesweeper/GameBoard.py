from typing import Tuple, Any

import numpy
import numpy as np
from itertools import product

import pygame.event

from FrameRendering.Buttons.Tile import Tile
from numpy.array_api import astype

from Minesweeper.Cell import Cell
from Minesweeper.GameSettings import GameSettings
from FrameRendering.Buttons.Button import Button
from FrameRendering.Buttons.Tile import Tile


# Might work even through negative cartesian coordinates
def neighbors(index, game_settings: GameSettings):
    N = len(index)
    for relative_index in product((-1, 0, 1), repeat=N):
        if not all(i == 0 for i in relative_index):
            yield tuple(i + i_rel for i, i_rel in zip(index, relative_index))


class GameBoard:
    def __init__(self, game_settings: GameSettings):
        self.game_settings = game_settings
        self.game_board = np.ndarray((game_settings.width,) * game_settings.dimensions, 'O')
        shape = self.game_board.shape
        for idx in product(*[range(s) for s in shape]):
            self.game_board[idx] = Cell()
        self.tile_board = self.buttons_start()

        for cell in np.random.choice(self.game_board.flatten(), game_settings.mine_count, False):
            cell.bomb = True
        self.get_cell_numbers()

    def get_cell_numbers(self):
        for idx in product(*[range(s) for s in self.game_board.shape]):
            count = 0
            cell_indices = neighbors(idx, self.game_settings)
            for cell_index in cell_indices:

                if any(i < 0 or i >= self.game_settings.width for i in cell_index):
                    continue

                cell = self.game_board[cell_index]
                if cell.bomb:
                    count += 1
            self.game_board[idx].number = count

    def buttons_start(self) -> numpy.ndarray:
        x = 50
        y = 40
        x_start = 50
        wide = 32
        evenOrOdd = self.game_setting.dimensions%2
        buttons = 
        # if evenOrOdd == 0:
        #     x_end = wide*(self.game_settings.width)**(self.game_setting.dimensions/2)
        #     y_end = wide*(self.game_settings.width)**(self.game_setting.dimensions/2)
        # else:
        #     x_end = wide*(self.game_settings.width)**(self.game_setting.dimensions//2 +1)
        #     y_end = wide*(self.game_settings.width)**(self.game_setting.dimensions//2)
        # buttons = np.ndarray((self.game_settings.width,) * self.game_settings.dimensions, 'O')
        # while y < y_end:
        #     while x < x_end:
        #         buttons[]
        #
        #         pass
        # if self.game_settings.dimensions == 2:
        #     x_end = wide * (self.game_settings.width - 1) + x
        # elif self.game_settings.dimensions <= 4:
        #     x_end = wide * (self.game_settings.width * self.game_settings.width - 1) + wide * (
        #                 self.game_settings.width - 1) + x
        # else:
        #     x_end = wide * (self.game_settings.width ** 3 - 1) + wide * (
        #                 self.game_settings.width * self.game_settings.width - 1) + x
        #
        # buttons = np.ndarray((self.game_settings.width,) * self.game_settings.dimensions, 'O')
        #
        # idx: tuple[Any, ...] | Any
        # for idx in product(*[range(s) for s in self.game_board.shape]):
        #     buttons[idx] = Tile((x, y), (wide, wide), self.game_board[idx])
        #     if (x - wide * (self.game_settings.width - 1)) % (self.game_settings.width * wide) != x_start:
        #         x += wide
        #     elif (y - wide * (self.game_settings.width - 1)) % (self.game_settings.width * wide) != y_start:
        #         y += wide
        #         x -= wide * (self.game_settings.width - 1)
        #     elif x != x_end:
        #         x += wide * 2
        #         y -= wide * (self.game_settings.width - 1)
        #     else:
        #         y += 2*wide
        #         x = x_start
        #
        # return buttons

    def update_game_board(self, click_button: int ) -> None:
        for idx in product(*[range(s) for s in self.tile_board.shape]):
            if self.tile_board[idx].is_mouse_overred():
                if click_button == 1:
                    self.tile_board[idx].clear = True
                if click_button == 3:
                    self.tile_board[idx].flag = not self.tile_board[idx].flag

