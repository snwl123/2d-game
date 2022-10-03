import pygame
import color

class Rectangle:

    def __init__(self, *, x = 0, y = 0, height = 1, width = 1, color = color.black, line_thickness = 1):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.line_thickness = line_thickness

    def draw(self, screen):
        points = [(self.x, self.y), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), (self.x, self.y + self.height)]
        pygame.draw.lines(screen, self.color, True, points, self.line_thickness)