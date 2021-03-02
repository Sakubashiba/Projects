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

def draw_lineRect(surface,x1,y1,x2,y2,x3,y3,x4,y4): #X is <----->     y is /\  \/
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x1, y1, x2, y2))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x2, y2, x3, y3))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x3, y3, x4, y4))
    sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (x4, y4, x1, y1))
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
    window = sdl2.ext.Window("Fps game Test", size=(1024, 720))
    window.show()
    
    windowsurface = window.get_surface()
        
    running = True
    
    countche = 120
    countche2 = 40
    
    #----------- randomanisation variables
    rnd1 = randint(0,1024)
    rnd2 = randint(0,720)
    rnd3 = randint(0,1024)
    rnd4 = randint(0,720)
    rnd5 = randint(0,1024)
    rnd6 = randint(0,720)
    rnd7 = 0
    rnd8 = 0
    #-----------
    valuesx = [countche,rnd1,rnd3,rnd5]
    valuesy = [countche2,rnd2,rnd4,rnd6]
    
    while running:
        
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_UP:#randomisation
                    #draw_line(windowsurface,randint(0,795), randint(0,600), randint(0,795), randint(0,600))#X is <------>   y is /|\
                                                                                                            #                      |
                                                                                                            #                      |
                                                                                                            #                     \|/
                    rnd1 = randint(0,1024)
                    rnd2 = randint(0,720)
                    rnd3 = randint(0,1024)
                    rnd4 = randint(0,720)
                    rnd5 = randint(0,1024)
                    rnd6 = randint(0,720)
                    rnd7 = 0
                    rnd8 = 0
                    countche = randint(0,1024)
                    countche2 = randint(0,720)
                    valuesx = [countche,rnd1,rnd3,rnd5]
                    valuesy = [countche2,rnd2,rnd4,rnd6]
                    break
        
        
        valuesx[0] = valuesx[0] + 20
        valuesy[0] = valuesy[0] + 5
        draw_lineRect(windowsurface,valuesx[1],valuesy[1],valuesx[2],valuesy[2],valuesx[3],valuesy[3],valuesx[0],valuesy[0])
            
        i = 0
        for valu in valuesx:
            #print(valu)
            for asd in valuesx:
                if valuesx[i] >= 1010 :
                    valuesx[i] = 0
                    break
                i=i+1
            i= 0    
            
        i = 0
        for valu in valuesy:
            #print(valu)
            for asd in valuesy:
                if valuesy[i] >= 710 :
                    valuesy[i] = 0
                    break
                i=i+1
            i= 0    
           
       
        #print(events)
        #print(pg.event.get())
          
        
        sdl2.SDL_Delay(60)
        
        window.refresh()
    sdl2.ext.quit()
    return 0
    
    

    
    
if __name__ == "__main__":
    sys.exit(run())
    