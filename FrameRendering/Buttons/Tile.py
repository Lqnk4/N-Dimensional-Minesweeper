import pygame.color
from pygame import Surface, SurfaceType

from FrameRendering.Buttons.Button import Button
from Minesweeper import Cell


class Tile(Button):
    def __init__(self, position: tuple[float, float], size: tuple[float, float], cell: Cell,
                 shape_color: pygame.color.Color = pygame.color.Color(161, 157, 146)):
        super().__init__(position, size, shape_color)
        self.cell = cell

        self.default_color = pygame.color.Color(161, 157, 146)
        self.hover_color = pygame.color.Color(255, 255, 255)
        self.clear_color = pygame.color.Color(199, 182, 181)

    def render_button(self, screen: Surface | SurfaceType):
        pygame.draw.rect(screen, self.shape_color, self.rect)
        if self.cell.flag:
            img = pygame.image.load_basic("path_to_flag")
            screen.blit(img, self.rect.center)
        elif self.cell.clear:
            if n:= self.cell.number > 0:
                img = pygame.image.load_basic("path to number")
                screen.blit(img, self.rect.center)
            else:
                self.shape_color = self.clear_color
        elif self.cell.bomb:
            img = pygame.image.load_basic("path to bomb")
            screen.blit(img, self.rect.center)
        elif self.is_mouse_overed():
            self.shape_color = self.hover_color
        else:
            self.shape_color = self.default_color
