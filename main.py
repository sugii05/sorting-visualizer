import numpy as np
import pygame as pg 

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

class Point:
    def __init__(self, pos_x:float , pos_y: float, fixed: bool):
        self.pos_x = pos_x
        self.pos_y = pos_y 
        self.fixed = fixed
        self.vel_x = 0
        self.vel_y = 0

    
    
A = Point(300,300, False)
B = Point(500,300, True)
dist_x = (A.pos_x - B.pos_x)
dist_y = (A.pos_y - B.pos_y)
L = np.hypot(dist_x, dist_y)

running = True
A.x -= 150
while (running):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = not(running)

            dist_x = (A.pos_x - B.pos_x)
            dist_y = (A.pos_y - B.pos_y)
            current = np.hypot(dist_x, dist_y)

            if current > 0:
                error = current - L 

                

                direction_x = dist_x/current 
                direction_y = dist_y/current
                alpha = 0.6

              
                A.pos_x = A.pos_x + direction_x*error*alpha
                A.pox_y = A.pos_x + direction_y*error*alpha

            
