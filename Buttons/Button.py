import string

import pygame
from pygame import Surface, Color, SurfaceType
from pygame.font import Font

from Fonts.Fonts import Fonts


# Base class for buttons
# Might extend to game cells as well
class Button:

    # Makes a rectangular button in the form of (left, top) and (w, h)
    def __init__(self, position: tuple[float, float], size: tuple[float, float], text, shape_color: Color, text_color: Color, font: Font):
        self.shape_color = shape_color
        self.text_color = text_color
        self.position = position
        self.size = size
        self.text = text
        self.font = font
        self.rect = pygame.rect.Rect(self.position, self.size)


    def render_button(self, screen: Surface | SurfaceType):
        # pygame.draw.rect(screen, self.shape_color, self.rect)
        img = self.font.render(self.text, True, self.text_color, self.shape_color)
        screen.blit(img, self.position, self.rect)
