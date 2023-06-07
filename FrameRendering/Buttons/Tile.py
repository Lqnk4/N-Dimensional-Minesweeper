import pygame.color
from pygame import Surface, SurfaceType

from FrameRendering.Buttons.Button import Button
from Minesweeper import Cell


class Tile(Button):
    def __init__(self, position: tuple[float, float], size: tuple[float, float], cell: Cell):
        self.default_color = pygame.color.Color(161, 157, 146)
        self.hover_color = pygame.color.Color(255, 255, 255)
        self.clear_color = pygame.color.Color(199, 182, 181)
        self.light_grass_color = pygame.color.Color(63, 155, 11)
        self.dark_grass_color = pygame.color.Color(56, 128, 4)

        super().__init__(position, size, self.default_color)
        self.cell = cell

        self.shape_color = self.default_color

        self.font = pygame.sysfont.SysFont(None, 24)

    def render_button(self, screen: Surface | SurfaceType):
        pygame.draw.rect(screen, self.shape_color, self.rect)
        number_image = self.font.render(str(self.cell.number), False, pygame.color.Color(255,0,0))
        screen.blit(number_image, self.rect.topleft)

    def render_bomb(self, screen: Surface | SurfaceType):
        img = pygame.image.load("FrameRendering/Sprites/pixil-frame-0.png")
        screen.blit(img, self.rect.topleft)

    def is_mouse_overed(self) -> bool:
        return super().is_mouse_overed()
