
###> Imports
import pygame, sys, random
from pygame.constants import QUIT,KEYDOWN,K_UP, K_RIGHT, K_DOWN, K_LEFT, SHOWN, USEREVENT
from pygame import init, quit, Vector2
from Graph import Graph
from buttons import Button
from Panel import Panel

###> Setting up pygame
init()
pygame.mixer.pre_init(44100, -16, 2, 512) #! handles a lot of things. Used here to remove delay before sound plays
clock = pygame.time.Clock()

w = int(input("Please enter the horizontal resolution of your screen: "))
h = int(input("Please enter the vertical resolution of your screen: "))
print(f"The program should have started with a window size of {w} x {h}")
print("If the program window is not fully visible then please enter a larger resolution, else change the resolution of your screen")
w = w - 400
h = h - 60
hor, ver, panelHor = w, h, 375
grid_size = 25
pygame.display.set_caption("Graph Search Visualizer")
pygame.display.set_icon(pygame.image.load("icon.png"))
canvas = pygame.Surface((hor, ver))
# panelSurf = pygame.Surface((panelHor - grid_size, ver - grid_size*2))
panel = Panel(hor + grid_size // 2, grid_size // 2, panelHor - grid_size, ver - grid_size , (164, 250, 107))
screen = pygame.display.set_mode((hor + panelHor, ver))
#> Colors
panelColor = (164, 250, 107) #(136, 248, 71)

#> Buttons
g = Graph(canvas, screen, 25, False)
Button.surfaceX = hor + grid_size // 2
Button.surfaceY = grid_size // 2

def draw_grid(width, length, size):
    grid_surf = pygame.Surface((width, length))
    grid_surf.set_colorkey((0, 0, 0))

    for hor in range(length // size):
        pygame.draw.line(grid_surf, (160, 160, 160), (0, size * hor), (width, size * hor))

    for ver in range(width // size):
        pygame.draw.line(grid_surf, (160, 160, 160), (size * ver, 0), (size * ver, length))

    return grid_surf


#> Main Loop
#>
loop = True
speed = 250
show = True

while(loop):
    mouse = pygame.mouse.get_pos()

    #$ Event Loop
    for event in pygame.event.get():        
        #$ QUIT event
        if (event.type == QUIT):
            loop = False

        if(canvas.get_rect().collidepoint(mouse)):
            if(event.type == pygame.MOUSEBUTTONDOWN):

                if(event.button == 1):
                    if not(g.addWeight(mouse)):
                        g.addNode(mouse)
                        g.addEdge(mouse)
                elif (event.button == 3):
                    g.removeNode(mouse)

        elif (panel.mouseOnPanel(mouse)):
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button == 1):
                    if(g.isEmpty() and panel.directed_btn.detect_click()):
                        g.directed = panel.directed_btn.detect_toggle()
                    
                    if(panel.clear_btn.detect_click()):
                        g.reset()

                    elif(panel.bfs_btn.detect_click()):
                        panel.bfs_btn.detect_toggle()
                        g.runAlgorithm(panel, draw_grid(hor, ver, grid_size), "BFS", speed)
                        panel.bfs_btn.toggled = False

                    elif(panel.ucs_btn.detect_click()):
                        panel.ucs_btn.detect_toggle()
                        g.runAlgorithm(panel, draw_grid(hor,ver, grid_size), "UCS", speed)
                        panel.ucs_btn.toggled = False

                    elif(panel.dfs_btn.detect_click()):
                        panel.dfs_btn.detect_toggle()
                        g.runAlgorithm(panel, draw_grid(hor,ver, grid_size), "DFS", speed) 
                        panel.dfs_btn.toggled = False
                    
                    elif(panel.ID_btn.detect_click()):
                        panel.ID_btn.detect_toggle()
                        max_depth = (g.input_depth_limit(mouse))
                        g.runAlgorithm(panel, draw_grid(hor,ver, grid_size), "ITD", speed, max_depth) 
                        panel.ID_btn.toggled = False

                    elif(panel.DLS_btn.detect_click()):
                        panel.DLS_btn.detect_toggle()
                        max_depth = (g.input_depth_limit(mouse))
                        g.runAlgorithm(panel, draw_grid(hor,ver, grid_size), "DLS", speed, max_depth) 
                        panel.DLS_btn.toggled = False

                    elif(panel.greedy_btn.detect_click()):
                        panel.greedy_btn.detect_toggle()
                        g.runAlgorithm(panel, draw_grid(hor,ver, grid_size), "GRY", speed) 
                        panel.greedy_btn.toggled = False

                    elif(panel.aStar_btn.detect_click()):
                        panel.aStar_btn.detect_toggle()
                        g.runAlgorithm(panel, draw_grid(hor,ver, grid_size), "AST", speed) 
                        panel.aStar_btn.toggled = False

                    elif (panel.speed_btn.detect_click()):
                        speed = panel.speed_control()

                    if (panel.showH_btn.detect_click()):
                        g.showHeuristic = panel.showH_btn.detect_toggle()

                    if (panel.showC_btn.detect_click()):
                        g.showCost = panel.showC_btn.detect_toggle()                   


    canvas.fill( (255, 255, 255))
    canvas.blit(draw_grid(hor, ver, grid_size), (0,0))
    panel.fill()
    screen.fill(panelColor)
    pygame.draw.rect(screen, (0,0,0), (hor, 0, panelHor, ver), 10)
    
    panel.displayMessage("Draw a Graph, then select an algorithm to run on the graph. nl > ADD Node [Left CLick]. nl > Remove Node [Right Click]. nl > Select Node [Left Click]")
    
    g.draw_edges()
    g.draw_nodes(mouse)
    # g.input_depth_limit(mouse)
    # box = pygame.Rect(500, 300, 50, 50)#prompt_rect.width + 20, prompt_rect.height + 30)
    # pygame.draw.rect(canvas, (0,0,0), box)

    panel.draw_btns()
    panel.btnDetect_hover(mouse)

    #$ Update Display
    screen.blit(canvas, (0,0))
    screen.blit(panel.panel_surf, (panel.cordX, panel.cordY))

    pygame.display.update()
    clock.tick(60)

    #> One loop only (Debugging)
    # pygame.time.delay(3000)
    # loop = False
  

quit()
sys.exit()