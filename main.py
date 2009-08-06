#!/home/amv/env/bin/python3

import pygame
from hello import CHello
from console import CConsole
from encoding import CEnc
from base import rsl

pygame.init()

main_surf = pygame.display.set_mode(rsl)

main_surf.fill((0,0,0))

my_hello = CHello(main_surf)
my_console = CConsole(main_surf)
my_enc = CEnc(main_surf)

pygame.display.set_caption("@@@ |^|atrix @@@ (created by Verzhak - verzhak@gmail.com)")
pygame.display.set_icon(pygame.image.load("image/icon.png"))

pygame.display.flip()

if my_hello.main_loop():
	
	if my_console.main_loop():

		my_enc.main_loop()
