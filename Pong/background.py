import pygame
import color
import text


class Background:
    def __init__(self, screen, width, height, color_=color.WHITE, line_thickness=10):
        self.screen = screen
        self.width = width
        self.height = height
        self.color = color_
        self.line_thickness = line_thickness
        self.max_rounds=5
        self.round_no=0

    def draw(self):
        coordinates =  (self.width/2, 0, 5, self.height)
        # draw middle line
        pygame.draw.rect(self.screen, self.color, coordinates)
        # display match round number
        self.display_match_round()

    def display_match_round(self):
        # render text of score for Player A and add transparency (100/255)%
        score_txt = text.set(str(self.round_no)+'/' + str(self.max_rounds) + ' ROUNDS', (self.screen.get_width()/2, self.screen.get_height()-50), 175)
        (self.screen).blit(*score_txt)

