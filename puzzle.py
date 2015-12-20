#!/usr/bin/env python

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('PUZZLES BAM!!!')

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
BLUE = ( 0, 0, 255)

width = 50	

def drawBoard():
	screen.fill(WHITE)
	for x in range(0, 500, 50):
		for y in range(0, 500, 50):
			color = BLUE
			pygame.draw.rect(screen, color, [x, y, width, width], 2)


	
def piece(key, y):
	block_place = [0, y, width, width]
	pygame.draw.rect(screen, BLACK, block_place)
	if key == K_DOWN: 
		y = y + 50
	elif key == K_UP:
		y = y - 50
		#block_place[1] = block_place[1] + 50
		pygame.draw.rect(screen, BLACK, block_place)
	pygame.display.flip()
	#while K_DOWN == True:
	#	block_place[1] = blockplace[1] + 50
	return y
clock = pygame.time.Clock()

running = True
y = 0
while running:
    clock.tick(50)
    event = None
    for event in pygame.event.get():
        # print event
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            event = event.key
    drawBoard()
    y = piece(event, y)
	
		

pygame.quit()
