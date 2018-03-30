import pygame, sys
from pygame.locals import *
sys.path.insert(0, '../my_canvas/')
from my_canvas_lib import *

class base_pygame:
    def __init__(self, scTitel, width, height, color):
        self.TITLE = scTitel
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.color = color
        self.canvas = Canvas(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.color)
        self.canvas_update()

    def canvas_update(self):
        pass
    
        
    def run(self):
        # VARIABLES DEFINITION
        continueFlag = True
        
        
        # PYGAME INITIALISATION
        pygame.init()
        
        screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption(self.TITLE)
        
        # PYGAME DEAD LOOP FOR RECEIVING EVENTS
        while continueFlag: # main game loop
        
            # EVENTS HANDLING
            for event in pygame.event.get():
                if event.type == QUIT:
                    continueFlag = False
                    print('pygame exit!')
                    break
                
                elif event.type == KEYDOWN:
                    keycap = event.key
                
                elif event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
        
            # PAINT THE SCREEN
            screen.fill(self.color)
            self.canvas.draw(screen)
            pygame.display.update()
            
        pygame.display.quit()
        pygame.quit()
