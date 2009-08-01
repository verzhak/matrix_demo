#!/home/amv/env/bin/python3
#coding=utf-8

import pygame
from hello import CHello

pygame.init()

rsl = (640,480)
surf = pygame.display.set_mode(rsl)

hello = CHello(rsl)

surf.fill((0,0,0))
pygame.display.flip()

run = 1
while run == 1:
	event = pygame.event.poll()
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			run = 0
	elif event.type == hello.event_type:
		surf.blit(hello.do_shot(surf.copy()), (0,0))
		pygame.display.flip()
