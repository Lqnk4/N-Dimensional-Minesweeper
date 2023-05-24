from typing import Tuple, Any

import numpy as np
from itertools import product
from FrameRendering.Buttons.Tile import Tile
from numpy.array_api import astype

from Minesweeper.Cell import Cell
from Minesweeper.GameSettings import GameSettings


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
        get_cell_numbers(self)


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
def buttons_start(self):
    x = 50
    y = 40
    x_start = 50
    y_start = 40

    if(game_settings.dimensions%2 == 0):
        x_end = 50 + 30*game_settings.width^(game_settings.dimensions//2)+ 30*(game_settings.width^((game_setting.dimensions-2)/2)-2)
        y_end = 40 + 30*game_settings.width^(game_settings.dimensions//2)+ 30*(game_settings.width^((game_setting.dimensions-2)/2)-2)
    else:
        x_end = 50 + 30*game_settings.width^(game_settings.dimensions//2)+ 30*(game_settings.width^(game_setting.dimensions//2)-2)
        y_end = 40 + 30 *game_settings.width ^ ((game_settings.dimensions-1) // 2) + 30 * (game_settings.width ^ ((game_settings.dimensions - 3)/2) - 2)
    buttons = np.ndarray((game_settings.width,) * game_settings.dimensions, 'O')

    idx: tuple[Any, ...] | Any
    for idx in product(*[range(s) for s in self.game_board.shape]):
        buttons[idx] = Tile((x,y),(30,30), self.game_board[idx])
        if((x-50-30*game_settings.width-1)%(game_settings.width*30) != 0):
            x += 30
        elif((y-40-30*game_settings.width-1)%(game_settings.width*30) != 0):
            y += 30
            x -= 30*(game_settings.width-1)
        elif(x != x_end):
            x += 60
            y -= 30*(game_settings.width-1)
        else:
            y += 60
            x = x_start
        render_button(buttons[idx])
    return buttons
