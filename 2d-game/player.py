import pygame
import color
import line

class Player():
    def __init__(self, shape, name, score, color, line_thickness = 5):
        self.shape = shape
        self.name = name
        self.score = score
        self.line_thickness = line_thickness
        self.color = color

    def draw(self, line_thickness = 20):
        start, end = self.shape.topleft, self.shape.bottomleft
        line.Line(start, end, self.color, line_thickness, line.LineType.DASHED).draw()


        

