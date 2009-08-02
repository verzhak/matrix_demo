#!/home/amv/env/bin/python3
#coding=utf-8

import pygame
from hello import CHello

pygame.init()

rsl = (640,480)
main_surf = pygame.display.set_mode(rsl)

hello = CHello(rsl)

main_surf.fill((0,0,0))
pygame.display.flip()

hello.main_loop(main_surf)

run = 1
while run == 1:
	event = pygame.event.poll()
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			run = 0
