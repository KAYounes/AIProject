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

    def collide(self, point):
        for node in self.nodes:
            if (node.insideNode(point, self.margin)):
                return True
                
        return False

    def addNode(self, point):
        # print("addNode")

        for node in self.nodes:
            # print(node.insideNode(point, self.margin))
            if (node.insideNode(point, self.margin)):
                return           

        self.adding = True
        self.nodes.append(Node(point))


    def removeNode(self, point):
        # print("removeNode")
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

                        # for edge in self.edges:
                        #     print(">", edge, self.edge[0].center, edge.startNode.center)
                        #     if (self.edge[0].center == edge.startNode.center or self.edge[0].center == edge.endNode.center):
                        #         print("YES")
                        if (Edge(self.edge[0], self.edge[1]) not in self.edges):
                            edge = Edge(self.edge[0], self.edge[1])
                            self.edges.append(edge)
                            self.edge[0].addAdjNode(node, edge)

                        self.edge = []

    def deleteEdge(self, node):
        deleteIndex = []
        for index, edge in enumerate(self.edges):
            if node.center == edge.startingPoint or node.center == edge.endingPoint:
                deleteIndex.append(index)
        
        for i in deleteIndex[::-1]:
            self.edges.pop(i)

    def draw_nodes(self, point):
        for node in self.nodes:
            pygame.draw.circle(self.screen, (180,180,180), (node.center.x + 4, node.center.y), self.radius)
            if (node in self.edge):
                pygame.draw.circle(self.screen, (0,0,255), node.center, self.radius)             
            elif (node.insideNode(point, self.padding)):
                pygame.draw.circle(self.screen, (0,255,0), node.center, self.radius)
            else:
                pygame.draw.circle(self.screen, (255,255,255), node.center, self.radius)
            pygame.draw.circle(self.screen, (0,0,0), node.center, self.radius, 3)

    def draw_edges(self):
        for edge in self.edges:
            edge.draw(self.screen, (0,0,0), (0,255,0))
            # edge.tb = 
            pygame.draw.line(self.screen, edge.color, edge.startingPoint, edge.endingPoint, 3)