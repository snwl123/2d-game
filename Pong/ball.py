import pygame
import color


class Ball:
    def __init__(self, screen, shape, color_=color.BLUE):
        self.screen = screen
        self.shape = shape
        self.color = color_

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)



        

