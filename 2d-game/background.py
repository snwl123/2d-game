import pygame
import color
import __main__ as main


class Background():
    def __init__(self, color = color, line_thickness = 10):
        screen = main.screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.color = color
        self.line_thickness = line_thickness

    def draw(self):
        coordinates = [(self.width/2, 0),(self.width/2, self.height)]
        pygame.draw.lines(main.screen, self.color.white, False, coordinates, self.line_thickness)
