import numpy as np
from itertools import product

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

            # TODO use this to break out of second for loop
            for i in cell_index:
                if i < 0 or i >= self.game_settings.width:
                    continue
                cell = self.game_board[cell_index]
            if cell.bomb:
                count += 1
        self.game_board[idx].number = count
        count = 0