import pygame
from enum import Enum
import math


class LineType(Enum):
    CONTINUOUS = 1
    DASHED = 2
    DOTTED = 3


class Line:
    def __init__(self, start, end, color, line_thickness, linetype = LineType.CONTINUOUS, interval_length = 10, space = 10):
        if not isinstance(linetype, LineType):
            raise ValueError("Expected LineType but got {}".format(type(linetype)))
        self.start = start
        self.end = end
        self.color = color
        self.linetype = linetype
        self.interval_length = interval_length
        self.space = space
        self.line_thickness = line_thickness

    def interval_and_total_dist(self, x, y):
        if x==0 and y ==0:
            interval_x = 0
            interval_y = 0
            total = 0
        elif x == 0:
            interval_x = 0
            interval_y = self.interval_length
            total = y
        elif y == 0:
            interval_y = 0 
            interval_x = self.interval_length
            total = x
        else:
            angle = math.atan(y/x)
            #sin(angle) = opp/hyp, opp = (sin(angle))(hyp)
            interval_y = math.sin(angle)*self.interval_length
            #cos(angle) = adj/hyp, adj = (cos(angle))(hyp)
            interval_x = math.cos(angle)*self.interval_length
            #pythagorean's theorem
            total = (x**2+y**2)**0.5
        return (interval_x, interval_y, total)

    def draw(self, screen):
        if self.linetype == LineType.CONTINUOUS:
            pygame.draw.line(screen, self.color, self.start, self.end, self.line_thickness)
        elif self.linetype == LineType.DASHED:
            start_x = self.start[0]
            start_y = self.start[1]
            end_x = self.end[0]
            end_y = self.end[1]
            dist_x = end_x-start_x
            dist_y = end_y-start_y
            dist_interval_x, dist_interval_y, dist_total = self.interval_and_total_dist(dist_x, dist_y)
            interval_count = math.floor(dist_total/self.interval_length)
            interval_count = int((interval_count-1)/2)
            if interval_count%2 != 0:
                final_x = end_x+dist_interval_x
                final_y = end_y+dist_interval_y
            else:
                final_x = dist_interval_x/2
                final_y = dist_interval_y/2
            for count in range(0,interval_count):
                end_x = start_x+dist_interval_x
                end_y = start_y+dist_interval_y
                pygame.draw.line(screen, self.color, (start_x, start_y), (end_x, end_y), self.line_thickness)
                start_x = end_x+dist_interval_x
                start_y = end_y+dist_interval_y
                count+=1
            pygame.draw.line(screen, self.color, (start_x, start_y), (start_x+final_x, start_y+final_y), self.line_thickness)







