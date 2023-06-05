import pygame.color
from pygame import Surface, SurfaceType

from FrameRendering.Buttons.Button import Button
from Minesweeper import Cell


class Tile(Button):
    def __init__(self, position: tuple[float, float], size: tuple[float, float], cell: Cell):
        self.default_color = pygame.color.Color(161, 157, 146)
        self.hover_color = pygame.color.Color(255, 255, 255)
        self.clear_color = pygame.color.Color(199, 182, 181)

        super().__init__(position, size, self.default_color)
        self.cell = cell

        self.shape_color = self.default_color

        self.font = pygame.sysfont.SysFont(None, 24)

    def render_button(self, screen: Surface | SurfaceType):
        pygame.draw.rect(screen, self.shape_color, self.rect)
        if self.cell.flag:
            img = pygame.image.load("FrameRendering/Sprites/564-5642137_a-pixel-art-trans-flag-i-made-flag.png")
            screen.blit(img, self.rect.topleft)
        elif self.cell.clear:
            if n := self.cell.number > 0:
                img = self.font.render(n)
                screen.blit(img, self.rect.topleft)
            else:
                self.shape_color = self.clear_color
        else:
            self.shape_color = self.default_color

    def render_bomb(self, screen: Surface | SurfaceType):
        img = pygame.image.load("FrameRendering/Sprites/pixil-frame-0.png")
        screen.blit(img, self.rect.topleft)

    def is_mouse_overed(self) -> bool:
        super().is_mouse_overed()
