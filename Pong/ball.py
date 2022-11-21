import pygame
import color


class Ball:
    def __init__(self, screen, shape, velocity, color_=color.BLUE):
        self.screen = screen
        self.shape = shape
        self.velocity = velocity
        self.color = color_

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)

    def move(self):
        x, y, width, height = self.shape
        shape = (x-self.velocity["x"], y-self.velocity["y"], width, height)
        self.shape = shape




        

