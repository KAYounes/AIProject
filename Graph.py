import pygame
from Node import Node
from Edge import Edge

class Graph:
    def __init__(self, surface, screen, radius, directed = False):
        self.screen = screen
        self.surface = surface
        self.radius = radius
        self.margin = radius * 2 - 5 #> Outside the node
        self.padding = radius - 5  #> Inside the node
        self.nodes = []
        self.edge = []
        self.edges = []
        self.directed = directed
        self.font = pygame.font.Font(None, 40)
        self.adding = False

    def addNode(self, point):

        for node in self.nodes:
            if (node.insideNode(point, self.margin)):
                return False           

        self.nodes.append(Node(point, radius= self.radius))
        # print(self.nodes)
        self.adding = True
        return True


    def removeNode(self, point):
        for node in self.nodes:
            if (node.insideNode(point, self.padding)):
                self.nodes.remove(node)
                self.edge = []
                self.deleteEdge(node)
                return

    def addEdge(self, point):
        if (self.adding):
            self.adding = False
        else:
            for node in self.nodes:
                if (node.insideNode(point, self.margin)):

                    if (node in self.edge):
                        self.edge = []
                    else:
                        self.edge.append(node)

                    if len(self.edge) == 2:
                        if (Edge(self.edge[0], self.edge[1]) not in self.edges):
                            edge = Edge(self.edge[0], self.edge[1], self.directed,self.surface, self.screen)
                            self.edges.append(edge)
                            self.edge[0].addConnection(node, edge)
                            if not(self.directed):
                                self.edge[1].addConnection(self.edge[0], edge)


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
            node.state = state
            pygame.draw.circle(self.surface, (48, 48, 48), (node.center.x + 2, node.center.y + 2), node.radius) #> Shadow
            
            if (node in self.edge): #> Selected
                # node.color = (162, 237, 50)        
                pygame.draw.circle(self.surface, node.selectedColor, node.center, node.radius) #> Node fill

            elif (node.insideNode(point, self.padding)): #> Hovering over node
                # node.color = (100, 50, 236) 
                pygame.draw.circle(self.surface, node.hoverColor, node.center, node.radius) #> Node fill

            else: #> not Selected nor Hovering
                # node.color = (255, 255, 255)
                pygame.draw.circle(self.surface, node.defaultColor, node.center, node.radius) #> Node fill


            pygame.draw.circle(self.surface, (0,0,0), node.center, node.radius, 3) #> Node border
            

    def draw_edges(self):
        for edge in self.edges:
            edge.draw(self.surface, edge.color, (0,255,0))
            edge.tb.render(self.surface)
    

    def addWeight(self, point):
        for node in self.nodes:
            for adj in node.adjacent:
                if(adj[1].tb.rect.collidepoint(point)):
                    adj[1].weight = adj[1].tb.takeInput(self.surface, self.screen)
                    return True


    def isEmpty(self):
        return True if len(self.edges) == 0 else False

    def reset(self):
        self.nodes = []
        self.edges = []
        self.edge = []

    def printGraph(self):
        for node in self.nodes:
            print(">", node.center)
            for adj in node.adjacent:
                print(adj[1].weight)

    def breadth_first_search(self): 
        start = self.nodes[0]
        frontier = []
        frontier.append(start) 
        print(">", start.center, list(map(lambda x: x.center, frontier)))

    

        while len(frontier) != 0:
            current = frontier[0]
            frontier = frontier[1:]
            print(">> ", current.center, list(map(lambda x: x.center, frontier)))

            current.color = (255,0,0)

            if current == self.nodes[-1]: 
                current.color = (255,255,0)
                print("GOAL")
                break 

            pygame.time.wait(500)
            pygame.display.update()
            for adj in current.adjacent: #> [node, edge], [node, edge]: 
                frontier.append(adj[0])
                adj[0].color = (150, 150, 100)
                pygame.display.update()
                pygame.time.wait(500)
                self.draw_edges()
                self.draw_nodes((0,0))


        return True

    def BFS(self):
        speed = pygame.USEREVENT + 1
        pygame.time.set_timer(speed, 2750)
        
        speed2 = pygame.USEREVENT + 2
        pygame.time.set_timer(speed2, 750)

        root = self.nodes[0]
        fringe = [root]
        visited = []
        goal = self.nodes[-1]
        cost = 0
        current = None

        while(len(fringe) > 0):
            for event in pygame.event.get():
                if event.type == speed:
            
                    current  = fringe[0]
                    if (current.parent is not None):
                        current.getEdgeFromParent().color = (255,0,0)
                    visited.append(current)
                    fringe = fringe[1:]

                    current.defaultColor = (255,0,0)
                    if current == goal:
                        print("> Goal")
                        current.defaultColor = (0, 255, 255)
                        break
                        

                    for adj in current.adjacent:
                        if adj[0] not in visited:
                            adj[0].defaultColor = (150,150,150)
                            if (adj[0] not in fringe):
                                adj[0].parent = current
                            fringe.append(adj[0])
                            
                        else:
                            adj[0].defaultColor = (150,255,150)
                    

                    self.draw_nodes((0,0))
                    self.screen.blit(self.surface, (0,0))
                    pygame.display.update()

        while(goal is not None):
            print( goal.getEdgeFromParent())
            cost += goal.getEdgeFromParent().weight
            goal = goal.parent
            
        print(">>", cost)
        return True
