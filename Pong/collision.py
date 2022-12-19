class Collision:
    def __init__(self, player_shape, ball_shape):
        self.player_shape = player_shape
        self.ball_shape = ball_shape
        

    def check(self):
        ball_x, ball_y, ball_width, ball_height = self.ball_shape
        player_x, player_y, player_width, player_height = self.player_shape

        player_yrange = range(player_y, player_y+player_height)
        ball_yrange = range(ball_y, ball_y+ball_height)
        y_intersection = [y for y in player_yrange if y in ball_yrange]

        player_xrange = range(player_x, player_x+player_width)
        ball_xrange = range(ball_x, ball_x+ball_width)
        x_intersection = [x for x in player_xrange if x in ball_xrange]

        if len(y_intersection)>1 and len(x_intersection)>1:
            return True
        else:
            return False
