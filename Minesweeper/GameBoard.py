from typing import Tuple, Any

import numpy
import numpy as np
from itertools import product
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
        x_end = 0
        if self.game_settings.dimensions == 2:
            x_end = wide*(self.game_settings.width-1)
        elif self.game_settings.dimensions <= 4:
            x_end = wide*(self.game_settings.width*self.game_settings.width-1) + wide*(self.game_settings.width-1)
        else:
            x_end = wide*(self.game_setting.width**3-1)+wide*(self.game_settings.width*self.game_setting.width-1)

        buttons = np.ndarray((self.game_settings.width,) * self.game_settings.dimensions, 'O')

        idx: tuple[Any, ...] | Any
        for idx in product(*[range(s) for s in self.game_board.shape]):
            buttons[idx] = Tile((x,y),(wide,wide), self.game_board[idx])
            if (x - 50 - wide * self.game_settings.width - 1)%(self.game_settings.width * wide) != 0:
                x += wide
            elif (y - 40 - wide * self.game_settings.width - 1)%(self.game_settings.width * wide) != 0:
                y += wide
                x -= wide*(self.game_settings.width-1)
            elif(x != x_end):
                x += wide*2
                y -= wide*(self.game_settings.width-1)
            else:
                y += wide
                x = x_start

        return buttons
