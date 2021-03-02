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

def draw_lineRect(surface,x1,y1,x2,y2,x3,y3,x4,y4): #X is <----->     y is /\  \/
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x1, y1, x2, y2))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x2, y2, x3, y3))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x3, y3, x4, y4))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x4, y4, x1, y1))
    
def draw_lineRect_dark(surface,x1,y1,x2,y2,x3,y3,x4,y4): #X is <----->     y is /\  \/
    sdl2.ext.line(surface, sdl2.ext.Color(0,0,0), (x1, y1, x2, y2))
    sdl2.ext.line(surface, sdl2.ext.Color(0,0,0), (x2, y2, x3, y3))
    sdl2.ext.line(surface, sdl2.ext.Color(0,0,0), (x3, y3, x4, y4))
    sdl2.ext.line(surface, sdl2.ext.Color(0,0,0), (x4, y4, x1, y1))

def draw_lineCube(surface,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8): #X is <----->     y is /\  \/
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x1, y1, x2, y2))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x2, y2, x3, y3))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x3, y3, x4, y4))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x4, y4, x1, y1))
    
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x5, y5, x6, y6))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x6, y6, x7, y7))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x7, y7, x8, y8))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x8, y8, x5, y5))
    
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x1, y1, x5, y5))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x2, y2, x6, y6))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x3, y3, x7, y7))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x4, y4, x8, y8))
    
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
    

    
    
    window = sdl2.ext.Window("Fps game Test", size=(1024, 720))
    window.show()
    
    windowsurface = window.get_surface()
        
    running = True
    xmaxsize = 1024
    ymaxsize = 720
    
    
    
    mousex = 512
    mousey = 360
    
    refreshx1 =100
    refreshx2 =100
    refreshx3 =100
    refreshx4 =100

    refreshy1 =100
    refreshy2 =100
    refreshy3 =100
    refreshy4 =100
    
    
    while running:
        sdl2.ext.fill(windowsurface, 0)
        
        innerCubex1 = xmaxsize - mousex - refreshx1
        innerCubex2 = xmaxsize - mousex + refreshx2
        innerCubex3 = xmaxsize - mousex + refreshx3
        innerCubex4 = xmaxsize - mousex - refreshx4

        innerCubey1 = ymaxsize - mousey  - refreshy1
        innerCubey2 = ymaxsize - mousey  - refreshy2
        innerCubey3 = ymaxsize - mousey  + refreshy3
        innerCubey4 = ymaxsize - mousey  + refreshy4
        
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_UP:#randomisation
                                #X is <------>   y is /|\
                                #                      |
                                #                      |
                                #                     \|/ 
                    if(mousex > innerCubex1 and mousey > innerCubey1 and mousex < innerCubex2 and mousey > innerCubey2 and mousex < innerCubex3 and mousey < innerCubey3 and mousex > innerCubex4 and mousey < innerCubey4):                        
                        refreshx1 +=5
                        refreshx2 +=5
                        refreshx3 +=5
                        refreshx4 +=5
                        
                        refreshy1 +=5
                        refreshy2 +=5
                        refreshy3 +=5
                        refreshy4 +=5
                        
                    if(mousex < innerCubex1 and mousey > innerCubey1 and mousex < innerCubex4 and mousey < innerCubey4): #left wall +
                        refreshx1 +=10
                        refreshx2 +=10
                        refreshx3 +=10
                        refreshx4 +=10
                        refreshy1 +=10
                        refreshy2 +=20
                        refreshy3 +=20
                        refreshy4 +=10
                        
                    if(mousex > innerCubex2 and mousex > innerCubex3): #left wall +
                        refreshx1 +=10
                        refreshx2 -=10
                        refreshx3 -=10
                        refreshx4 +=10
                        refreshy1 +=20
                        refreshy2 +=10
                        refreshy3 +=10
                        refreshy4 +=20
                        
                    break
                    
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_DOWN:
                    if(mousex > innerCubex1 and mousey > innerCubey1 and mousex < innerCubex2 and mousey > innerCubey2 and mousex < innerCubex3 and mousey < innerCubey3 and mousex > innerCubex4 and mousey < innerCubey4):                        
                        refreshx1 -=5
                        refreshx2 -=5
                        refreshx3 -=5
                        refreshx4 -=5

                        refreshy1 -=5
                        refreshy2 -=5
                        refreshy3 -=5
                        refreshy4 -=5
                    if(mousex < innerCubex1 and mousey > innerCubey1 and mousex < innerCubex4 and mousey < innerCubey4): #left wall +
                        refreshx1 -=10
                        refreshx2 -=10
                        refreshx3 -=10
                        refreshx4 -=10
                        refreshy1 -=10
                        refreshy2 -=20
                        refreshy3 -=20
                        refreshy4 -=10
                    if(mousex > innerCubex2 and mousex > innerCubex3): #left wall +
                        refreshx1 +=10
                        refreshx2 -=10
                        refreshx3 -=10
                        refreshx4 +=10
                        refreshy1 -=20
                        refreshy2 -=10
                        refreshy3 -=10
                        refreshy4 -=20
                    break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_LEFT:
                    break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_RIGHT:
                
                    break
            if event.type == sdl2.SDL_MOUSEMOTION:#MOUSEMOTION:
                #print(sdl2.SDL_MOUSEBUTTONDOWN)
                sdl2.ext.fill(windowsurface, 0)
                                
                mousex = event.motion.x
                mousey = event.motion.y
                
                #print(mousex)
                #print(mousey)
                break
                #>512 if 600,300 mouse 100,100 1024 1024 - mouse posx = x1- 512 
        try:
            
        
            draw_lineCube(windowsurface,innerCubex1,innerCubey1,innerCubex2,innerCubey2,innerCubex3,innerCubey3,innerCubex4,innerCubey4,0,0,1024,0,1024,720,0,720)
            sdl2.SDL_FlushEvent(sdl2.SDL_MOUSEMOTION)
            if(innerCube < 10):
                innerCube = 400
            if(innerCube > 410):
                innerCube = 10
        except Exception:
            print("errrror")
            pass
        
        #draw_lineCube(windowsurface,50,50,100,50,130,80,70,80,150,150,200,150,230,180,230,160)
        #print(mousex)
        #print(mousey)
        #print(events)
        #print(pg.event.get())
          
        
        sdl2.SDL_Delay(60)
        
        window.refresh()
    sdl2.ext.quit()
    return 0
    
    

    
    
if __name__ == "__main__":
    sys.exit(run())
    