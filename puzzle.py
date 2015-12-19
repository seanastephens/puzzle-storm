#!/usr/bin/env python

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption('PUZZLES BAM!!!')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

# Handle Input Events
while True:
    for event in pygame.event.get():
        print event

pygame.quit()
