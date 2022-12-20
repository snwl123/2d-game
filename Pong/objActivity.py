import pygame

class ObjActivity:
    def __init__(self, shape, velocity):
        self.shape = shape
        self.velocity=velocity

    def move(self):
        x, y, width, height = self.shape
        shape = pygame.Rect(x-self.velocity["x"], y-self.velocity["y"], width, height)
        self.shape = shape