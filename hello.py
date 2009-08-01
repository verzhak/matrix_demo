#!/home/amv/env/bin/python3
#coding=utf-8

import pygame

class CHello:

	class CHelloStr:

		def __init__(self, rsl, str, font_size,
				font_name = "monotype", font_color = (255,255,255), pos = None, only = False):
			self.__rsl = rsl
			self.str = str
			self.len = len(str)

			self.fsize = font_size

			font = pygame.font.Font(pygame.font.match_font(font_name),self.fsize)

			if only == True:
				self.surf = font.render(self.str,True,font_color)
				self.height = self.surf.get_rect().height
				self.width = self.surf.get_rect().width
			else:
				self.surf = []
				for x in range(0, self.len):
					self.surf.append(font.render(self.str[x],True,font_color))
				self.height = self.surf[0].get_rect().height
				self.width = self.surf[0].get_rect().width * self.len

			if pos == None:
				pos = ((self.__rsl[0] - self.width) / 2, (self.__rsl[1] - self.height) / 2)

			self.set_pos(pos)

		def set_pos(self, pos):
			self.pos = pos
			self.rect = pygame.Rect(self.pos,(self.width, self.height))

		def symbol_pos_x(self, x):
				return (self.pos[0] + x * self.fsize / 2, self.pos[1])

	def __init__(self, rsl):
		self.__shot = 0
		self.__rsl = rsl

		self.__name = self.CHelloStr(self.__rsl, "Verzhak",36)
		self.__pres = self.CHelloStr(self.__rsl, "presented:",14)
		self.__pres.set_pos((self.__pres.pos[0], self.__pres.pos[1] + self.__name.height / 2))
		self.__date = self.CHelloStr(self.__rsl, "(02.08.2009)",14,only = True)
		self.__date.set_pos((self.__rsl[0] - self.__date.width, self.__rsl[1] - self.__date.fsize - 3))
		# TODO убрать self.__matrix = self.CHelloStr("MATRIX",72,"arial",(0,150,0))
		# TODO убрать self.__has_you = self.CHelloStr("has you",14,"arial",(0,150,0))

		self.event_type = pygame.USEREVENT + 1
		pygame.time.set_timer(self.event_type,100)

	def do_shot(self,main_surf):
		if 0 < self.__shot < (self.__name.len + 1):
			main_surf.fill(main_surf.get_at((0,0)), rect = self.__name.rect)
			for x in range(0,self.__shot):
				main_surf.blit(self.__name.surf[x], self.__name.symbol_pos_x(x))

		if self.__name.len < self.__shot < (self.__name.len + self.__pres.len + 1):
			main_surf.fill(main_surf.get_at((0,0)), rect = self.__pres.rect)

			for x in range(0,self.__shot - self.__name.len):
				main_surf.blit(self.__pres.surf[x],self.__pres.symbol_pos_x(x))

		if (self.__name.len + self.__pres.len) < self.__shot < (self.__name.len + self.__pres.len +15):
			main_surf.blit(main_surf,(0, - self.__rsl[1] / 30))

		if (self.__name.len + self.__pres.len + 15) == self.__shot:
			main_surf.blit(self.__date.surf, self.__date.pos)

		self.__shot = self.__shot + 1

		return main_surf

