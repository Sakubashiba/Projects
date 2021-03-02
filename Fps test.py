import sys
from random import randint
import sdl2
import sdl2.ext
import time
import pygame as pg
from PIL import ImageGrab
from PIL import Image
import re
from sdl2.ext.compat import byteify


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
def draw_letter(surface,letter,xpos,ypos):
    if(letter == "a"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos + 10, xpos + 5, ypos ))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 5, ypos , xpos +9, ypos +10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos +2, ypos + 7, xpos +8, ypos +7))
    if(letter == "b"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos + 10, xpos + 1, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos + 5, xpos + 7, ypos+5))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 7, ypos + 5, xpos + 7, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 7, ypos + 10, xpos + 1, ypos+10))
    if(letter == "c"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos + 10, xpos + 1, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos , xpos + 6, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos + 10, xpos + 6, ypos+10))
    if(letter == "d"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 7, ypos , xpos + 7, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 7, ypos + 10, xpos + 3, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 3, ypos + 10, xpos + 3, ypos+4))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 3, ypos + 4, xpos + 8, ypos+3))
    if(letter == "e"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos + 10, xpos + 1, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos , xpos + 6, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos +5, xpos + 6, ypos+5))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos + 10, xpos + 6, ypos+10))
    if(letter == "f"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos + 10, xpos + 1, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos , xpos + 6, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos +5, xpos + 6, ypos+5))
    if(letter == "g"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos + 10, xpos + 1, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos , xpos + 8, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos +10, xpos + 8, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 8, ypos +10, xpos + 8, ypos+6))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 5, ypos +6, xpos + 10, ypos+6))
    if(letter == "h"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos + 10, xpos + 1, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos + 5, xpos + 10, ypos+5))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 10, ypos + 10, xpos + 10, ypos))
    if(letter == "i"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 6, ypos + 10, xpos + 6, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 3, ypos, xpos + 8, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 3, ypos+10, xpos + 8, ypos+10))
    if(letter == "j"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 6, ypos + 8, xpos + 6, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 2, ypos, xpos + 8, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 6, ypos +8, xpos + 3, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 3, ypos +10, xpos + 3, ypos+6))
    if(letter == "k"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 1, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos +4, xpos + 4, ypos+1))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos +4, xpos + 4, ypos+9))
    if(letter == "l"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 1, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos+10, xpos + 7, ypos+10))
    if(letter == "m"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 1, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 4, ypos+4))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 4, ypos+4, xpos + 8, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 8, ypos, xpos + 8, ypos+10))
    if(letter== "n"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 1, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos+10, xpos + 9, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 9, ypos, xpos + 9, ypos+10))
    if(letter == "o"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 1, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos+10, xpos + 8, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 8, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 8, ypos, xpos + 8, ypos+10))
    if(letter == "p"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 1, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 6, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 6, ypos, xpos + 6, ypos+6))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 6, ypos+6, xpos + 1, ypos+6))
    if(letter == "q"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 1, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos+10, xpos + 8, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 8, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 8, ypos, xpos + 8, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 7, ypos+7, xpos + 10, ypos+10))
    if(letter == "r"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 1, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 6, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 6, ypos, xpos + 6, ypos+6))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 6, ypos+6, xpos + 1, ypos+6))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos+6, xpos + 6, ypos+10))
    if(letter == "s"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 8, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 1, ypos+5))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos+5, xpos + 8, ypos+6))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 8, ypos+6, xpos + 8, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 8, ypos+10, xpos + 1, ypos+10))
    if(letter == "t"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 9, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 5, ypos, xpos + 5, ypos+10))
    if(letter == "u"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 1, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos + 10, xpos + 6, ypos+6))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 6, ypos+6, xpos + 6, ypos))
    if(letter == "v"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 5, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 5, ypos+10, xpos + 9, ypos))
    if(letter == "w"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 3, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 3, ypos+10, xpos + 5, ypos+5))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 5, ypos+5, xpos +7, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 7, ypos+10, xpos +9, ypos))
    if(letter == "x"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 6, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos , ypos+10, xpos + 6, ypos))
    if(letter == "y"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos , ypos+10, xpos + 6, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos , ypos, xpos + 3, ypos+3))
    if(letter == "z"):
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos, xpos + 9, ypos))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 9, ypos, xpos + 1, ypos+10))
        sdl2.ext.line(surface, sdl2.ext.Color(randint(70, 255),255,randint(70, 255)), (xpos + 1, ypos+10, xpos + 10, ypos+10))


def run():
    # You know those from the helloworld.py example.
    # Initialize the video subsystem, create a window and make it visible.
    sdl2.ext.init()
    
    #NULL=None
    
    
    window = sdl2.ext.Window("Fps game Test", size=(1024, 720))
    window.show()
    
    



    #this needs practice..
    """
    #window2 = sdl2.SDL_CreateWindow(byteify("SDL2 Displaying Image", "utf-8"),sdl2.video.SDL_WINDOWPOS_UNDEFINED,sdl2.video.SDL_WINDOWPOS_UNDEFINED, 399, 489, sdl2.SDL_WINDOW_BORDERLESS);    
    #sdl2.SDL_ShowWindow(window2)
    #renderer = sdl2.SDL_CreateRenderer(window2, -1, 0)
    #image = sdl2.SDL_LoadBMP(b"C:\\Users\\0\\Desktop\\Lests try to make a game\\HeadNeckInfo.bmp")
    #print(image)
    #texture = sdl2.SDL_CreateTextureFromSurface(renderer, image)
    SDL_DestroyTexture(texture);
    SDL_FreeSurface(image);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Rect dstrect = { 5, 5, 320, 240 };
    SDL_RenderCopy(renderer, texture, NULL, &dstrect);
    sdl2.SDL_RenderCopy(renderer, texture, NULL, NULL);
    sdl2.SDL_RenderPresent(renderer);
    """
    
    
    windowsurface = window.get_surface()
    
    img = Image.open('C:\\Users\\0\\Desktop\\Lests try to make a game\\HeadNeck.png')
    rgb_im = img.convert('RGB')
    
    print(img.size[0])

    

    running = True                                                     
    xminsize = 0                                            
    yminsize = 0                                            
    xmaxsize = 1440                                         
    ymaxsize = 900                                          
                                                            
    HhumanLocation =0                                       
    #Human location code = 
    #0=none selected
    #1=Head
    #2=neck
    #3=Body
    #4=Left Arm
    #5=Right Arm
    #6=Left Leg
    #7=Right Leg

    
    sdl2.ext.fill(windowsurface, 0)
    
    mouseClickCount = 0
    
    x=500
    y=600
    test_string = 'clear'
    lengofarr =len(test_string)
    for i in range(0,lengofarr):
        draw_letter(windowsurface,test_string[i],x,y)
        x+=10
    draw_lineRect(windowsurface,480,590,570,590,570,620,480,620)
    
    
    
    
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
            
            if event.type == sdl2.SDL_MOUSEMOTION:
                mousex = event.motion.x
                mousey = event.motion.y
                sdl2.ext.fill(windowsurface, 0,(250,1,350,50))
                if(mousex > 140 and mousey > 40 and mousex < 200 and mousey < 100):#head
                    print("Head")
                    x=270
                    y=10   
                    test_string = 'head'
                    lengofarr =len(test_string)
                    for i in range(0,lengofarr):
                        draw_letter(windowsurface,test_string[i],x,y)
                        x+=10
                if(mousex > 160 and mousey > 100 and mousex < 180 and mousey < 120):#neck
                    print("neck")
                    x=270
                    y=10   
                    test_string = 'neck'
                    lengofarr =len(test_string)
                    for i in range(0,lengofarr):
                        draw_letter(windowsurface,test_string[i],x,y)
                        x+=10
                if(mousex > 120 and mousey > 120 and mousex < 220 and mousey < 300):#body
                    print("body")
                    x=270
                    y=10   
                    test_string = 'body'
                    lengofarr =len(test_string)
                    for i in range(0,lengofarr):
                        draw_letter(windowsurface,test_string[i],x,y)
                        x+=10
                if(mousex > 40 and mousey > 120 and mousex < 120 and mousey < 300):#left arm
                    print("left arm")
                    x=270
                    y=10   
                    test_string = 'left arm'
                    lengofarr =len(test_string)
                    for i in range(0,lengofarr):
                        draw_letter(windowsurface,test_string[i],x,y)
                        
                        x+=10
                        if(x==320):
                            x-=50
                            y+=15
                if(mousex > 220 and mousey > 120 and mousex < 300 and mousey < 300):#right arm
                    print("right arm")
                    x=270
                    y=10   
                    test_string = 'right arm'
                    lengofarr =len(test_string)
                    for i in range(0,lengofarr):
                        draw_letter(windowsurface,test_string[i],x,y)
                        
                        x+=10
                        if(x==320):
                            x-=50
                            y+=15
                if(mousex > 100 and mousey > 300 and mousex < 140 and mousey < 530):#left lwg
                    print("left leg")
                    x=270
                    y=10   
                    test_string = 'left leg'
                    lengofarr =len(test_string)
                    for i in range(0,lengofarr):
                        draw_letter(windowsurface,test_string[i],x,y)
                        
                        x+=10
                        if(x==320):
                            x-=50
                            y+=15
                if(mousex > 200 and mousey > 300 and mousex < 240 and mousey < 530):#rught leg
                    print("right leg")
                    x=270
                    y=10   
                    test_string = 'right leg'
                    lengofarr =len(test_string)
                    for i in range(0,lengofarr):
                        draw_letter(windowsurface,test_string[i],x,y)
                        
                        x+=10
                        if(x==320):
                            x-=50
                            y+=15

                break
            if event.type == sdl2.SDL_MOUSEBUTTONDOWN:#MOUSEMOTION:
                
                #print(sdl2.SDL_MOUSEBUTTONDOWN)
                #sdl2.ext.fill(windowsurface, 0)
                mousex = event.motion.x
                mousey = event.motion.y
                
                    
                x=660
                y=20
                test_string = 'occipital neuralgia is a condition that occurs when the nerves that run from the spinal cord to the scalp are damaged it is often confused with migraines occipital neuralgia causes sharp aching throbbing pain that starts at the base of the head in the neck and moves towards the scalp '
                lengofarr =len(test_string)
                for i in range(0,lengofarr):
                #print(asdf[i])
                    draw_letter(windowsurface,test_string[i],x,y)
                    x+=10
                    if(x == 1000):
                        x-=340
                        y+=15
                #
                
                sdl2.SDL_Delay(60)
                if(mousex > 140 and mousey > 40 and mousex < 200 and mousey < 100):#head
                    HhumanLocation = 1
                    for i in range (0,img.size[0]):
                        for j in range (0,img.size[1]):
                            r, g, b = rgb_im.getpixel((i, j))
                            sdl2.ext.fill(windowsurface, (r,g,b), (i+650, j+240, 1, 1))
                if(mousex > 160 and mousey > 100 and mousex < 180 and mousey < 120):#neck
                    HhumanLocation = 2
                if(mousex > 120 and mousey > 120 and mousex < 220 and mousey < 300):#body
                    HhumanLocation = 3
                if(mousex > 40 and mousey > 120 and mousex < 120 and mousey < 300):#left arm
                    HhumanLocation = 4
                if(mousex > 220 and mousey > 120 and mousex < 300 and mousey < 300):#right arm
                    HhumanLocation = 5
                if(mousex > 100 and mousey > 300 and mousex < 140 and mousey < 530):#left lwg
                    HhumanLocation = 6
                if(mousex > 200 and mousey > 300 and mousex < 240 and mousey < 530):#rught leg
                    HhumanLocation = 7
                print(HhumanLocation)
                HhumanLocation = 0#this might need to move
                if(mousex > 480 and mousey > 590 and mousex < 570 and mousey < 620):
                    sdl2.ext.fill(windowsurface, 0)
                    draw_lineRect(windowsurface,480,590,570,590,570,620,480,620)
                    x=500
                    y=600   
                    test_string = 'clear'
                    lengofarr =len(test_string)
                    for i in range(0,lengofarr):
                        draw_letter(windowsurface,test_string[i],x,y)
                        x+=10
                break

        try:
            
            draw_lineRect(windowsurface,140,40,200,40,200,100,140,100)#Head
            draw_lineRect(windowsurface,160,100,180,100,180,120,160,120)#neck
            draw_lineRect(windowsurface,120,120,220,120,220,300,120,300)#Body
            draw_lineRect(windowsurface,120,120,40,300,70,300,120,130)#Left Arm
            draw_lineRect(windowsurface,220,120,300,300,270,300,220,130)#Right Arm
            draw_lineRect(windowsurface,120,300,100,520,130,520,130,300)#Left Leg
            draw_lineRect(windowsurface,220,300,230,520,200,520,210,300)#Right Leg
            draw_lineRect(windowsurface,1,1,350,1,350,600,1,600)#square arouind human
            draw_lineRect(windowsurface,350,1,650,1,650,200,350,200)#top sqware detail about part
            draw_lineRect(windowsurface,350,200,650,200,650,400,350,400)#mid Sqware pain type
            draw_lineRect(windowsurface,350,400,650,400,650,550,350,550)#bot sqware pain level
            draw_lineRect(windowsurface,250,1,350,1,339,50,250,50)
            pattern = "[a-z]+\s"
            
            #result = re.findall(pattern, test_string)
            
            normalStr = "hello you"
            asdf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
            asdd = "a"
            #sdl2.ext.fill(windowsurface, 0)
            #draw_letter(windowsurface,asdf[5],200,200)
            #print(result[1])
            
            
        except Exception:
            print(Exception[0])
            pass
        

        
        window.refresh()
    sdl2.ext.quit()
    return 0
    
    

    
    
if __name__ == "__main__":
    sys.exit(run())
    