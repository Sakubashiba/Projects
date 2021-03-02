#!/usr/bin/env python
import sys
import os

from random import randint
from time import time

import pygame as pg
from pygame.compat import xrange_

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

print(main_dir)
print(data_dir)
print(os.path.abspath(__file__))
print(os.path.split(os.path.abspath(__file__)))
print(os.path.split(os.path.abspath(__file__))[0])
print(os.path.split(os.path.abspath(__file__))[1])
print(os.path.join(main_dir, "Loolol"))

screen_dims = [640, 480] #Screen dimensions x and y 
print(screen_dims)

update_rects = False
use_static = False
use_layered_dirty = False
use_alpha = False
flags = 0

class Thingy(pg.sprite.DirtySprite):
    images = None

    def __init__(self):
        ##        pg.sprite.Sprite.__init__(self)
        pg.sprite.DirtySprite.__init__(self)
        self.image = Thingy.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 300#randint(0, screen_dims[0])
        self.rect.y = 220#randint(0, screen_dims[1])
        # self.vel = [randint(-10, 10), randint(-10, 10)]
        self.vel = [randint(-8, 8), randint(-8, 8)]
        #self.dirty = 0

    def update(self):
        for i in [0, 1]:
            nv = self.rect[i] + self.vel[i]
            if nv >= screen_dims[i] or nv < 0:
                self.vel[i] = -self.vel[i]
                nv = self.rect[i] + self.vel[i]
            self.rect[i] = nv

def main(
    update_rects=True,
    use_static=False,
    use_layered_dirty=True,
    screen_dims=[640, 480],
    use_alpha=True,
    flags=0,
):




    pg.init()  # needed to initialise time module for get_ticks()
#screen_dims = [640, 480]
#flags = 0
#screen = pg.display.set_mode(screen_dims, flags, vsync="-vsync" in sys.argv)
    screen = pg.display.set_mode(screen_dims)
    screen.fill([0, 0, 0])
    pg.display.flip()
    sprite_surface = pg.image.load(os.path.join(data_dir, "asprite.bmp"))
    Thingy.images = [sprite_surface]
    if use_static:
        Static.images = [sprite_surface2]

    
    numsprites = 1000
    sprites = None
    if use_layered_dirty:
        ##        sprites = pg.sprite.FastRenderGroup()
        sprites = pg.sprite.LayeredDirty()
    else:
        if update_rects:
            sprites = pg.sprite.RenderUpdates()
        else:
            sprites = pg.sprite.Group()

    for i in xrange_(0, numsprites):
        if use_static and i % 2 == 0:
            sprites.add(Static())
        sprites.add(Thingy())    
    
    going2 = True
    
    while going2:
        frames = 0
        start = time()
        
        background = pg.Surface(screen.get_size())
        background = background.convert()
        background.fill([0, 0, 0])
        
        going = True
        while going:
            if not update_rects:
                screen.fill([0, 0, 0])
        
            ##        for sprite in sprites:
            ##            sprite.move()
        
            if update_rects:
                sprites.clear(screen, background)
            sprites.update()
        
            rects = sprites.draw(screen)
            if update_rects:
                pg.display.update(rects)
            else:
                pg.display.flip()
        
            for event in pg.event.get():
                if event.type in [pg.QUIT, pg.KEYDOWN, pg.QUIT, pg.JOYBUTTONDOWN]:
                    going2 = False
        
            frames += 1
            if frames == 60:
                going = False
        end = time()
        print("FPS: %f" % (frames / ((end - start))))
        #pg.quit()

if __name__ == "__main__":
    main(update_rects, use_static, use_layered_dirty, screen_dims, use_alpha, flags)
