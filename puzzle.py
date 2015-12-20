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

def drawBuses(buses):
	pass  # Fix this yo

def piece(key, y):
	block_place = [0, y, TILE_SIZE, TILE_SIZE]

	if key == K_DOWN: 
		y = y + TILE_SIZE
	elif key == K_UP:
		y = y - TILE_SIZE

	pygame.draw.rect(screen, BLACK, block_place)

	return y

clock = pygame.time.Clock()

buses = [(0, 0, 0, 2), (2, 2, 5, 2)]

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
	drawBackground()
	drawBuses(buses)
	y = piece(event, y)
	pygame.display.flip()
	
		

pygame.quit()
