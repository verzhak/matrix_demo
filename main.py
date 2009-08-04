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

pygame.display.set_caption("@@@ |^|atrix @@@ (created by Verzhak - verzhak@gmail.com)")
pygame.display.set_icon(pygame.image.load("image/icon.png"))

main_surf.fill((0,0,0))
pygame.display.flip()

#if my_hello.main_loop(main_surf): #TODO раскомментировать
	
if my_console.main_loop(main_surf):
		
	pass

