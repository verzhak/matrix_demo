#!/home/amv/env/bin/python3
#coding=utf-8

import pygame

class CBase:

	def __init__(self, event_num, event_delay = 100):
		
		self.__event_num = event_num
		self.__event_delay = event_delay
		self.cur_shot = 0

	def do_shot(self, main_surf):

		print("[Переопределить метод]")

	def main_loop(self, main_surf):

		event_type = pygame.USEREVENT + self.__event_num
		pygame.time.set_timer(event_type, self.__event_delay)

		run = 1
		while run == 1:
			event = pygame.event.poll()
			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_ESCAPE:
					run = 0
			elif event.type == event_type:
				temp_surf = self.do_shot(main_surf.copy())
				if temp_surf == None:
					run = 0
					main_surf.fill((0,0,0))
				else:
					main_surf.blit(temp_surf, (0,0))
				pygame.display.flip()

class CStr:

		def __init__(self, rsl, str, font_size,
				font_name = "monotype", font_color = (255,255,255), pos = None, only = False):

			self.__rsl = rsl
			self.__only = only
			self.str = str
			self.len = len(str)

			self.fsize = font_size

			font = pygame.font.Font(pygame.font.match_font(font_name),self.fsize)

			if self.__only == True:
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

		def draw(self, main_surf, x = 0):
			
			if self.__only == True:

				main_surf.blit(self.surf, self.pos)

			else:

				main_surf.blit(self.surf[x],
						(self.pos[0] + sum(map(lambda x: x.get_width(), self.surf[0 : x])),
							self.pos[1]))

