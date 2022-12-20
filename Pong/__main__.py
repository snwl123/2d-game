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
        self.player_A = player.Player(self.screen, pygame.Rect(10, self.height/2-30, 5, 60), 'Player A')
        self.player_B = player.Player(self.screen, pygame.Rect(self.width-10, self.height/2-30, 5, 60), 'Player B')
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
        self.player_A.display_name((self.width/4, 50))
        self.player_A.display_score((self.width/4, 100))
        self.player_B.draw()
        self.player_B.display_name(((self.width/4)*3, 50))
        self.player_B.display_score(((self.width/4)*3, 100))
        self.ball.draw()

    def restart_screen(self):
        if self.background.round_no < self.background.max_rounds:
            self.background.round_no+=1
        else:
            self.background.round_no=0
            self.player_A.score = 0
            self.player_B.score = 0
        self.ball = ball.Ball(self.screen, pygame.Rect(self.width/2-5, self.height/2+5, 10, 10))
        
    
    def main_loop(self):
        done = False
        self.draw()
        #create rect for sides of screen
        screen_top = pygame.Rect(0, 0, self.width, 1)
        screen_bottom = pygame.Rect(0, 0+self.height, self.width, 1)
        screen_left = pygame.Rect(0, 0, 1, self.height)
        screen_right = pygame.Rect(0+self.width, 0, 1, self.height)
        clock = pygame.time.Clock()
        while not done:
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_UP] and not ((self.ball.shape).colliderect(screen_top) or (self.ball.shape).colliderect(screen_bottom)):
                self.player_A.velocity["y"]=self.move_constant
                self.player_B.velocity["y"]=self.move_constant
            if keystate[pygame.K_DOWN] and not ((self.ball.shape).colliderect(screen_top) or (self.ball.shape).colliderect(screen_bottom)):
                self.player_A.velocity["y"]=-self.move_constant
                self.player_B.velocity["y"]=-self.move_constant
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            #check for collision with paddle
            if (self.player_A.shape).colliderect(self.ball.shape):
                self.ball.deflect_off_player(self.player_A.shape)
            if (self.player_B.shape).colliderect(self.ball.shape):
                self.ball.deflect_off_player(self.player_B.shape)
            #check for collision with top and bottom screen
            if (self.ball.shape).collidelist([screen_top, screen_bottom])!=-1:
                self.ball.deflect_off_screen()
            #check for collision with left and right screen
            if (self.ball.shape).colliderect(screen_right):
                self.player_A.score += 1
                self.restart_screen()
            elif (self.ball.shape).colliderect(screen_left):
                self.player_B.score += 1
                self.restart_screen()
            self.move()
            self.draw()
            pygame.display.update()
            clock.tick(60)


if __name__ == '__main__':
    Pong()
