import pygame
import color
import objActivity


class Ball(objActivity.ObjActivity):
    def __init__(self, screen, shape, color_=color.BLUE):
        velocity = {"x":10, "y":0}
        super().__init__(shape,velocity)
        self.screen = screen
        self.shape = shape
        self.color = color_

    def get_direction(self):
        direction = 1
        if self.velocity["x"] > 0 :
            direction = -1
        return direction

    def deflect_off_player(self, player_shape):
        player_y, player_height = player_shape.y, player_shape.height
        player_y_midpt = player_y+(player_height/2)
        ball_y, ball_height = self.shape.y, self.shape.height
        ball_y_midpt = ball_y+(ball_height/2)
        direction = self.get_direction()
        if player_y_midpt == ball_y_midpt:
            self.velocity["x"]= direction*10
        elif 0<abs(player_y_midpt-ball_y_midpt)<=30:
            self.velocity["x"] = direction*10
            self.velocity["y"] = direction*10
        elif 30<abs(player_y_midpt-ball_y_midpt)<=60:
            self.velocity["x"] = direction*10
            self.velocity["y"] = direction*15

    def deflect_off_screen(self):
        direction = self.get_direction()
        self.velocity["y"] = direction*10
        
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)




        

