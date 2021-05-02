import pygame, sys
from Node import Node
from Edge import Edge
from queue import PriorityQueue

class Graph:
    def __init__(self, surface, screen, radius, directed = False):
        self.surface = surface
        self.screen = screen
        self.radius = radius
        self.margin = radius * 2 - 5 #> Outside the node
        self.padding = radius - 5  #> Inside the node
        self.nodes = []
        self.edge = []
        self.edges = []
        self.directed = directed
        self.font = pygame.font.Font("RobotoCondensed-Regular.ttf", 20)
        self.adding = False
        self.showHeuristic = False

    def addNode(self, point):

        for node in self.nodes:
            if (node.insideNode(point, self.margin)):
                return False           

        self.nodes.append(Node(point, radius= self.radius))
        self.adding = True
        return True


    def removeNode(self, point):
        for nodeA in self.nodes:
            if (nodeA.insideNode(point, self.padding)):
                for nodeB in self.nodes:
                    nodeB.removeConnection(nodeA)
                    nodeB.color = Node.default_color
                self.nodes.remove(nodeA)
                self.edge = []
                self.deleteEdge(nodeA)
                return


    def addEdge(self, point):
        if (self.adding):
            self.adding = False
        else:
            for node in self.nodes:
                if (node.insideNode(point, self.padding)):

                    if (node in self.edge):
                        self.edge = []
                        node.color = Node.default_color
                    else:
                        self.edge.append(node)

                    if len(self.edge) == 2:
                        if (Edge(self.edge[0], self.edge[1]) not in self.edges):
                            edge = Edge(self.edge[0], self.edge[1], self.directed,self.surface, self.screen)
                            self.edges.append(edge)
                            self.edge[0].addConnection(node, edge)
                            if not(self.directed):
                                self.edge[1].addConnection(self.edge[0], edge)
                        
                        self.edge[0].color = Node.default_color


                        self.edge = []


    def deleteEdge(self, node):
        deleteIndex = []
        for index, edge in enumerate(self.edges):
            if node.center == edge.startingPoint or node.center == edge.endingPoint:
                deleteIndex.append(index)
        
        for i in deleteIndex[::-1]:
            self.edges.pop(i)


    def draw_nodes(self, point):

        for state,node in enumerate(self.nodes):

            if (node.type == "G"):
                node.state = "G"
            else:
                node.state = "S" + str(state)


            pygame.draw.circle(self.surface, (48, 48, 48), (node.center.x + 2, node.center.y + 2), node.radius) #> Shadow
            
            if (node in self.edge): #> Selected
                node.color = Node.selected_color
            
            pygame.draw.circle(self.surface, node.color, node.center, node.radius) #> Node fill
    
            node.draw_state(self.font, self.surface)

            if (self.showHeuristic):
                node.tb.render(self.surface, self.font)

            if (node.insideNode(point, self.padding)): #> Hovering over node
                # node.color = node.hovered_color
                pygame.draw.circle(self.surface, Node.hovered_color, node.center, node.radius, 4) #> Node fill
            else:
                pygame.draw.circle(self.surface, (0,0,0), node.center, node.radius, 3) #> Node border
            

    def draw_edges(self):
        for edge in self.edges:
            edge.draw(self.surface, edge.color, (0,255,0))
            edge.tb.render(self.surface, self.font)
    

    def addWeight(self, point):
        for node in self.nodes:
            if (node.tb.rect.collidepoint(point) and self.showHeuristic):
                node.heuristic = node.tb.takeInput(self.surface, self.screen, self.font)
                return True
            else:
                for adj in node.adjacent:
                    if(adj[1].tb.rect.collidepoint(point)):
                        adj[1].weight = adj[1].tb.takeInput(self.surface, self.screen, self.font)
                        return True


    def isEmpty(self):
        return True if len(self.edges) == 0 else False


    def reset(self):
        self.nodes = []
        self.edges = []
        self.edge = []
        self.reset_nodes()


    def printGraph(self):
        for node in self.nodes:
            print(node)


    def get_path_cost(self, current):
        cost = 0
        while(current.parent is not None):
            edge = current.getEdgeFromParent()
            cost += edge.weight
            edge.color = (76, 82, 245)
            current = current.parent
            print(">> Cost", cost)

 
    def start_goal_states(self, point):
        for node in self.nodes:
            if(node.insideNode(point, self.padding)):
                return node


    def runAlgorithm(self, panel, grid_surf, algorithm, speed):
        loop = True
        start_state = None
        goal_states = []
        message = ""

        message = "Please select ONE START state"
        while(loop):
            mouse = pygame.mouse.get_pos()

            #$ Event Loop
            for event in pygame.event.get():        
                #$ QUIT event
                if (event.type == pygame.QUIT):
                    loop = False
                    pygame.quit()
                    sys.exit()
                if(event.type == pygame.MOUSEBUTTONDOWN):

                    if(panel.mouseOnPanel(mouse)):

                        if (panel.showH_btn.detect_click()):
                            self.showHeuristic = panel.showH_btn.detect_toggle()
                        
                        elif (panel.speed_btn.detect_click()):
                            speed = panel.speed_control()

                        elif (panel.play_btn.detect_click()):
                            if (start_state is not None and len(goal_states) > 0):
                                panel.play_btn.detect_toggle()
                                if (algorithm == "BFS"):
                                    self.BFS(start_state, goal_states, speed)

                                elif (algorithm == "UCS"):
                                    print("Run UCS")
                                    self.UCS(start_state, goal_states, speed)

                                elif (algorithm == "DFS"):
                                    self.DFS(start_state, goal_states, speed)

                                message = "Algorithm has finished execution. nl Press stop search to return back to drawing."

                        elif(panel.stop_btn.detect_click()):
                            panel.play_btn.toggled = False
                            loop = False
                            self.reset_nodes()
                            start_state = None
                            goal_states = []
                            return True

                    else: #$ If click on canvas
                        node = self.start_goal_states(mouse)
                        if (node is not None):
                            if (start_state is None):
                                message = "Please select at least one GOAL state. nl Then press PLAY SEARCH to begin."
                                node.color = Node.start_state_color
                                node.type = "S"
                                start_state = node
                            elif(start_state is not node):
                                node.color = Node.goal_state_color
                                node.type = "G"
                                goal_states.append(node)
            
            panel.fill()
            self.surface.fill((255, 255, 255))
            self.surface.blit(grid_surf, (0,0))
            

            panel.btnDetect_hover(mouse)
            panel.draw_btns()
            panel.displayMessage(message)

            self.draw_edges()
            self.draw_nodes(mouse)
            
            self.screen.blit(self.surface, (0,0))
            self.screen.blit(panel.panel_surf, (panel.cordX, panel.cordY))
            pygame.display.update()


    def BFS(self, start_state, goal_states, speed = 750):
        #> Potential Bug
            #$ Calling BFS with 1 node returns the last calculated cost

        speed_event = pygame.USEREVENT + 1
        pygame.time.set_timer(speed_event, speed)

        root = start_state
        fringe = [root]
        visited = []
        goal = goal_states
        cost = 0
        current = None

        while(len(fringe) > 0):
            for event in pygame.event.get():
                if event.type == speed_event:
            
                    current = fringe[0]
                    if (current.parent is not None):
                        current.getEdgeFromParent().color = (143, 115, 104)
                    visited.append(current)
                    fringe = fringe[1:]

                    current.color = Node.current_node_color
                    if current in goal:
                        current.color = Node.goal_state_color
                        self.get_path_cost(current)
                        return True
                        

                    for adj in current.adjacent:
                        if adj[0] not in visited:
                            adj[0].color = Node.in_fringe_color
                            if (adj[0] not in fringe):
                                adj[0].parent = current
                            fringe.append(adj[0])
                            
                        else:
                            adj[0].color = Node.visited_color
                    

                    self.draw_edges()
                    self.draw_nodes((0,0))
                    self.screen.blit(self.surface, (0,0))
                    pygame.display.update()


    def UCS(self, start_state, goal_states, speed = 750):
            speed_event = pygame.USEREVENT + 1
            pygame.time.set_timer(speed_event, speed)

            root = start_state
            counter = 0
            fringe = PriorityQueue()
            fringe.put((0, counter, root))  # the counter is used to differentiate between elements with the same weight
            visited = []

            while not fringe.empty():
                for event in pygame.event.get():
                    if event.type == speed_event:
                        
                        item_out = fringe.get()
                        current = item_out[2]
                        visited.append(current)

                        print("> Current ", current)
                        print("> Goals ")
                        list(map(lambda x: print(x), goal_states))
                        if (current.parent is not None):
                            current.getEdgeFromParent().color = (143, 115, 104)


                        if current in goal_states:
                            current.color = Node.goal_state_color
                            self.get_path_cost(current)
                            return

                        for adj in current.adjacent:
                            betterSol = current.total_cost + adj[1].weight < adj[0].total_cost
                            adj[0].color = Node.in_fringe_color

                            if adj[0] not in visited:

                                if (adj[0].parent is None):
                                    adj[0].parent = current
                                    adj[0].total_cost = adj[0].parent.total_cost + adj[1].weight
                                    counter += 1                                                            
                                    fringe.put((adj[0].total_cost, counter, adj[0]))
                                    visited.append(adj[0])

                            elif betterSol:
                                adj[0].parent = current
                                adj[0].total_cost = adj[0].parent.total_cost + adj[1].weight
                                # betterSol = True

                                counter += 1                                                            
                                fringe.put((adj[0].total_cost, counter, adj[0]))

                        current.color = Node.current_node_color

                        self.draw_edges()
                        self.draw_nodes((0, 0))
                        self.screen.blit(self.surface, (0, 0))
                        pygame.display.update()


    def DFS(self, start_state, goal_states, speed = 750):

        # > Potential Bug
        # $ Calling BFS with 1 node returns the last calculated cost

        speed_event = pygame.USEREVENT + 1
        pygame.time.set_timer(speed_event, speed)

        root = start_state
        fringe = []
        fringe.append(root)
        visited = []

        goal = goal_states
        cost = 0

        while (len(fringe) > 0):
            for event in pygame.event.get():

                if event.type == speed_event:
                    current = fringe.pop()

                    if (current.parent is not None):
                        current.getEdgeFromParent().color = (143, 115, 104)

                    visited.append(current)

                    current.color = Node.current_node_color
                    print(current)

                    if current in goal_states:
                        current.color = Node.goal_state_color
                        running = False
                        self.get_path_cost(current)
                        return

                    for adj in current.adjacent:
                        if adj[0] not in visited:
                            adj[0].color = Node.in_fringe_color

                            if (adj[0] not in fringe):
                                adj[0].parent = current
                            fringe.append(adj[0])

                        # else:
                            # adj[0].color = Node.visited_color

                    self.draw_edges()
                    self.draw_nodes((0, 0))
                    self.screen.blit(self.surface, (0, 0))
                    pygame.display.update()

        return False


    def reset_nodes(self):
        for node in self.nodes:
            node.color = Node.default_color
            node.total_cost = 0
            node.parent = None
            node.type = ""

        for edge in self.edges:
            edge.color = (0,0,0)

