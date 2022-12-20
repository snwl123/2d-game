import pygame
import color

def set(text, center, transparency=255):

        # set in-built default font in pygame using 'None' which is 'freesansbold' at size 50
        font = pygame.font.Font(None, 50)

        #set text render
        txt = font.render(text, True, color.WHITE)

        # set transparency of text by (x/255)%
        txt.set_alpha(transparency)

        # set the center of the text rectangles to determine where it displays on screen
        txt_rect=txt.get_rect(center=center)
        
        return (txt, txt_rect)
