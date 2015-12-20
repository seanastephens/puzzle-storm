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

def drawBackground():
	screen.fill(WHITE)
	for x in range(0, WIDTH, TILE_SIZE):
		for y in range(0, HEIGHT, TILE_SIZE):
			pygame.draw.rect(screen, BLUE, [x, y, TILE_SIZE, TILE_SIZE], 2)


	
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
	pygame.draw.rect(screen, BLACK, block_place)

	return x, y

clock = pygame.time.Clock()

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
	x, y = piece(event, x, y)
	pygame.display.flip()
	
		

pygame.quit()
