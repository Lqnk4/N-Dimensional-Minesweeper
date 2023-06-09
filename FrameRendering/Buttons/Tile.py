import pygame.color
from pygame import Surface, SurfaceType

from FrameRendering.Buttons.Button import Button
from Minesweeper import Cell


class Tile(Button):
    def __init__(self, position: tuple[float, float], size: tuple[float, float], cell: Cell):
        self.light_grass_color = pygame.color.Color(63, 155, 11)
        self.dark_grass_color = pygame.color.Color(56, 128, 4)

        super().__init__(position, size, self.light_grass_color)
        self.cell = cell

        self.font = pygame.sysfont.SysFont(None, 24)

    def render_button(self, screen: Surface | SurfaceType):
        pygame.draw.rect(screen, self.shape_color, self.rect)
        flag_img = pygame.image.load("FrameRendering/Sprites/pixil-frame-0.png")
        bomb_img = pygame.image.load("FrameRendering/Sprites/pixil-frame-0_4.png")
        if self.cell.flag:
            screen.blit(flag_img, self.rect.topleft)
        if self.cell.clear:
            pass

        if self.cell.bomb and self.cell.clear:
            screen.blit(bomb_img, self.rect.topleft)



    def render_bomb(self, screen: Surface | SurfaceType):
        img = pygame.image.load("FrameRendering/Sprites/pixil-frame-0.png")
        screen.blit(img, self.rect.topleft)

    def is_mouse_overed(self) -> bool:
        return super().is_mouse_overed()
