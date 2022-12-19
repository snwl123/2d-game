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

    def deflection(self, player_shape):
        player_x, player_y, player_width, player_height = player_shape
        player_y_midpt = player_y+(player_height/2)
        ball_x, ball_y, ball_width, ball_height = self.shape
        ball_y_midpt = ball_y+(ball_height/2)
        move_multiplier = 1
        if self.velocity["x"] > 0 :
            move_multiplier = -1
        if player_y_midpt == ball_y_midpt:
            self.velocity["x"]= move_multiplier*10
        elif 0<abs(player_y_midpt-ball_y_midpt)<=30:
            self.velocity["x"] = move_multiplier*10
            self.velocity["y"] = move_multiplier*10
        elif 30<abs(player_y_midpt-ball_y_midpt)<=60:
            self.velocity["x"] = move_multiplier*10
            self.velocity["y"] = move_multiplier*15
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)




        

