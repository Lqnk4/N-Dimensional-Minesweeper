from typing import Tuple, Any

import numpy
import numpy as np
from itertools import product

import pygame.event

import EventHandler
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
        # grid = self.game_board.reshape(self.game_board[0], -1)

        # x = 0
        # y = 0
        # x_start = 64
        # y_start = 96
        #
        # tile_width = 32
        #
        # if self.game_settings.dimensions % 2 == 0:
        #
        #     x = (self.game_settings.width)**(self.game_setting.dimensions/2)
        #     y = (self.game_settings.width)**(self.game_setting.dimensions/2)
        # else:
        #     x = (self.game_settings.width)**(self.game_setting.dimensions//2 +1)
        #     y = (self.game_settings.width)**(self.game_setting.dimensions//2)
        # for i in range(y):
        #     for i in range(x):
        #         grid[(x,y)] = Tile(, (32, 32), grid[(x,y)])



        x = 50
        y = 40
        x_start = 50
        y_start = 40
        y_space = 0
        x_space = 0
        wide = 32

        evenOrOdd = self.game_settings.dimensions%2
        if evenOrOdd == 0:
            x_end = wide * self.game_settings.width ** (self.game_settings.dimensions // 2) - wide + x_start
        else:
            x_end = wide*(self.game_settings.width)**(self.game_settings.dimensions//2 +1)-wide+x_start
        tiles = np.ndarray((self.game_settings.width,) * self.game_settings.dimensions, 'O')


        idx: tuple[Any, ...] | Any
        for idx in product(*[range(s) for s in self.game_board.shape]):
            tiles[idx] = Tile((x+x_space, y+y_space), (wide, wide), self.game_board[idx])
            if sum(idx) % 2 == 0:
                tiles[idx].shape_color = pygame.Color(56, 128, 4)  # Dark grass color
            if (x-wide*(self.game_settings.width-1))%(wide*self.game_settings.width) != x_start:
                x += wide
            elif (y-wide*(self.game_settings.width-1))%(wide*self.game_settings.width) != y_start:
                y += wide
                x -= wide*(self.game_settings.width-1)
            elif x != x_end:
                x += wide
                x_space += wide
                y -= wide*(self.game_settings.width-1)
            else:
                x = x_start
                x_space = 0
                y += wide
                y_space += wide
        return tiles

    def update_game_board(self, click_button: int) -> None:
        count_max = self.game_settings.width ** self.game_settings.dimensions - self.game_settings.mine_count
        count = 0
        for idx in product(*[range(s) for s in self.tile_board.shape]):

            if self.tile_board[idx].cell.clear:
                count += 1
            if self.tile_board[idx].is_mouse_overed():
                if click_button == 1:
                    self.tile_board[idx].cell.clear = True
                    count += 1
                    if self.tile_board[idx].cell.number == 0:
                        # for index in neighbors(idx, self.game_settings):
                        #     count += 1
                        #     self.tile_board[index].cell.clear = True
                        pass
                    if self.tile_board[idx].cell.bomb:
                        # return -1
                        pass

                if click_button == 3 and not self.tile_board[idx].cell.bomb:
                    self.tile_board[idx].cell.flag = not self.tile_board[idx].cell.flag
            if count == count_max:
                # return 1
                pass
            else:
                #return 0
                pass
