import pygame
import color
import text
import objActivity

class Player(objActivity.ObjActivity):
    def __init__(self, screen, shape, name, score=0, color_=color.WHITE):
        velocity = {"x":0, "y":0}
        super().__init__(shape,velocity)
        self.screen = screen
        self.shape = shape
        self.name = name
        self.score = score
        self.color = color_

    def set_text(self, txt, center):
        txt = text.set(txt, center, 100)
        return txt

    def display_name(self, centre):
        name_txt = self.set_text(self.name, centre)
        (self.screen).blit(*name_txt)

    def display_score(self, centre):
        score_txt = self.set_text(str(self.score), centre)
        (self.screen).blit(*score_txt)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)
        self.velocity["y"] = 0



        

