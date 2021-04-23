import pygame
from Node import Node
from Edge import Edge

class Graph:
    def __init__(self, surface, radius):
        self.screen = surface
        self.radius = radius
        self.margin = radius * 2 - 5 #> Outside the node
        self.padding = radius - 5  #> Inside the node
        self.nodes = []
        self.edge = []
        self.edges = []
        self.font = pygame.font.Font(None, 40)
        self.adding = False

    def addNode(self, point):

        for node in self.nodes:
            if (node.insideNode(point, self.margin)):
                return False           

        self.nodes.append(Node(point, radius= self.radius))
        self.adding = True
        return True


    def removeNode(self, point):
        for node in self.nodes:
            if (node.insideNode(point, self.padding)):
                self.nodes.remove(node)
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
                            edge = Edge(self.edge[0], self.edge[1])
                            self.edges.append(edge)
                            self.edge[0].addConnection(node, edge)

                        self.edge = []

    def deleteEdge(self, node):
        deleteIndex = []
        for index, edge in enumerate(self.edges):
            if node.center == edge.startingPoint or node.center == edge.endingPoint:
                deleteIndex.append(index)
        
        for i in deleteIndex[::-1]:
            self.edges.pop(i)

    # def deleteEdge2(self, node):
    #     for adjacent in node.adjacent:
            

    def draw_nodes(self, point):
        for node in self.nodes:
            for adj in node.adjacent:
            # pygame.draw.circle(self.screen, (48, 48, 48), (node.center.x + 2, node.center.y + 2), node.radius) #> Shadow

                if (node in self.edge): #> Selected
                    node.color = (162, 237, 50)        
                elif (node.insideNode(point, self.padding)): #> Hovering over node
                    node.color = (100, 50, 236)  
                else: #> not Selected nor Hovering
                    node.color = (255, 255, 255)

                pygame.draw.circle(self.screen, node.color, node.center, node.radius) #> Node fill
                pygame.draw.circle(self.screen, (0,0,0), node.center, node.radius, 3) #> Node border
                adj[1].draw(self.screen, (0,0,0), (0,255,0))


    def draw_edges(self):
        for edge in self.edges:
            # pygame.draw.line(self.screen, edge.color, edge.startingPoint, edge.endingPoint, 3)
            edge.draw(self.screen, (0,0,0), (0,255,0))
            edge.tb.render(self.screen)
    

    def addWeight(self, point):
        for edge in self.edges:
            if (edge.tb.rect.collidepoint(point)):
                edge.weight = edge.tb.takeInput(self.screen, self)
                return True

    def printGraph(self):
        self.nodes[0].color = (255,0,0)
        self.nodes[0].adjNode()
        self.nodes[0].adjEdge()


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
            # gameGrid.paintSquare(current,(255)) 

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
