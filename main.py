#!/home/amv/env/bin/python3
#coding=utf-8

import pygame
from hello import CHello
from console import CConsole

pygame.init()

rsl = (640,480)

my_hello = CHello(rsl)
my_console = CConsole(rsl)

main_surf = pygame.display.set_mode(rsl)
main_surf.fill((0,0,0))
pygame.display.flip()

# my_hello.main_loop(main_surf) #TODO раскомментировать
my_console.main_loop(main_surf)

# TODO убрать
run = 1
while run == 1:
	event = pygame.event.poll()
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			run = 0
