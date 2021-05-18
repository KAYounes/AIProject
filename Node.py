import pygame
from pygame import Vector2
from TextBox import TextBox
class Node:
    default_color = (255, 255, 255)
    hovered_color = (50, 50, 237) #$ (140, 103, 240) #$ old color (100, 50, 236) 
    selected_color = (162, 237, 50)  
    current_node_color = (255, 140, 78)
    in_fringe_color = (149, 162, 169)
    start_state_color = (116, 255, 41)
    goal_state_color = (255, 237, 40)
    visited_color = (245, 95, 95)

    def __init__(self, center, radius = 30, width = 0):
        self.center = Vector2(center)
        self.radius = radius
        self.width = width

        self.color = Node.default_color

        self.adjacent = []
        self.parent = None
        self.parents = []
        self.state = ""
        self.heuristic = 1
        self.total_cost = 0
        self.f_cost = 0
        self.type = ""

        self.selected = False

        self.tb = TextBox(self.center.x, self.center.y - self.radius * 1.7, 42, 23,allowZero=True)

    def __eq__(self, node):
        return (self.center == node.center)

    def __str__(self):
        return f"State {self.state}" # - Adjacent: {list(map(lambda x: x[0].state, self.adjacent))}"
#     def __str__(self):
#         return f"""---------------------------- 
# state: {self.state}\n
# center: {self.center}\n
# parent: {self.parent.state if self.parent is not None else "No parent"}\n
# cost from parent: {self.getEdgeFromParent().weight if self.parent is not None else "No parent"}\n
# Total cost parent: {self.total_cost}\n
# heuristic: {self.heuristic}
# ----------------------------
#"""

    def insideNode(self, point, margin):
        return (
            point[0] > (self.center.x - margin) and
            point[0] < (self.center.x + margin) and
            point[1] > (self.center.y - margin) and
            point[1] < (self.center.y + margin))


    def addConnection(self, node, edge):
        self.adjacent.append([node, edge])

    def removeConnection(self, node):
        for adj in self.adjacent:
            if node == adj[0]:
                self.adjacent.remove(adj)
        


    def getEdgeFromParent(self):
        if (self.parent is None):
            return None
        for adj in self.parent.adjacent:
            if self == adj[0]:
                return adj[1]
        
        return 0

    def draw_state(self, font, surface):
        state_surface = font.render(self.state, True, (0,0,0))
        state_rect = state_surface.get_rect()
        state_rect.center = self.center
        surface.blit(state_surface, state_rect)
        
        # return state_surface, state_surface.get_rect()

    def update_f_cost(self):
        self.f_cost = self.total_cost + self.heuristic
    
    