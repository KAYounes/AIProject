import pygame
from pygame import Vector2
from TextBox import TextBox
import math
class Edge:
    def __init__(self, startNode, endNode, weight = 1, color = (0, 0, 0), width = 15):
        self.startNode = startNode
        self.endNode = endNode
        self.weight = weight
        self.color = color
        self.width = width
        self.direction = 0 #> 0: no direction, 1: from start to end

        self.startingPoint = startNode.center
        self.endingPoint = endNode.center
        self.tb = TextBox(self.startingPoint.x - self.endingPoint.x, self.startingPoint.y - self.endingPoint.y)

        self.start = self.startingPoint
        self.end = self.endingPoint
        self.rad = math.pi/180
        self.rotation = self.arrow()

    def __eq__(self, edge):
        return (
            self.startingPoint == edge.startingPoint
            and
            self.endingPoint == edge.endingPoint

            or
            self.startingPoint == edge.endingPoint
            and
            self.endingPoint == edge.startingPoint
        )



    # def addWeight(self):

    def arrow(self):
        start = self.startingPoint
        end = self.endingPoint
        rad = math.pi/180
        return (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2

    def draw(self, screen, lcolor, tricolor, trirad = 10, thickness=5):
        theta = math.atan2(self.start[1] - self.end[1], self.end[0] - self.start[0])
        print(f"theta {theta}")
        m = 38
        newX = math.cos(theta) * m
        newY = math.sin(theta) * m
        if (self.start[0] <= self.end[0] and self.start[1] >= self.end[1]):
             newX = 1 * newX
             newY = -1 * newY
        if (self.start[0] > self.end[0] and self.start[1] >= self.end[1]):
             newX = 1 * newX
             newY = -1 * newY
        if (self.start[0] <= self.end[0] and self.start[1] <= self.end[1]):
             newX = 1 * newX
             newY = -1 * newY
        if (self.start[0] > self.end[0] and self.start[1] <= self.end[1]):
             newX = 1 * newX
             newY = -1 * newY


        print(math.sqrt(newX **2 + newY **2))
        print(newX)
        print(newY)
        pygame.draw.line(screen, lcolor, self.start, self.end, thickness)
        pygame.draw.polygon(screen, tricolor, ((self.end[0] - newX + trirad * math.sin(self.rotation),
                                        self.end[1] - newY + trirad * math.cos(self.rotation)),
                                       (self.end[0] - newX + trirad * math.sin(self.rotation - 120*self.rad),
                                        self.end[1] - newY + trirad * math.cos(self.rotation - 120*self.rad)),
                                       (self.end[0] - newX + trirad * math.sin(self.rotation + 120*self.rad),
                                        self.end[1] - newY + trirad * math.cos(self.rotation + 120*self.rad))))