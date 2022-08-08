import pygame
import color
import player


class Background():
    def __init__(self, screen, color = color, line_thickness = 10):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.color = color
        self.line_thickness = line_thickness

    def draw_middle_line(self):
        coordinates = [(self.width/2, 0),(self.width/2, self.height)]
        pygame.draw.lines(self.screen, self.color.white, False, coordinates, self.line_thickness)

    def draw_players(self, distance_from_end = 20 , names = ['Player A', 'Player B'], score = 0, player_length = 60):
        for name in names:
            player = player.Player.construct_player(self.screen, distance_from_end, name, score, player_length, self.line_thickness)

    # def draw_players(self, player_width = 60, distance_from_end = 10, line_thickness = 10):
    #     player_a_coordinates = [(distance_from_end, self.height/2 - player_width/2),(distance_from_end, self.height/2 + player_width/2)]
    #     player_b_coordinates = [(self.width - distance_from_end, self.height/2 - player_width/2),(self.width - distance_from_end, self.height/2 + player_width/2)]
    #     player_a_shape = pygame.draw.lines(self.screen, self.color.white, False, player_a_coordinates, line_thickness)
    #     player_b_shape = pygame.draw.lines(self.screen, self.color.white, False, player_b_coordinates, line_thickness)
    #     player.Player(player_a_shape, 'Player A', 0)
    #     player.Player(player_b_shape, 'Player B', 0)
