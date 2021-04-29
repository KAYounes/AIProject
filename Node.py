import pygame
from pygame import Vector2

class Node:
    state_count = 0
    def __init__(self, center, color = (255, 255, 255), radius = 30, width = 0):
        self.center = Vector2(center)
        self.defaultColor = (255, 255, 255)
        self.hoverColor = (100, 50, 236) 
        self.selectedColor = (162, 237, 50)  
        self.currentColor = color
        self.fringeColor = color
        self.parent = None
        self.state = 0
        self.radius = radius
        self.width = width
        self.adjacent = []
        self.edgeColor = (0, 0, 0)

    def __eq__(self, node):
        return (self.center == node.center)

    def __str__(self):
        return f"|| node center: {self.center} __ node parent: {self.parent} __ path cost from parent: {self.getEdgeFromParent().weight} ||"

    def insideNode(self, point, margin):
        return (
            point[0] > (self.center.x - margin) and
            point[0] < (self.center.x + margin) and
            point[1] > (self.center.y - margin) and
            point[1] < (self.center.y + margin))


    def addConnection(self, node, edge):
        self.adjacent.append([node, edge])

    def getEdgeFromParent(self):
        if (self.parent is None):
            return None
        for adj in self.parent.adjacent:
            if self == adj[0]:
                return adj[1]
        
        return 0



    
    