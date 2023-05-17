import pygame
from pygame import Surface, Color, SurfaceType
from pygame.font import Font


# Base class for buttons
# Might extend to game cells as well
class Button:

    # Makes a rectangular button in the form of (left, top) and (w, h)
    def __init__(self, position: tuple[float, float], size: tuple[float, float], shape_color: Color, text_color: Color,
                 font: Font = None, text: str = None):
        self.shape_color = shape_color
        self.text_color = text_color
        self.position = position
        self.size = size
        self.text = text
        self.font = font

        self.rect = pygame.rect.Rect(self.position, self.size)

    def render_button(self, screen: Surface | SurfaceType):

        # Only draws a rectangle if no text or font
        pygame.draw.rect(screen, self.shape_color, self.rect)

        if self.text is None or self.font is None:
            return

        # Works
        img = self.font.render(self.text, True, self.text_color, self.shape_color)
        center = self.rect.center
        screen.blit(img, center)

    # Returns weather the mouse is over the cursor for animation purposes
    def is_mouse_overed(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.left <= mouse_pos[0] <= self.rect.right and self.rect.top <= mouse_pos[1] <= self.rect.bottom
