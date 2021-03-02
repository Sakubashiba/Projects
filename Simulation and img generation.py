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
    


    #Load the image
    """
    img = Image.open('C:\\Users\\0\\Desktop\\rock pixelated.png')

    #Get basic details about the image
    print(img.format)
    print(img.mode)
    print(img.size)
    rgb_im = img.convert('RGB') #3,3 7,6 inner pixxel must stay the same color test left  30x30 inner pixel same if inner pixel first is more than inner pixel secound
                                #add from 3,8 to 8,8 inner pixel +1 twords the secound pixel repeat for each side diagonals are first - secound devided by 2 pixel color
    for i in range (0,29):
        for j in range (0,29):
            r, g, b = rgb_im.getpixel((i, j))
            print("PIXEL["+str(i)+","+str(j)+"]=(",r, g, b,end="),")
    #(65, 100, 137)
    #show the image
    #img.show()
    """
    
    window = sdl2.ext.Window("Fps game Test", size=(1440, 900))
    window.show()
    
    windowsurface = window.get_surface()
       
    running = True
    xminsize = 0
    yminsize = 0
    xmaxsize = 1440
    ymaxsize = 900
    rectxpos = 0
    rectypos = 0
    rectw = 0
    recth = 0
    countche = randint(1000,4000)
    iterations=0
    colorch = 1
    sdl2.ext.fill(windowsurface, 0)
    """
    for j in range(0,30):
        yminsize +=32
        sdl2.ext.line(windowsurface, sdl2.ext.Color(0,255,0), (xminsize, yminsize, 1024, yminsize))
                
    for i in range (0,31):   
        xminsize +=32
        sdl2.ext.line(windowsurface, sdl2.ext.Color(0,255,0), (xminsize, 0, xminsize, 720))
    """
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
                    sdl2.SDL_Delay(1000)
                    break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_LEFT:
                    image = ImageGrab.grab(bbox=(205,60,1250,840))
                    image.save('C:\\Users\\0\\Desktop\\Lests try to make a game\\ImageSimulation\\'+str(randint(0,2999999))+ '.png')
                    break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    sdl2.ext.fill(windowsurface, 0)
                    xminsize = 0
                    yminsize = 0
                    xmaxsize = 1024
                    ymaxsize = 720
                    for j in range(0,30):
                        yminsize +=32
                        sdl2.ext.line(windowsurface, sdl2.ext.Color(0,255,0), (xminsize, yminsize, 1440, yminsize))
                
                    for i in range (0,31):   
                        xminsize +=32
                        sdl2.ext.line(windowsurface, sdl2.ext.Color(0,255,0), (xminsize, 0, xminsize, 900))
                    break
            if event.type == sdl2.SDL_MOUSEMOTION:#MOUSEMOTION:
                #print(sdl2.SDL_MOUSEBUTTONDOWN)
                #sdl2.ext.fill(windowsurface, 0)
                                
                mousex = event.motion.x
                mousey = event.motion.y
                
                #print(mousex)
                #print(mousey)
                break
                #>512 if 600,300 mouse 100,100 1024 1024 - mouse posx = x1- 512 
        try:
            
            
            for x in range(0,randint(10,30)):
                for y in range(0,randint(10,30)):
                    if(colorch == 1):
                        sdl2.ext.fill(windowsurface, (randint(0,255),randint(0,255),randint(0,255)), (randint(0,8)+rectxpos, randint(0,8)+rectypos, 1, 1))
                    elif(colorch == 0):
                        sdl2.ext.fill(windowsurface, (0,0,0), (randint(0,8)+rectxpos, randint(0,8)+rectypos, 1, 1)) 
                    rectypos +=randint(8,16)
                    if (rectypos >= 900):
                        rectypos = 0
                rectxpos +=randint(8,16)
                if (rectxpos >= 1440):
                        rectxpos = 0
            
        except Exception:
            print("errrror")
            pass
        
        #draw_lineCube(windowsurface,50,50,100,50,130,80,70,80,150,150,200,150,230,180,230,160)
        #print(mousex)
        #print(mousey)
        #print(events)
        #print(pg.event.get())
          
        
        #sdl2.SDL_Delay(0)
        if (countche == 0):
            image = ImageGrab.grab(bbox=(0,0,1440,900))
            image.save('C:\\Users\\0\\Desktop\\Lests try to make a game\\ImageSimulation\\Iterations'+str(iterations)+'S'+str(randint(0,2999999))+ '.png')
            #sdl2.ext.fill(windowsurface, 0)
            xminsize = 0
            yminsize = 0
            xmaxsize = 1440
            ymaxsize = 900
            iterations = 0
            countche = randint(1000,4000)
            if (colorch == 1):
                colorch = 0
            elif(colorch == 0):
                colorch = 1
                
            """
            for j in range(0,30):
                yminsize +=32
                sdl2.ext.line(windowsurface, sdl2.ext.Color(0,255,0), (xminsize, yminsize, 1024, yminsize))
        
            for i in range (0,31):   
                xminsize +=32
                sdl2.ext.line(windowsurface, sdl2.ext.Color(0,255,0), (xminsize, 0, xminsize, 720))
                """
        iterations+=1
        countche-=1
        window.refresh()
    sdl2.ext.quit()
    return 0
    
    

    
    
if __name__ == "__main__":
    sys.exit(run())
    