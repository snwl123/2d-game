import pygame
import color
import objActivity

class Player(objActivity.ObjActivity):
    def __init__(self, screen, shape, score=0, color_=color.WHITE):
        self.velocity = {"x":0, "y":0}
        super().__init__(shape,self.velocity)
        self.screen = screen
        self.shape = shape
        self.score = score
        self.color = color_

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)
        self.velocity["y"] = 0



        

