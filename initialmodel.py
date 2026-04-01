#import numpy as np
import math 
import pygame as pg 

pg.init()
screen = pg.display.set_mode((1000, 800))
clock = pg.time.Clock()

class Point:
    def __init__(self, pos_x:float , pos_y: float, fixed: bool):
        self.pos_x = pos_x
        self.pos_y = pos_y 
        self.fixed = fixed
        
    
A = Point(900,600, False)
B = Point(980,454, False)
p1 = [A.pos_x, A.pos_y]
p2 = [B.pos_x, B.pos_y]
L = math.dist(p1,p2)

running = True

A.pos_y -= 0
A.pos_x-= 0

while (running):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    dist_x = B.pos_x - A.pos_x
    dist_y = B.pos_y - A.pos_y


    current = math.hypot(dist_x, dist_y)

    if current > 0.05:
        error = current - L 


        direction_x = dist_x/current 
        direction_y = dist_y/current

        alpha = 0.25
        if (A.fixed == False):  
            
            A.pos_x = A.pos_x + direction_x*error*alpha
            
            A.pos_y = A.pos_y + direction_y*error*alpha
        if B.fixed == False:
            B.pos_x += -1*direction_x*error*alpha 
            B.pos_y += -1*direction_y*error*alpha 


    screen.fill("BLACK")

    pg.draw.line(screen, "GREEN", (A.pos_x, A.pos_y), (B.pos_x, B.pos_y), 2)
    pg.draw.circle(screen, "RED", (int(A.pos_x), int(A.pos_y)), 8)
    pg.draw.circle(screen, "WHITE", (int(B.pos_x), int(B.pos_y)), 8)

    pg.display.flip()
    clock.tick(60)

pg.quit()
        
            
