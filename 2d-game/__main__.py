import pygame
import background
import player
import color

def initialise():
    pygame.init()  
    screen = pygame.display.set_mode((640,480))
    background.Background(screen).draw_middle_line()
    player.Player.construct_player(screen, 20, 'Player A', 0, 10, 60).draw(color.white, 10)
    player.Player.construct_player(screen, 20, 'Player B', 0, 10, 60).draw(color.white, 10)
    main_loop()
    
def main_loop():
    done = False
    while not done:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True  
        pygame.display.update()


    
        

if __name__ == '__main__':
    initialise()