
###> Imports
import pygame, sys, random
from pygame.constants import QUIT,KEYDOWN,K_UP, K_RIGHT, K_DOWN, K_LEFT, USEREVENT
from pygame import init, quit, Vector2
from Graph import Graph

###> Setting up pygame
init()
pygame.mixer.pre_init(44100, -16, 2, 512) #! handles a lot of things. Used here to remove delay before sound plays
clock = pygame.time.Clock()

hor, ver, rightPanel = 1200, 900, 500
pygame.display.set_caption("CAPTION")
# pygame.display.set_icon(pygame.image.load(""))
screen = pygame.Surface((hor, ver))
full_screen = pygame.display.set_mode((hor + rightPanel, ver))


g = Graph(screen, 25)

def drawRightPanel(rightPanel):
    pygame.draw.rect(full_screen, (227, 254, 213), (hor, 0, rightPanel, ver))
    pygame.draw.rect(full_screen, (0, 0, 0), (hor, 0, rightPanel, ver), 8)
    

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
                # elif (g.adding):
                else:
                    g.addNode(mouse)
                    g.addEdge(mouse)
            elif (event.button == 3):
                g.removeNode(mouse)
            else:
                g.breadth_first_search()

        

    screen.fill( (255, 255, 255))
    full_screen.fill((227, 254, 213))
    draw_grid(hor, ver, 25)
    drawRightPanel(rightPanel)
    # g.draw_edges()
    g.draw_nodes(mouse)
    #$ Update Display
    full_screen.blit(screen, (0,0))
    pygame.display.update()
    clock.tick(60)

quit()
sys.exit()