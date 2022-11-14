import pygame
import color


class Background:
    def __init__(self, screen, width, height, color_=color.WHITE, line_thickness=10):
        self.screen = screen
        self.width = width
        self.height = height
        self.color = color_
        self.line_thickness = line_thickness

    def draw(self):
        coordinates =  (self.width/2, 0, 5, self.height)
        pygame.draw.rect(self.screen, self.color, coordinates)
