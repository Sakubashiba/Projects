import sys
from random import randint
import sdl2
import sdl2.ext
import time
import pygame as pg


def draw_lines(surface, width1, height1, width2 , height2):
    # Fill the whole surface with a black color.
    sdl2.ext.fill(surface, 0)
    #for x in range(15):
        # Create a set of four random points for drawing the line.
    x1, x2 = width1, width2 #randint(0, width), randint(0, width)
    y1, y2 = height1, height2 #randint(0, height), randint(0, height)
    # Create a random color.
    color = sdl2.ext.Color(randint(0, 255),
                           randint(0, 255),
                           randint(0, 255))
    # Draw the line with the specified color on the surface.
    # We also could create a set of points to be passed to the function
    # in the form
    #
    # line(surface, color, (x1, y1, x2, y2, x3, y3, x4, y4, ...))
    #                       ^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^
    #                         first line     second line
    sdl2.ext.line(surface, color, (x1, y1, x2, y2))

def draw_line(surface,x1,y1,x2,y2):
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),randint(70, 255),randint(70, 255)), (x1, y1, x2, y2))

def draw_line_dark(surface,x1,y1,x2,y2):
    sdl2.ext.line(surface, sdl2.ext.Color(0,0,0), (x1, y1, x2, y2))
    
def draw_rects(surface, width, height):
    # Fill the whole surface with a black color.
    sdl2.ext.fill(surface, 0)
    for k in range(5):
        # Create a set of four random points for the edges of the rectangle.
        x, y = 5,100#randint(0, width), randint(0, height)
        w, h = 60,30#randint(1, width // 2), randint(1, height // 2)
        # Create a random color.
        color = sdl2.ext.Color(randint(0, 255),
                               randint(0, 255),
                               randint(0, 255))
        # Draw the filled rect with the specified color on the surface.
        # We also could create a set of points to be passed to the function
        # in the form
        #
        # fill(surface, color, ((x1, y1, x2, y2), (x3, y3, x4, y4), ...))
        #                        ^^^^^^^^^^^^^^    ^^^^^^^^^^^^^^
        #                          first rect        second rect
        sdl2.ext.fill(surface, color, (x, y, w, h))

    
    






def run():
    # You know those from the helloworld.py example.
    # Initialize the video subsystem, create a window and make it visible.
    sdl2.ext.init()
    window = sdl2.ext.Window("Fps game Test", size=(800, 600))
    window.show()
    
    windowsurface = window.get_surface()
    count = 0
    xl1 = 1
    xl2 = 100
    xl3 = 150
    xl4 = 150
    xl5 = 150
    xl6 = 400
    xl7 = 1
    xl8 = 500 
    xk1 = 150
    xk2 = 150
    xk3 = 300
    xk4 = 200
    xk5 = 300
    xk6 = 300
    xk7 = 150
    xk8 = 400
    xm1 = 300
    xm2 = 200
    xm3 = 360
    xm4 = 220
    xm5 = 360
    xm6 = 260
    
    yl1 = 800
    yl2 = 100
    yl3 = 650
    yl4 = 150
    yl5 = 650
    yl6 = 400
    yl7 = 800
    yl8 = 500 
    yk1 = 650
    yk2 = 150
    yk3 = 500
    yk4 = 200
    yk5 = 500
    yk6 = 300
    yk7 = 650
    yk8 = 400
    ym1 = 500
    ym2 = 200
    ym3 = 440
    ym4 = 220
    ym5 = 440
    ym6 = 260
    
    
    
    
    
    
    running = True
    
    while running:
        
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
                
        draw_line_dark(windowsurface,xl1, xl2, xl3, xl4)
        draw_line_dark(windowsurface,xl3, xl4, xl5, xl6)
        draw_line_dark(windowsurface,xl5, xl6, xl7, xl8)

        draw_line_dark(windowsurface,xl3, xl4, xk3, xk4)                 #
        draw_line_dark(windowsurface,xk3, xk4, xk5, xk6)                 #Left side of the model
        draw_line_dark(windowsurface,xk5, xk6, xl5, xl6)                 #
     
        draw_line_dark(windowsurface,xk3, xk4, xm3, xm4)
        draw_line_dark(windowsurface,xm3, xm4, xm5, xm6)
        draw_line_dark(windowsurface,xm5, xm6, xk5, xk6)
        
        
        draw_line_dark(windowsurface,yl1, yl2, yl3, yl4)
        draw_line_dark(windowsurface,yl3, yl4, yl5, yl6)
        draw_line_dark(windowsurface,yl5, yl6, yl7, yl8)
        
        draw_line_dark(windowsurface,yl3, yl4, yk3, yk4)                 #
        draw_line_dark(windowsurface,yk3, yk4, yk5, yk6)                 #Right side of the model
        draw_line_dark(windowsurface,yk5, yk6, yl5, yl6)                 #
        
        draw_line_dark(windowsurface,yk3, yk4, ym3, ym4)
        draw_line_dark(windowsurface,ym3, ym4, ym5, ym6)
        draw_line_dark(windowsurface,ym5, ym6, yk5, yk6)
        
        draw_line_dark(windowsurface,ym3, ym4, xm3, xm4)
        draw_line_dark(windowsurface,ym5, ym6, xm5, xm6)
        
        draw_line_dark(windowsurface,yk5, yk6, xk5, xk6)
        draw_line_dark(windowsurface,yl5, yl6, xl5, xl6)
        
        
        xl2=xl2-randint(-10,10)
        xl3=xl3-randint(-10,10)
        xl4=xl4-randint(-10,10)
        xl5=xl5-randint(-10,10)
        xl6=xl6+randint(-10,10)
        xl8=xl8+randint(-10,10)
        xk2=xk2-randint(-10,10)
        xk3=xk3-randint(-10,10)
        xk4=xk4-randint(-10,10)
        xk5=xk5-randint(-10,10)
        xk6=xk6+randint(-10,10)
        xk8=xk8+randint(-10,10)
        xm2=xm2-randint(-10,10)
        xm3=xm3-randint(-10,10)
        xm4=xm4-randint(-10,10)
        xm5=xm5-randint(-10,10)
        xm6=xm6+randint(-10,10)
                        
        yl2=yl2-randint(-10,10)
        yl3=yl3+randint(-10,10)
        yl4=yl4-randint(-10,10)
        yl5=yl5+randint(-10,10)
        yl6=yl6+randint(-10,10)
        yl8=yl8+randint(-10,10)
        yk2=yk2-randint(-10,10)
        yk3=yk3+randint(-10,10)
        yk4=yk4-randint(-10,10)
        yk5=yk5+randint(-10,10)
        yk6=yk6+randint(-10,10)
        yk8=yk8+randint(-10,10)
        ym2=ym2-randint(-10,10)
        ym3=ym3+randint(-10,10)
        ym4=ym4-randint(-10,10)
        ym5=ym5+randint(-10,10)
        ym6=ym6+randint(-10,10)
        
        
        
        if (count == 200):
            count = 0
            xl1 = 1
            xl2 = 100
            xl3 = 150
            xl4 = 150
            xl5 = 150
            xl6 = 400
            xl7 = 1
            xl8 = 500 
            xk1 = 150
            xk2 = 150
            xk3 = 300
            xk4 = 200
            xk5 = 300
            xk6 = 300
            xk7 = 150
            xk8 = 400
            xm1 = 300
            xm2 = 200
            xm3 = 360
            xm4 = 220
            xm5 = 360
            xm6 = 260
            
            
            yl1 = 800
            yl2 = 100
            yl3 = 650
            yl4 = 150
            yl5 = 650
            yl6 = 400
            yl7 = 800
            yl8 = 500 
            yk1 = 650
            yk2 = 150
            yk3 = 500
            yk4 = 200
            yk5 = 500
            yk6 = 300
            yk7 = 650
            yk8 = 400
            ym1 = 500
            ym2 = 200
            ym3 = 440
            ym4 = 220
            ym5 = 440
            ym6 = 260
            
        
        
        count = count + 1
        
        
        draw_line(windowsurface,xl1, xl2, xl3, xl4)
        draw_line(windowsurface,xl3, xl4, xl5, xl6)
        draw_line(windowsurface,xl5, xl6, xl7, xl8)
        
        draw_line(windowsurface,xl3, xl4, xk3, xk4)                 #
        draw_line(windowsurface,xk3, xk4, xk5, xk6)                 #Left side of the model
        draw_line(windowsurface,xk5, xk6, xl5, xl6)                 #
        
        draw_line(windowsurface,xk3, xk4, xm3, xm4)
        draw_line(windowsurface,xm3, xm4, xm5, xm6)
        draw_line(windowsurface,xm5, xm6, xk5, xk6)
        
    
        draw_line(windowsurface,yl1, yl2, yl3, yl4)
        draw_line(windowsurface,yl3, yl4, yl5, yl6)
        draw_line(windowsurface,yl5, yl6, yl7, yl8)
    
        draw_line(windowsurface,yl3, yl4, yk3, yk4)                 #
        draw_line(windowsurface,yk3, yk4, yk5, yk6)                 #Right side of the model
        draw_line(windowsurface,yk5, yk6, yl5, yl6)                 #
        
        draw_line(windowsurface,yk3, yk4, ym3, ym4)
        draw_line(windowsurface,ym3, ym4, ym5, ym6)
        draw_line(windowsurface,ym5, ym6, yk5, yk6)
        
        draw_line(windowsurface,ym3, ym4, xm3, xm4)                 #Front 
        draw_line(windowsurface,ym5, ym6, xm5, xm6)
        
        draw_line(windowsurface,yk5, yk6, xk5, xk6)                 #floor
        draw_line(windowsurface,yl5, yl6, xl5, xl6)
        
        sdl2.SDL_Delay(60)
        
        window.refresh()
    sdl2.ext.quit()
    return 0
    
    

    
    
if __name__ == "__main__":
    sys.exit(run())