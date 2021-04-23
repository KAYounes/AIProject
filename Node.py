import pygame
from pygame import Vector2

class Node:
    state_count = 0
    def __init__(self, center, color = (255, 255, 255), radius = 30, width = 0):
        self.center = Vector2(center)
        self.color = color
        self.state = Node.state_count + 1
        self.radius = radius
        self.width = width
        self.adjacent = []
        self.edgeColor = (0, 0, 0)
    
    def insideNode(self, point, margin):
        return (
            point[0] > (self.center.x - margin) and
            point[0] < (self.center.x + margin) and
            point[1] > (self.center.y - margin) and
            point[1] < (self.center.y + margin))


    def addConnection(self, node, edge):
        self.adjacent.append([node, edge])



    
    