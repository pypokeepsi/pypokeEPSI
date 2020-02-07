import pygame
from pygame.locals import *

def RoundedRect(surface, rect, color, text, radius=0.4):
    font = pygame.font.SysFont('arial', 28)
    text = font.render(text, True, (232, 208, 208))
    textRect = text.get_rect()
    textRect.center = (rect[2] // 2, rect[3] // 2)
    rect         = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = pygame.Surface(rect.size,SRCALPHA)

    circle       = pygame.Surface([min(rect.size)*3]*2,SRCALPHA)
    pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = pygame.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)
    radius = rectangle.blit(circle,(0,0))
    radius.bottomright = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)
    surface.blit(rectangle,pos)
    surface.blit( text, textRect )
    return surface

if __name__ == "__main__":
    pygame.init()
    scr = pygame.display.set_mode((300,300))
    scr.fill(-1)
    AAfilledRoundedRect(scr,(0,0,200,50),(200,20,20), 'Attack', 2)
    pygame.display.flip()
    while pygame.event.wait().type != QUIT: pass