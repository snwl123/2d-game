import pygame
import color


class Background:
    def __init__(self, width, height, color_=color.BLACK, line_thickness=10):
        self.width = width
        self.height = height
        self.color = color_
        self.line_thickness = line_thickness

    def draw(self, screen):
        coordinates = [(self.width/2, 0),(self.width/2, self.height)]
        is_closed = False
        pygame.draw.lines(screen, self.color, is_closed, coordinates, self.line_thickness)
