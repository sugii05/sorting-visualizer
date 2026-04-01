#import numpy as np
import math 
import pygame as pg 

pg.init()
screen = pg.display.set_mode((1000, 800))
clock = pg.time.Clock()

class Point:
    def __init__(self, pos_x:float , pos_y: float, fixed: bool):
        self.x = pos_x
        self.y = pos_y 
        self.vx = 0
        self.vy = 0
        self.fixed = fixed
        
    
A = Point(500,600, False)
B = Point(500,454, False)
p1 = [A.x, A.y]
p2 = [B.x, B.y]

L = math.dist(p1,p2)
current = L

running = True
A.y -= 100
m = 10
k = 10 
c = 2
dt = 0.016
while (running):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if (current != 0):
        dx = B.x - A.x #distance between points in the x-axis. Defined from A -> B
        dy = B.y - A.y #distance between points in the y-axis

        current = math.hypot(dx, dy) #total distance between the points 

        error = current - L #offset between length of spring and current length. If current is greater than L -> we have a "positive" offeset 

        ex, ey = dx/current, dy/current #scaled both componenets to reduce to unit vector
    

    #First lets compute the force and acceleration using Hooke's law (vector valued?)
        relative_vx = B.vx - A.vx
        relative_vy = B.vy - A.vy 
        relative_v = relative_vx*ex + relative_vy*ey
        
        F = k*error + c * (relative_v)
        a = F/m
        if (A.fixed == False):
            #update velocity based on acceleration (and split into components)
            A.vx += a*dt*ex
            A.vy += a*dt*ey




            #update position
            A.x += A.vx*dt
            A.y += A.vy*dt

        if (B.fixed == False):
            #update velocity based on acelartion (and split into components)
            B.vx -=  a*dt*ex
            B.vy -=  a*dt*ey

            #update position
            B.x += B.vx*dt
            B.y += B.vy*dt
    



  














 


    screen.fill("BLACK")

    pg.draw.line(screen, "GREEN", (A.x, A.y), (B.x, B.y), 2)
    pg.draw.circle(screen, "RED", (int(A.x), int(A.y)), 8)
    pg.draw.circle(screen, "WHITE", (int(B.x), int(B.y)), 8)

    pg.display.flip()
    clock.tick(60)

pg.quit()
        
            
