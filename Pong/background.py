import pygame
import color


class Background:
    def __init__(self, screen, width, height, color_=color.WHITE, line_thickness=10):
        self.screen = screen
        self.width = width
        self.height = height
        self.color = color_
        self.line_thickness = line_thickness

    def draw(self):
        coordinates =  (self.width/2, 0, 5, self.height)
        pygame.draw.rect(self.screen, self.color, coordinates)
        

    def display_player_name(self):
        font = pygame.font.Font('freesansbold.ttf', 500)
        text = font.render('Player 1', True, color.GREEN, color.BLUE)
        textRect = text.get_rect()
        textRect.center = (self.width/4, self.height/5)
        # set the center of the rectangular object.
        (self.screen).blit(text, textRect)
