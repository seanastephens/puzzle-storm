#!/usr/bin/env python

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('PUZZLES BAM!!!')

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
BLUE = ( 0, 0, 255)


def drawBoard(t):
	screen.fill(WHITE)
	width = 50	
	for x in range(0, 500, 50):
		for y in range(0, 500, 50):
			if (x + y) % 100 == 0:
				color = BLUE
			else:
				color = BLACK
			pygame.draw.rect(screen, color, [x + (t % 50), y, width, width])

	pygame.display.flip()
	
clock = pygame.time.Clock()

running = True
ticker = 0
while running:
    clock.tick(60)
    for event in pygame.event.get():
        # print event
        if event.type == QUIT:
            running = False
    drawBoard(ticker)
    ticker += 1


pygame.quit()
