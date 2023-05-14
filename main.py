import pygame

from EventHandler import EventHandler



if __name__ == "__main__":
    fonts = pygame.font.get_fonts()
    print(len(fonts))
    for f in fonts:
        print(f)
    eventHandler = EventHandler()
    eventHandler.deploy()
