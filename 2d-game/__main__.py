import pygame
import background
import player
import color

pygame.init()  
screen = pygame.display.set_mode((640,480))

def initialise():
    pygame.init()  
    screen = pygame.display.set_mode((640,480))
    background.Background().draw()
    player_A = player.Player(pygame.Rect(10, screen.get_height()/2-30, 1, 60), 'Player A', 0, color.white, 1)
    player_B = player.Player(pygame.Rect(screen.get_width()-10, screen.get_height()/2-30, 1, 60), 'Player B', 0, color.white, 1)
    main_loop(player_A, player_B)
    
def main_loop(player_A, player_B):
    done = False
    player_A.draw()
    player_B.draw()
    while not done:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True  
        pygame.display.update()


    
        

if __name__ == '__main__':
    initialise()