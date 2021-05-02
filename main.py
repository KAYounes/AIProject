
###> Imports
import pygame, sys, random
from pygame.constants import QUIT,KEYDOWN,K_UP, K_RIGHT, K_DOWN, K_LEFT, USEREVENT
from pygame import init, quit, Vector2
from Graph import Graph
from buttons import Button
from Panel import Panel

###> Setting up pygame
init()
pygame.mixer.pre_init(44100, -16, 2, 512) #! handles a lot of things. Used here to remove delay before sound plays
clock = pygame.time.Clock()

hor, ver, panelHor = 1200, 1000, 275
grid_size = 25
pygame.display.set_caption("CAPTION")
# pygame.display.set_icon(pygame.image.load(""))
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

# button_offset = 75
# algo_Title_y = 0
# algo_Title = Button(45)
# algo_Title.btn_text = "Algorithms"
# algo_Title.cords = (0, algo_Title_y)
# algo_Title.trans = True
# algo_Title.txt_color = (0,0,0)
# algo_Title.bold = True

# uninfored_title = Button(30)
# uninfored_title.btn_text = "• Uninformed"
# uninfored_title.cords = (30, algo_Title_y + 75)
# uninfored_title.trans = True
# uninfored_title.txt_color = (0,0,0)
# uninfored_title.bold = True
# uninfored_title.render()
# # algo_Title.center = False
# bfs_btn = Button()
# bfs_btn.btn_text = "BFS Algorithm"
# bfs_btn.cords = (75, 125)
# bfs_btn.render()

# dfs_btn = Button()
# dfs_btn.btn_text = "DFS Algorithm"
# dfs_btn.cords = (button_offset, algo_Title_y + 175)
# dfs_btn.render()

# ucs_btn = Button()
# ucs_btn.btn_text = "UCS Algorithm"
# ucs_btn.cords = (button_offset, algo_Title_y + 225)
# ucs_btn.render()


# infored_title = Button(30)
# infored_title.btn_text = "• Informed"
# infored_title.cords = (30, algo_Title_y + 275)
# infored_title.trans = True
# infored_title.txt_color = (0,0,0)
# infored_title.bold = True
# infored_title.render()

# greedy_btn = Button()
# greedy_btn.btn_text = "GREEDY Algorithm"
# greedy_btn.cords = (button_offset, algo_Title_y + 325)
# greedy_btn.render()

# aStar_btn = Button()
# aStar_btn.btn_text = "A* Algorithm"
# aStar_btn.cords = (button_offset, algo_Title_y + 375)
# aStar_btn.render()


# control_Title_y = algo_Title_y + 425
# control_Title = Button(45)
# control_Title.btn_text = "Control"
# control_Title.cords = (0, control_Title_y)
# control_Title.trans = True
# control_Title.txt_color = (0,0,0)
# control_Title.bold = True
# # control_Title.center = False
# play_btn = Button()
# play_btn.btn_text = " Play Search "
# play_btn.cords = (button_offset, control_Title_y + 75)
# play_btn.render()

# stop_btn = Button()
# stop_btn.btn_text = " Stop Search "
# stop_btn.cords = (button_offset, control_Title_y + 125)
# stop_btn.render()


# graph_title_y = control_Title_y + 175
# graph_title = Button(45)
# graph_title.btn_text = "Graph"
# graph_title.cords = (0, graph_title_y)
# graph_title.trans = True
# graph_title.txt_color = (0,0,0)
# graph_title.bold = True
# # graph_title.center = False

# directed_btn = Button()
# directed_btn.btn_text = "Directed Graph"
# directed_btn.cords = (button_offset, graph_title_y + 75)
# directed_btn.render()

# clear_btn = Button()
# clear_btn.btn_text = " Clear "
# clear_btn.cords = (button_offset, graph_title_y + 125)
# clear_btn.render()
# #######################$
# algo_Title.render()

# control_Title.render()

# graph_title.render()    
# directed_btn.render()
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
                else:
                    # g.BFS()
                    g.DFS()
                    # g.printGraph()

        elif (panel.mouseOnPanel(mouse)):
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button == 1):
                    if(g.isEmpty()):
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
                    
                    elif (panel.speed_btn.detect_click()):
                        speed = panel.speed_control()

                    if (panel.showH_btn.detect_click()):
                        g.showHeuristic = panel.showH_btn.detect_toggle()



        

    canvas.fill( (255, 255, 255))
    canvas.blit(draw_grid(hor, ver, grid_size), (0,0))
    panel.fill()
    screen.fill(panelColor)
    pygame.draw.rect(screen, (0,0,0), (hor, 0, panelHor, ver), 10)
    
    panel.displayMessage("Draw a Graph, then select an algorithm to run on the graph. nl > ADD Node [Left CLick]. nl > Remove Node [Right Click]. nl > Select Node [Left Click]")
    
    g.draw_edges()
    g.draw_nodes(mouse)
    panel.draw_btns()
    panel.btnDetect_hover(mouse)
    #$ Update Display
    screen.blit(canvas, (0,0))
    screen.blit(panel.panel_surf, (panel.cordX, panel.cordY))
    pygame.display.update()
    clock.tick(60)
    # pygame.time.delay(3000)
    # loop = False
  

quit()
sys.exit()