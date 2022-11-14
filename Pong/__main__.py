import pygame
import background
import player
import ball
import color

pygame.init()  


class Pong:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        width = self.screen.get_width()
        height = self.screen.get_height()
        self.background = background.Background(self.screen, width, height)
        self.player_A = player.Player(self.screen, pygame.Rect(10, height/2-30, 5, 60))
        self.player_B = player.Player(self.screen, pygame.Rect(width-10, height/2-30, 5, 60))
        self.ball = ball.Ball(self.screen, pygame.Rect(width/2-5, height/2+5, 10, 10))
        self.move_constant = 10
        self.main_loop()

    def draw(self):
        self.screen.fill((color.BLACK))
        self.background.draw()
        self.player_A.draw()
        self.player_B.draw()
        self.ball.draw()

    def main_loop(self):
        done = False
        self.draw()
        clock = pygame.time.Clock()
        while not done:
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_UP]:
                self.player_A.move(-self.move_constant)
            if keystate[pygame.K_DOWN]:
                self.player_A.move(self.move_constant)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            self.draw()
            pygame.display.update()
            clock.tick(60)


if __name__ == '__main__':
    Pong()
