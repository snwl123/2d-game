import pygame
import color


class Player:
    def __init__(self, screen, shape, score=0, color_=color.WHITE):
        self.screen = screen
        self.shape = shape
        self.score = score
        self.color = color_

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)
        
    def move(self, distance):
        x, y, width, height = self.shape
        shape = (x, y+distance, width, height)
        self.shape = shape



        

