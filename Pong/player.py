import color
import line


class Player:
    def __init__(self, shape, score=0, color_=color.WHITE, line_thickness=5):
        self.shape = shape
        self.score = score
        start, end = self.shape.topleft, self.shape.bottomleft
        self.line = line.Line(start, end, color_, line_thickness, line.LineType.DASHED)

    def draw(self, screen):
        self.line.draw(screen)


        

