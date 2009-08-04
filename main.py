#!/home/amv/env/bin/python3
#coding=utf-8

import pygame
from hello import CHello
from console import CConsole
from base import rsl

pygame.init()

my_hello = CHello(100)
my_console = CConsole(100)

main_surf = pygame.display.set_mode(rsl)
main_surf.fill((0,0,0))
pygame.display.flip()

#my_hello.main_loop(main_surf) #TODO раскомментировать
my_console.main_loop(main_surf)

# TODO убрать
run = 1
while run == 1:
	event = pygame.event.poll()
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			run = 0
