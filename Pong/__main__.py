import pygame
import background
import player
import ball
import color

pygame.init()  
pygame.display.set_caption('Pong')


class Pong:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.background = background.Background(self.screen, self.width, self.height)
        self.move_constant = 5
        self.player_A = player.Player(self.screen, pygame.Rect(10, self.height/2-30, 5, 60))
        self.player_B = player.Player(self.screen, pygame.Rect(self.width-10, self.height/2-30, 5, 60))
        self.ball = ball.Ball(self.screen, pygame.Rect(self.width/2-5, self.height/2+5, 10, 10))
        self.main_loop()

    def move(self):
        self.ball.move()
        self.player_A.move()
        self.player_B.move()

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
                self.player_A.velocity["y"]=self.move_constant
                self.player_B.velocity["y"]=self.move_constant
            if keystate[pygame.K_DOWN]:
                self.player_A.velocity["y"]=-self.move_constant
                self.player_B.velocity["y"]=-self.move_constant
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            screen_top = pygame.Rect(0, 0, self.width, 1)
            screen_bottom = pygame.Rect(0, 0+self.height, self.width, 10)
            if (self.player_A.shape).colliderect(self.ball.shape):
                self.ball.deflect_off_player(self.player_A.shape)
            if (self.player_B.shape).colliderect(self.ball.shape):
                self.ball.deflect_off_player(self.player_B.shape)
            if (self.ball.shape).collidelist([screen_top, screen_bottom])!=-1:
                self.ball.deflect_off_screen()
            self.move()
            self.draw()
            pygame.display.update()
            clock.tick(60)


if __name__ == '__main__':
    Pong()
