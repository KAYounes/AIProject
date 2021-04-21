
###> Imports
import pygame, sys, random
from pygame.constants import QUIT,KEYDOWN,K_UP, K_RIGHT, K_DOWN, K_LEFT, USEREVENT
from pygame import init, quit, Vector2
from TextBox import TextBox
from Graph import Graph

###> Setting up pygame
init()
pygame.mixer.pre_init(44100, -16, 2, 512) #! handles a lot of things. Used here to remove delay before sound plays
clock = pygame.time.Clock()

hor, ver = 1200, 900
pygame.display.set_caption("CAPTION")
# pygame.display.set_icon(pygame.image.load(""))
screen = pygame.display.set_mode((hor, ver))


tb = TextBox(100, 100)
g = Graph(screen, 30)


def draw_grid(width, length, size):
        for hor in range(length // size):
            pygame.draw.line(screen, (160, 160, 160), (0, size * hor), (width, size * hor))

        for ver in range(width // size):
            pygame.draw.line(screen, (160, 160, 160), (size * ver, 0), (size * ver, length))

#> Main Loop
#>
loop = True

while(loop):
    mouse = pygame.mouse.get_pos()

    #$ Event Loop
    for event in pygame.event.get():        
        #$ QUIT event
        if (event.type == QUIT):
            loop = False

        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(event.button == 1):
                if (g.addWeight(mouse)):
                    pass
                else:
                    g.addNode(mouse)
                    g.addEdge(mouse)
            elif (event.button == 3):
                g.removeNode(mouse)
            else:
                g.printGraph()
        
        

    screen.fill( (255, 255, 255))
    tb.render(screen)
    draw_grid(hor, ver, 30)
    g.draw_edges()
    g.draw_nodes(mouse)
    #$ Update Display
    pygame.display.update()
    clock.tick(60)

quit()
sys.exit()