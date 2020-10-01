import pygame
from pygame.draw import *
import numpy as np
pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))

yellow  = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
center = 300, 300
red = (255, 0, 0)
x0, y0 = center
d = 12

circle(screen, yellow, center, 15*d)
circle(screen, black, center, 15*d, 2)

rect(screen, black, (x0 - 10*d, y0 + 3*d, 20*d, 2*d))

circle(screen, red, (x0 + 6*d, y0 - 5*d), 2*d)
circle(screen, black, (x0 + 6*d, y0 - 5*d), 2*d, 1)
circle(screen, black, (x0 + 6*d, y0 - 5*d), d)
polygon(screen, black, (
	(x0 + 6*d - 4*d, y0 - 5*d - 1.5*d),
	(x0 + 6*d - 4.2*d, y0 - 5*d - 2.5*d),
	(x0 + 6*d + 4.5*d, y0 - 5*d - 3.5*d),
	(x0 + 6*d + 4.8*d, y0 - 5*d - 2.5*d)))


circle(screen, red, (x0 - 6*d, y0 - 5*d), 3*d)
circle(screen, black, (x0 - 6*d, y0 - 5*d), 3*d, 1)
circle(screen, black, (x0 - 6*d, y0 - 5*d), d)
polygon(screen, black, (
	(x0 - 6*d -5.3*d, y0 - 5*d - 6.8*d),
	(x0 - 6*d - 6.0*d, y0 - 5*d - 5.8*d),
	(x0 - 6*d + 5.3*d, y0 - 5*d - 0.8*d),
	(x0 - 6*d + 6.0*d, y0 - 5*d - 1.8*d)))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()