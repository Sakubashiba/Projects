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
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_UP:
                    #draw_line(windowsurface,randint(0,795), randint(0,600), randint(0,795), randint(0,600))
                    
                        
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
                    
                    xl2=xl2-1
                    xl3=xl3-5
                    xl4=xl4-2
                    xl5=xl5-2
                    xl6=xl6+5
                    xl8=xl8+2
                    xk2=xk2-5
                    xk3=xk3-5
                    xk4=xk4-5
                    xk5=xk5-5
                    xk6=xk6+5
                    xk8=xk8+5
                    xm2=xm2-5
                    xm3=xm3-5
                    xm4=xm4-5
                    xm5=xm5-5
                    xm6=xm6+5
                    
                    yl2=yl2-1
                    yl3=yl3+5
                    yl4=yl4-2
                    yl5=yl5+2
                    yl6=yl6+5
                    yl8=yl8+2
                    yk2=yk2-5
                    yk3=yk3+5
                    yk4=yk4-5
                    yk5=yk5+5
                    yk6=yk6+5
                    yk8=yk8+5
                    ym2=ym2-5
                    ym3=ym3+5
                    ym4=ym4-5
                    ym5=ym5+5
                    ym6=ym6+5
                    
                    
                    
                    if (count == 20):
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
                    
                    
                    
                    
                    break
        
        
        """
        draw_line(windowsurface,1, 100, 150, 150)
        draw_line(windowsurface,150, 150, 150, 400)
        draw_line(windowsurface,150, 400, 1, 500)
        
        draw_line(windowsurface,150, 150, 300, 200)                 #
        draw_line(windowsurface,300, 200, 300, 300)                 #Left side of the model
        draw_line(windowsurface,300, 300, 150, 400)                 #
        
        draw_line(windowsurface,300, 200, 360, 220)
        draw_line(windowsurface,360, 220, 360, 260)
        draw_line(windowsurface,360, 260, 300, 300)
        
        
        draw_line(windowsurface,800, 100, 650, 150)
        draw_line(windowsurface,650, 150, 650, 400)
        draw_line(windowsurface,650, 400, 800, 500)
        
        draw_line(windowsurface,650, 150, 500, 200)                 #
        draw_line(windowsurface,500, 200, 500, 300)                 #Right side of the model
        draw_line(windowsurface,500, 300, 650, 400)                 #
        
        draw_line(windowsurface,500, 200, 440, 220)
        draw_line(windowsurface,440, 220, 440, 260)
        draw_line(windowsurface,440, 260, 500, 300)
        
        
        
        
        
        
        draw_line(windowsurface,350, 290, 450, 290)#first line in the center
        
        #draw_line_dark(windowsurface,340, 300, 460, 300)#eraser of line 1
               
        draw_line(windowsurface,320, 320, 480, 320)
        
        draw_line(windowsurface,290, 350, 510, 350)
        
        draw_line(windowsurface,260, 380, 540, 380)
        
        draw_line(windowsurface,230, 410, 570, 410)
        
        draw_line(windowsurface,200, 440, 600, 440)
        
        draw_line(windowsurface,170, 470, 630, 470)
        
        draw_line(windowsurface,140, 500, 660, 500)
        
        draw_line(windowsurface,110, 530, 690, 530)# last line in the center
        
        
        draw_line(windowsurface,360, 223, 440, 223)#next coridor
        draw_line(windowsurface,360, 258, 440, 258)
        
        draw_line(windowsurface,5, 0, 5, 80)#top lines
        draw_line(windowsurface,50, 0, 50, 95)
        draw_line(windowsurface,100, 0, 100, 110)
        draw_line(windowsurface,150, 0, 150, 125)
        draw_line(windowsurface,200, 0, 200, 140)
        draw_line(windowsurface,250, 0, 250, 155)
        draw_line(windowsurface,300, 0, 300, 170)
        draw_line(windowsurface,350, 0, 350, 195)
        draw_line(windowsurface,400, 0, 400, 195)
        draw_line(windowsurface,450, 0, 450, 195)
        draw_line(windowsurface,500, 0, 500, 170)
        draw_line(windowsurface,550, 0, 550, 155)
        draw_line(windowsurface,600, 0, 600, 140)
        draw_line(windowsurface,650, 0, 650, 125)
        draw_line(windowsurface,700, 0, 700, 110)
        draw_line(windowsurface,750, 0, 750, 95)
        draw_line(windowsurface,795, 0, 795, 80)
        """
        
        #print(events)
        #print(pg.event.get())
          
        
        sdl2.SDL_Delay(60)
        """
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
                
            draw_line(windowsurface,1, 100, 150, 150)
            draw_line(windowsurface,150, 150, 150, 400)
            draw_line(windowsurface,150, 400, 1, 500)
            
            draw_line(windowsurface,150, 150, 300, 200)
            draw_line(windowsurface,300, 200, 300, 300)
            draw_line(windowsurface,300, 300, 150, 400)
            
            draw_line(windowsurface,650, 150, 500, 200)
            draw_line(windowsurface,500, 200, 500, 300)
            draw_line(windowsurface,500, 300, 650, 400)
            
            draw_line(windowsurface,800, 100, 650, 150)
            draw_line(windowsurface,650, 150, 650, 400)
            draw_line(windowsurface,650, 400, 800, 500)
            sdl2.SDL_Delay(10)    
            
            
            if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                #draw_rects(windowsurface, 800, 600)
                draw_line(windowsurface,1, 100, 150, 150)
                draw_line(windowsurface,150, 150, 150, 400)
                draw_line(windowsurface,150, 400, 1, 500)
                
                draw_line(windowsurface,150, 150, 300, 200)
                draw_line(windowsurface,300, 200, 300, 300)
                draw_line(windowsurface,300, 300, 150, 400)
                
                draw_line(windowsurface,650, 150, 500, 200)
                draw_line(windowsurface,500, 200, 500, 300)
                draw_line(windowsurface,500, 300, 650, 400)
                
                draw_line(windowsurface,800, 100, 650, 150)
                draw_line(windowsurface,650, 150, 650, 400)
                draw_line(windowsurface,650, 400, 800, 500)
                time.sleep(0.005)
                
                #draw_lines(windowsurface, 1, 100, 150, 150)
                #draw_lines(windowsurface, 150, 150, 150, 400)
                #draw_lines(windowsurface, 150, 400, 1, 500)
                
                print("asd")
                break
        """
        window.refresh()
    sdl2.ext.quit()
    return 0
    
    

    
    
if __name__ == "__main__":
    sys.exit(run())