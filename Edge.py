import pygame
from TextBox import TextBox
import math

class Edge:
    def __init__(self, startNode, endNode, directed = False, weight = 1, color = (0, 0, 0), width = 15):
        self.startNode = startNode
        self.endNode = endNode
        self.weight = 1
        self.color = (0, 0, 0)
        self.width = width
        self.directed = directed

        self.startingPoint = startNode.center
        self.endingPoint = endNode.center
        self.tb = TextBox((self.startingPoint.x + self.endingPoint.x) // 2, (self.startingPoint.y + self.endingPoint.y) // 2)

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


    def arrow(self):
        start = self.startingPoint
        end = self.endingPoint
        rad = math.pi/180
        return (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2

    def draw(self, screen, lcolor, tricolor, trirad = 13, thickness=6):
        pygame.draw.line(screen, lcolor, self.start, self.end, thickness)

        if (self.directed):
            theta = math.atan2(self.start[1] - self.end[1], self.end[0] - self.start[0])
            
            m = 25 + 9
            newX = math.cos(theta) * m
            newY = -math.sin(theta) * m


            pygame.draw.polygon(screen, tricolor, ((self.end[0] - newX + trirad * math.sin(self.rotation),
                                            self.end[1] - newY + trirad * math.cos(self.rotation)),
                                        (self.end[0] - newX + trirad * math.sin(self.rotation - 120*self.rad),
                                            self.end[1] - newY + trirad * math.cos(self.rotation - 120*self.rad)),
                                        (self.end[0] - newX + trirad * math.sin(self.rotation + 120*self.rad),
                                        self.end[1] - newY + trirad * math.cos(self.rotation + 120*self.rad))))

                                    