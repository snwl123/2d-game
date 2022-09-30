import pygame
import background
import player

pygame.init()  


class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        width = self.screen.get_width()
        height = self.screen.get_height()
        self.background = background.Background(width, height)
        self.player_A = player.Player(pygame.Rect(10, height/2-30, 1, 60))
        self.player_B = player.Player(pygame.Rect(width-10, height/2-30, 1, 60))
        self.main_loop()

    def draw(self):
        self.player_A.draw(self.screen)
        self.player_B.draw(self.screen)
        self.background.draw(self.screen)

    def main_loop(self):
        done = False
        self.draw()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            pygame.display.update()


if __name__ == '__main__':
    Tetris()
