import pygame
from pygame.draw import *
import numpy as np
pygame.init()


# Function draws a whitebear
def whitebear(Surface, x, y, size):
	# Head:
	ellipse(Surface, white, (x + size*4, y - size*2.1, size*6, size*3))
	ellipse(Surface, black, (x + size*4, y - size*2.1, size*6, size*3), 1)
	ellipse(Surface, white, (x + size*4.5, y - size*2, size*1, size*1.2))
	ellipse(Surface, black, (x + size*4.5, y - size*2, size*1, size*1.2), 1)
	ellipse(Surface, black, (x + size*6.5, y - size*1.3, size*0.5, size*0.5))
	ellipse(Surface, black, (x + size*9.7, y - size*1, size*0.5, size*0.5))
	arc(Surface, black, (x + size*4, y - size*1.6, size*6, size*2), 4.5, 0,  1)
	# Body:
	ellipse(Surface, white, (x, y, size*9, size*15))
	ellipse(Surface, black, (x, y, size*9, size*15), 1)
	# Leg:
	ellipse(Surface, white, (x + size*4, y + size*10, size*6, size*5))
	ellipse(Surface, black, (x + size*4, y + size*10, size*6, size*5), 1)
	ellipse(Surface, white, (x + size*8, y + size*13.5, size*5, size*2))
	ellipse(Surface, black, (x + size*8, y + size*13.5, size*5, size*2), 1)
	# Lake:
	ellipse(Surface, (200, 200, 200), (x + size*15, y + size*10 - size*2, size*10, size*4))
	ellipse(Surface, black, (x + size*15, y + size*10 - size*2, size*10, size*4), 1)
	ellipse(Surface, (0, 150, 150), (x + size*16, y + size*8.75, size*8, size*3.2))
	ellipse(Surface, (0, 50, 50), (x + size*16, y + size*8.75, size*8, size*3.2), 1)
	# Fishing rod:
	lines(Surface, black, False, [
		(x + size*9.5, y + size*7), 
		(x + size*13.5, y + size*2.3), 
		(x + size*15, y + size*1),
		(x + size*18, y + size*-1.5),
		(x + size*21, y + size*-2.8),
		], int(size*0.2))
	line(Surface, black, (x + size*21, y + size*-2.8), (x + size*21, y + size*10), 1)
	# Arm:
	ellipse(Surface, white, (x + size*7, y + size*4, size*5, size*2))
	ellipse(Surface, black, (x + size*7, y + size*4, size*5, size*2), 1)
	

# Function draws a fish
def fish(Surface, x, y, size):
	# Fins:
	polygon(Surface, red, [
		(x + size*4, y - size*0.6),
		(x + size*3.7, y - size*0.9),
		(x + size*3, y - size*1.1),
		(x + size*2.5, y - size*1.2),
		(x + size*4.2, y - size*1.4),
		(x + size*4.55, y - size*1.1),
		(x + size*4.5, y - size*0.6),
		])
	polygon(Surface, black, [
		(x + size*4, y - size*0.6),
		(x + size*3.7, y - size*0.9),
		(x + size*3, y - size*1.1),
		(x + size*2.5, y - size*1.2),
		(x + size*4.2, y - size*1.4),
		(x + size*4.55, y - size*1.1),
		(x + size*4.5, y - size*0.6),
		], 1)
	polygon(Surface, red, [
		(x + size*3, y + size*0.3),
		(x + size*3.4, y + size*0.3),
		(x + size*3.5, y + size*0.7),
		(x + size*2.8, y + size*0.8),
		(x + size*3, y + size*0.55),
		])
	polygon(Surface, black, [
		(x + size*3, y + size*0.3),
		(x + size*3.4, y + size*0.3),
		(x + size*3.5, y + size*0.7),
		(x + size*2.8, y + size*0.8),
		(x + size*3, y + size*0.55),
		], 1)
	polygon(Surface, red, [
		(x + size*4.8, y + size*0.2),
		(x + size*4.9, y + size*0.1),
		(x + size*5.2, y + size*0.25),
		(x + size*5.8, y + size*0.3),
		(x + size*4.8, y + size*0.7),
		(x + size*4.7, y + size*0.55),
		])
	polygon(Surface, black, [
		(x + size*4.8, y + size*0.2),
		(x + size*4.9, y + size*0.1),
		(x + size*5.2, y + size*0.25),
		(x + size*5.8, y + size*0.3),
		(x + size*4.8, y + size*0.7),
		(x + size*4.7, y + size*0.55),
		], 1)
	# Tail:
	polygon(Surface, grey, [
		(x, y), 
		(x + size*0.5, y + size*0.1), 
		(x + size*2, y), 
		(x + size*0.5, y + size)
		])
	polygon(Surface, black, [
		(x, y), 
		(x + size*0.5, y + size*0.1), 
		(x + size*2, y), 
		(x + size*0.5, y + size)
		], 1)
	# Body:
	polygon(Surface, grey, [
		(x + size*2, y),
		(x + size*3.25, y - size*0.72),
		(x + size*4.5, y - size*0.9),
		(x + size*5.25, y - size*0.75), 
		(x + size*6, y - size*0.4),
		(x + size*5.4, y + size*0.1),
		(x + size*4.5, y + size*0.4),
		(x + size*3, y + size*0.4)
		])
	polygon(Surface, black, [
		(x + size*2, y),
		(x + size*3.25, y - size*0.72),
		(x + size*4.5, y - size*0.9),
		(x + size*5.25, y - size*0.75), 
		(x + size*6, y - size*0.4),
		(x + size*5.4, y + size*0.1),
		(x + size*4.5, y + size*0.4),
		(x + size*3, y + size*0.4)
		], 1)
	# Eye:
	circle(Surface, (0, 121, 255), (int(x + size*5), int(y - size*0.42)), int(size*0.27))
	circle(Surface, black, (int(x + size*5), int(y - size*0.42)), int(size*0.1))
	circle(Surface, white, (int(x + size*4.9), int(y - size*0.43)), int(size*0.07))

# Constants:
FPS = 30
white = (235, 235, 235)
black = (0, 0, 0)
chromakey = (0, 255, 0)
grey = (230, 220, 255)
red = (255, 120, 115)
yellow = (255, 255, 100)
backcolor = (0, 255, 255)
zoom = 10 

background = pygame.display.set_mode((40*zoom, 60*zoom))
background.fill(backcolor)
rect(background, white, (0, 34*zoom, 40*zoom, 60*zoom))
rect(background, black, (0, 34*zoom, 40*zoom, 60*zoom), 1)

# Surfaces with Sun:
sun_surface_1 = pygame.Surface((30*zoom, 60*zoom))
sun_surface_1.fill(chromakey)
sun_surface_1.set_colorkey(chromakey)
sun_surface_1.set_alpha(150)
circle(sun_surface_1, yellow, (15*zoom, 15*zoom), 15*zoom)
circle(sun_surface_1, backcolor, (15*zoom, 15*zoom), 12*zoom)
rect(sun_surface_1, yellow, (14*zoom, 0, 2*zoom, 30*zoom))
rect(sun_surface_1, yellow, (0, 14*zoom, 30*zoom, 2*zoom))
background.blit(sun_surface_1, (10*zoom, -zoom))

sun_surface_2 = pygame.Surface((30*zoom, 60*zoom))
sun_surface_2.fill(chromakey)
sun_surface_2.set_colorkey(chromakey)
sun_surface_2.set_alpha(175)
circle(sun_surface_2, yellow, (15*zoom, 15*zoom), int(2*zoom))
circle(sun_surface_2, yellow, (15*zoom, 2*zoom), int(1.2*zoom))
circle(sun_surface_2, yellow, (28*zoom, 15*zoom), int(1.2*zoom))
circle(sun_surface_2, yellow, (2*zoom, 15*zoom), int(1.1*zoom))
circle(sun_surface_2, yellow, (15*zoom, 28*zoom), int(1*zoom))
background.blit(sun_surface_2, (10*zoom, -zoom))

# Surfaces with fishes and bears:
bear_surface = pygame.Surface((60*zoom, 60*zoom))
bear_surface.fill(chromakey)
bear_surface.set_colorkey(chromakey)
whitebear(bear_surface, 5*zoom, 6*zoom, 1.5*zoom)
background.blit(bear_surface, (- 3*zoom, 20*zoom))

fish_surface = pygame.Surface((40*zoom, 40*zoom))
fish_surface.fill(chromakey)
fish_surface.set_colorkey(chromakey)
fish(fish_surface, 2*zoom, 8*zoom, 2*zoom)
fish_surface.set_alpha(150)
background.blit(fish_surface, (22*zoom, 43*zoom))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()