
###> Imports
import pygame, sys, random, math
from pygame.constants import QUIT,KEYDOWN,K_UP, K_RIGHT, K_DOWN, K_LEFT, USEREVENT
from pygame import init, quit, Vector2

###> Setting up pygame
init()
pygame.mixer.pre_init(44100, -16, 2, 512) #! handles a lot of things. Used here to remove delay before sound plays
clock = pygame.time.Clock()

hor, ver = 1000, 800
pygame.display.set_caption("CAPTION")
# pygame.display.set_icon(pygame.image.load(""))
screen = pygame.display.set_mode((hor, ver))

#> Main Loop
#>
loop = True

# tri = [(0, 50), (50,0), (50,100)]
# tri_surface = pygame.Surface((100, 100))
# tri_surface.fill((255, 255, 255))
# pygame.draw.polygon(tri_surface, (255,0,0), tri)
# tri_surface = pygame.transform.rotate(tri_surface, 62.3)


def arrow(screen, lcolor, tricolor, start, end, trirad = 10, thickness=50):
    rad = math.pi/180
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    pygame.draw.polygon(screen, tricolor, ((end[0] + trirad * math.sin(rotation),
                                        end[1] + trirad * math.cos(rotation)),
                                       (end[0] + trirad * math.sin(rotation - 120*rad),
                                        end[1] + trirad * math.cos(rotation - 120*rad)),
                                       (end[0] + trirad * math.sin(rotation + 120*rad),
                                        end[1] + trirad * math.cos(rotation + 120*rad))))

while(loop):
    
    #$ Event Loop
    for event in pygame.event.get():        
        #$ QUIT event
        if (event.type == QUIT):
            loop = False
    screen.fill((255, 255, 255))
    # screen.blit(tri_surface, (100, 100))
    arrow(screen, (0,0,0), (0,255,0), (100, 70), (50,100))
    #$ Update Display
    pygame.display.update()
    clock.tick(60)

quit()
sys.exit()