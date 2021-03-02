import sys
from random import randint
import sdl2
import sdl2.ext
import time
import pygame as pg
import array
import os

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
def locateCurrentPos(array,direction):
    arrRows = len(array[0]) # = 20
    arrCols = array.__len__()# = 25
    
    foundx = 0
    foundy = 0
    found = False
    
    for i in range(0,arrCols):
        for j in range(0,arrRows):
            if array[i][j] == '*':
                foundx = i
                foundy = j
                array[i][j] = 0
                found = True
    if direction == "up" and found == True:
        array[foundx-1][foundy] = "*"
    if direction == "down" and found == True:
        array[foundx+1][foundy] = "*"
    if direction == "left" and found == True:
        array[foundx][foundy-1] = "*"
    if direction == "right" and found == True:
        array[foundx][foundy+1] = "*"
    os.system('cls')
def run():
    # You know those from the helloworld.py example.
    # Initialize the video subsystem, create a window and make it visible.
    sdl2.ext.init()
    os.system('cls')

    
    
    window = sdl2.ext.Window("Fps game Test", size=(1024, 720))
    window.show()
    
    windowsurface = window.get_surface()
        
    running = True
    xmaxsize = 1024
    ymaxsize = 720
    
    
    
    
    mousex = 512
    mousey = 360
    
    innerCube = 50
    leftRight = 20
    upDown= 27
    
    levelArray = [[0 for i in range(leftRight)] for j in range(upDown)]
    levelArray[9][9] = '*'

    
    for i in range(0,20):    
        print(levelArray[i])   
    
    while running:
        
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
                    sdl2.ext.fill(windowsurface, 0)
                    locateCurrentPos(levelArray,"up")
                    for i in range(0,20):    
                        print(levelArray[i])   
                    break
                    
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_DOWN:
                    sdl2.ext.fill(windowsurface, 0)
                    locateCurrentPos(levelArray,"down")
                    for i in range(0,20):    
                        print(levelArray[i])   
                    break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_LEFT:
                    sdl2.ext.fill(windowsurface, 0)
                    locateCurrentPos(levelArray,"left")
                    for i in range(0,20):    
                        print(levelArray[i])   
                    break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    sdl2.ext.fill(windowsurface, 0)
                    locateCurrentPos(levelArray,"right")
                    for i in range(0,20):    
                        print(levelArray[i])   
                    break
                    
            if event.type == sdl2.SDL_MOUSEBUTTONDOWN:#MOUSEMOTION:
                #print(sdl2.SDL_MOUSEBUTTONDOWN)
                sdl2.ext.fill(windowsurface, 0)
                                
                mousex = event.motion.x
                mousey = event.motion.y               
                #print(mousex)
                #print(mousey)
                break
                    

            #time.sleep(0.200)
            
        #os.system('cls')
          
        
        sdl2.SDL_Delay(60)
        
        window.refresh()
    sdl2.ext.quit()
    return 0
    
    

    
    
if __name__ == "__main__":
    sys.exit(run())
    