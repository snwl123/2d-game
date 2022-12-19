import pygame
import color
import objActivity


class Ball(objActivity.ObjActivity):
    def __init__(self, screen, shape, color_=color.BLUE):
        self.velocity = {"x":10, "y":0}
        super().__init__(shape,self.velocity)
        self.screen = screen
        self.shape = shape
        self.color = color_

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)




        

