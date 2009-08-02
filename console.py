#!/home/amv/env/bin/python3
#coding=utf-8

import pygame
from base import CBase, CStr

class CConsole(CBase):

	def __init__(self, rsl):
		
		CBase.__init__(self, 2)

		self.__rsl = rsl

		self.__wakeup = CStr(rsl, "Wake up, Neo!", 14, font_color = (30, 189, 4), pos = (10,10))
		self.__has_you = CStr(rsl, "The Matrix has you...", 14,
				font_color = (30, 189, 4), pos = (10,25))
		self.__rabbit = CStr(rsl, "Follow the white rabbit...", 14,
				font_color = (30, 189, 4), pos = (10,40))
		self.__knock = CStr(rsl, "KNOCK, KNOCK", 32, font_color = (30, 189, 4))

	def do_shot(sel, main_surf):

		# TODO
		pass

