import sys
from random import randint
import sdl2
import sdl2.ext
import time
import pygame as pg
from PIL import ImageGrab
from PIL import Image

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
    sdl2.ext.line(surface, sdl2.ext.Color(255,255,255), (x1,y1,x2,y2,x2,y2,x3,y3,x3,y3,x4,y4,x4,y4,x1,y1))

def draw_lineRectFill(surface,x1,y1,x2,y2,x3,y3,x4,y4): #X is <----->     y is /\  \/
    j = 0
    ifchanger = 0
    #k = 0
    sdl2.ext.line(surface, sdl2.ext.Color(255,255,255), (x1,y1,x2,y2,x2,y2,x3,y3,x3,y3,x4,y4,x4,y4,x1,y1))
    
    if (ifchanger == 0):
        pass
        #todo 

    if(y1 < y2):
        for i in range (0,x2 - x1):
            sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),randint(70, 255),randint(70, 255)), (x1+i*2,y1+j,x4+i,y4))
            if (j != (y2-y1) and i % 2 == 0):
                sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),randint(70, 255),randint(70, 255)), (x1+i,y1+j,x4+i,y4))
                j+=1

    elif (x2 - x1 > 0 and y2 - y1 > 0):
        for i in range (0,x2 - x1):
            sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),randint(70, 255),randint(70, 255)), (x1+i,y1-j,x4+i,y4))
            if (j != (y2-y1) and i % 2 == 0):
                sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),randint(70, 255),randint(70, 255)), (x1+i,y1-j,x4+i,y4))
                j+=1
    elif (x1-x2 > 0 and y2-y1 > 0):
        for i in range (0,x1 - x2):
            sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),randint(70, 255),randint(70, 255)), (x1+i,y1-j,x4+i,y4))
            if (j != (y2-y1) and i % 2 == 0):
                sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),randint(70, 255),randint(70, 255)), (x1+i,y1-j,x4+i,y4))
                j+=1

        
        
    
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
    
def draw_rects(surface, x , y , w , h):
        sdl2.ext.fill(surface, (sdl2.ext.Color(255,255,255)), (x, y, w, h))


def run():
    # You know those from the helloworld.py example.
    # Initialize the video subsystem, create a window and make it visible.
    sdl2.ext.init()
    

    
    
    window = sdl2.ext.Window("Fps game Test", size=(1024, 720))
    window.show()
    
    windowsurface = window.get_surface()
       
    running = True
    xminsize = 0
    yminsize = 0
    xmaxsize = 1440
    ymaxsize = 900

    sdl2.ext.fill(windowsurface, 0)
    
    mouseClickCount = 0
    
    while running:
        

        
        
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_UP:#randomisation
                    running = False
                    break
                    
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_DOWN:
                    sdl2.ext.fill(windowsurface, 0)
                    break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_LEFT:

                    break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    sdl2.ext.fill(windowsurface, 0)
                    xminsize = 0
                    yminsize = 0
                    xmaxsize = 1024
                    ymaxsize = 720

                    break
            if event.type == sdl2.SDL_MOUSEBUTTONDOWN:#MOUSEMOTION:
                
                #print(sdl2.SDL_MOUSEBUTTONDOWN)
                #sdl2.ext.fill(windowsurface, 0)
                if(mouseClickCount == 0):
                    x1,x2,x3,x4,y1,y2,y3,y4 =0,0,0,0,0,0,0,0
                    mousex = event.motion.x
                    x1 = mousex
                    mousey = event.motion.y
                    y1 = mousey
                    mouseClickCount+=1
                elif(mouseClickCount == 1):
                    mousex = event.motion.x
                    x2 = mousex
                    mousey = event.motion.y
                    y2 = mousey
                    mouseClickCount+=1
                elif(mouseClickCount == 2):
                    mousex = event.motion.x
                    x3 = mousex
                    mousey = event.motion.y
                    y3 = mousey
                    mouseClickCount+=1
                elif(mouseClickCount == 3):
                    mousex = event.motion.x
                    x4 = mousex
                    mousey = event.motion.y
                    y4 = mousey
                    print("Mouse X is = ("+str(mousex)+")..Mouse Y is = ("+str(mousey)+")")
                    for i in range(0,100):
                        i+=2
                        draw_lineRect(windowsurface,x1+i,y1+i,x2-i,y2+i,x3-i,y3-i,x4+i,y4-i)
                    
                    
                    #draw_lineRect(windowsurface,x1,y1,x2,y2,x3,y3,x4,y4)
                    
                    #draw_lineRect(windowsurface,x4,y1,x2,y1,x2,y3,x4,y3)#outer perfect rect
                    
                    print(abs(int((x1-x2)/2)))
                    print(abs(int((y1-y2)/2)))
                    print(abs(int((x3-x4)/2)))
                    print(abs(int((y3-y4)/2)))
                    
                    xx1 = x1 + abs(int((x1-x2)/2))
                    yy1 = y1 + abs(int((y1-y2)/2))
                    xx2 = x4 + abs(int((x3-x4)/2))
                    yy2 = y4 + abs(int((y3-y4)/2))

                    #draw_line(windowsurface,xx1,yy1,xx2,yy2)
                    #draw_line(windowsurface,x1,y1,x3,y3)
                    #y1-y4 x1-x2
                    print(abs(int((x2-x3)/2)))
                    print(abs(int((y2-y3)/2)))
                    print(abs(int((x1-x4)/2)))
                    print(abs(int((y1-y4)/2)))
                    
                    xxx1 = x1 - abs(int((x1-x4)/2))
                    yyy1 = y1 + abs(int((y1-y4)/2))
                    xxx2 = x2 + abs(int((x2-x3)/2))
                    yyy2 = y2 + abs(int((y2-y3)/2))

                    #draw_line(windowsurface,xxx1,yyy1,xxx2,yyy2)
                    #draw_line(windowsurface,x2,y2,x4,y4)
                    
                    print("The resault="+str(int((x1+x3) /2)))
                    
                    #y1-y4 x1-x2
                    xxxx1 = x2 - abs(int((x1-x2)/2))
                    yyyy1 = y4 - abs(int((y1-y4)/2))
                    
                    #draw_line(windowsurface,xxxx1,yyyy1,x1,y1)
                    #draw_line(windowsurface,xxxx1,yyyy1,x2,y2)
                    #draw_line(windowsurface,xxxx1,yyyy1,x3,y3)
                    #draw_line(windowsurface,xxxx1,yyyy1,x4,y4)
                    
                    mouseClickCount = 0

                break

        try:
            
            sdl2.SDL_Delay(60)
        except Exception:
            print(Exception[0])
            pass
        

        
        window.refresh()
    sdl2.ext.quit()
    return 0
    
    

    
    
if __name__ == "__main__":
    sys.exit(run())
    