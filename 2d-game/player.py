import pygame
import color

class Player():
    def __init__(self, screen, shape, name, score, line_thickness = 10, color = color.white):
        self.screen = screen
        self.shape = shape
        self.name = name
        self.score = score
        self.line_thickness = line_thickness

    @staticmethod
    def construct_player(screen, distance_from_end, name, score, line_thickness, player_length = 60):
        player_coordinates = [(distance_from_end, screen.get_height()/2 - player_length/2),(distance_from_end, screen.get_height()/2 + player_length/2)]
        player_shape = pygame.draw.lines(screen, color.white, False, player_coordinates, line_thickness)
        return Player(screen, player_shape, name, score)

    def draw(self, color = color.white, line_thickness = 10):
        pygame.draw.rect(self.screen, color, self.shape, line_thickness)

