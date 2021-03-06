#!/usr/bin/env python

import pygame
from pygame.locals import *

# Global constants
WIDTH = 500
HEIGHT = 500
TILE_SIZE = 50	

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PUZZLES BAM!!!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (102, 0, 102)
GREEN = (51, 204, 51)
CYAN = (0, 204, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 102, 0)
OLIVE = (51, 51, 0)





def drawBackground():
	screen.fill(WHITE)
	for x in range(0, WIDTH, TILE_SIZE):
		for y in range(0, HEIGHT, TILE_SIZE):
			pygame.draw.rect(screen, BLUE, [x, y, TILE_SIZE, TILE_SIZE], 2)

def drawBuses(buses):
	for bus in buses:
		pygame.draw.rect(screen, bus[4], bus[:4])
		
def piece(key, x, y):
	block_place = [x, y, TILE_SIZE, TILE_SIZE]

	if key == K_DOWN: 
		y = y + TILE_SIZE
		if y == WIDTH:
			y = WIDTH - TILE_SIZE
	
	elif key == K_UP:
		y = y - TILE_SIZE
		if y == -TILE_SIZE:
			y = 0
	
	elif key == K_RIGHT:
		x = x + TILE_SIZE
		if x == WIDTH:
			x = WIDTH - TILE_SIZE
	
	elif key == K_LEFT:
		x = x - TILE_SIZE
		if x == -TILE_SIZE:
			x = 0
	pygame.draw.rect(screen, RED, block_place, 4)

	return x, y

clock = pygame.time.Clock()

# first character = x coordinate, 2nd = y coordinate, 3rd = x length of object, 4th = y length
buses = [
	(0, 0, TILE_SIZE * 3, TILE_SIZE, PURPLE), 
	(TILE_SIZE * 2, TILE_SIZE * 2, TILE_SIZE, TILE_SIZE * 2, GREEN),
	(TILE_SIZE * 3, TILE_SIZE * 4, TILE_SIZE, TILE_SIZE * 3, ORANGE)
]
running = True
x = 0
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
	drawBackground()
	drawBuses(buses)
	x, y = piece(event, x, y)
	pygame.display.flip()
	
		

pygame.quit()
